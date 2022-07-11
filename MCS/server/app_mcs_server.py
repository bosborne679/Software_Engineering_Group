import sys
import socket
import selectors
import traceback

import server


class _server_ignition():
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.store = server.mcs_store.storage()
        self.host = ""
        self.port = int(8080)
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


        self.lsock.bind((self.host, self.port))
        self.lsock.listen()
        print(f"Listening on {(self.host, self.port)}")
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)




    """accept wrapper handles a oppen connection without data flow"""
    def accept_wrapper(self, sock):
        #opens socket connection
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        #sets blocking to false
        conn.setblocking(False )
        #loads event data to message
        message = server.libmcs_server.Message(self.sel, conn, addr,self.store)
        #adds data to register
        self.sel.register(conn, selectors.EVENT_READ, data=message)

    def server_engine(self):



        """Start of server loop"""

        try:
            while True:
                #watches for events
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        #if no data in event, creates empty connection
                        self.accept_wrapper(key.fileobj)
                    else:
                        #if data is in event sets message equal to event data
                        message = key.data
                        try:
                            #processes message data
                            message.process_events(mask)
                        except Exception:
                            #handles errors in data and cleans message data
                            print(f"Main: Error: Exception for {message.addr}:\n"
                                f"{traceback.format_exc()}")
                            message.close()

        except KeyboardInterrupt:
            #waits for keybord to stop run time
            print("Caught  keyboard interrupt, exiting")

        finally:
            #final clean up of selection items
            self.sel.close()

