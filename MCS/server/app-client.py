import sys
import socket
import selectors
import traceback

import libclient

#set the default selector for selecting server action
sel = selectors.DefaultSelector()


#creates a server request based off an action and value
def create_request(action, value):
    if action == "search":
        #returns a dictionary of type json with the server action request this will become the message
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    else:
        #returns a custom request dictionary
        return dict(
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


#opens a connection to the host server
def start_connection(host, port, request):
    addr = (host, port)
    print(f"Starting connection to {addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    #sets the server request event
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    #sets the server message
    message = libclient.Message(sel, sock, addr, request)
    #registeres the data eith the socket connection, event request, and data to send
    sel.register(sock, events, data=message)


if len(sys.argv) != 5:
    print(f"Usage: {sys.argv[0]} <host> <port> <action> <value>")
    sys.exit(1)
#imports system inputs
host, port = sys.argv[1], int(sys.argv[2])
#imports sysrtem inputs
action, value = sys.argv[3], sys.argv[4]
#uses request fuction to create a server event request
request = create_request(action, value)
#starts the connection on the given socket with the built request
start_connection(host, port, request)

try:
    while True:
        #builds an event selector call
        events = sel.select(timeout=1)
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
        if not sel.get_map():
            break
        #escape loop
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    #cleans up selector data
    sel.close()
