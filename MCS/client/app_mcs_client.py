import sys
import socket
import selectors
import traceback

import libmcs_client

class _clientobj():
    def __init__(self, host, port):
        self.sel = selectors.DefaultSelector()
        self.host = host
        self.port = port
        self.action = None
        self.value = None
        self.request = None


    def create_request(self,action, value):
        if action == "search":
        #returns a dictionary of type json with the server action request this will become the message
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, value=value),
            )
        elif action == "store":
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, value=value),
            )
        elif action == "get":
            return dict(
                type="text/json",
                encoding = "utf-8",
                content=dict(action=action,value=value),
            )
        else:
        #returns a custom request dictionary
            return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(action + value, encoding="utf-8"),
            )

    def start_connection(self,request):
        addr = (self.host, self.port)
        print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libmcs_client.Message(self.sel, sock, addr, request)
        self.sel.register(sock, events, data=message)

    def get_action(self):
        print(f"Connected to: <{self.host}> <{self.port}>")
        self.action = input("Enter action: ")
        if self.action == "store":

            self.value = input("Enter value: ")
        else:
            self.value = "Whatever"

    def event_loop(self):
        self.request = self.create_request(self.action,self.value)

        self.start_connection(self.request)
        try:
            while True:
        #builds an event selector call
                events = self.sel.select(timeout=1)
                for key, mask in events:
            #loads return messages data
                    message = key.data
                    try:
                #processes message data
                        message.process_events(mask)
                    except Exception:
                        print(
                            f"Main: Error: Exception for {message.addr}:\n"
                            f"{traceback.format_exc()}"
                        )
                #cleans up message data
                        message.close()
        # Check for a socket being monitored to continue.
                if not self.sel.get_map():
                    break
        #escape loop
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
    #cleans up selector data
            self.sel.close()









