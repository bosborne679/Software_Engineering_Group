import sys
import socket
import selectors
import traceback

import libserver

#creates a default selector
sel = selectors.DefaultSelector()


#function creates a server request handler
def accept_wrapper(sock):
    #opens socket connection
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    #sets blocking to false
    conn.setblocking(False )
    #loads event data to message
    message = libserver.Message(sel, conn, addr)
    #adds data to register
    sel.register(conn, selectors.EVENT_READ, data=message)

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)
#loads input
host, port = sys.argv[1], int(sys.argv[2])
#builds socket handle
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sets socket option to be open
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#binds socket to given port
lsock.bind((host, port))
#sets socket to listen for requests
lsock.listen()
print(f"Listening on {(host, port)}")
#sets blocking to off
lsock.setblocking(False)
#sets selection register
sel.register(lsock, selectors.EVENT_READ, data = None)


try:
    while True:
        #watches for events
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                #if no data in event, creates empty connection
                accept_wrapper(key.fileobj)
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
    sel.close()


