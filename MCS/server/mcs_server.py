"""
File to handle the overall server instance.
A singleton of MCSServer will be created to communicate with each client
"""
import socket
import threading
import selectors
import sys
import types


class MCSServer():
    
    def __init__(self, host, port=8080):
        # Function sets values but does not start a server
        self._host = host
        self._port = port
        self._mcssocket = None

    @property
    def mcssocket(self):
        return self._mcssocket

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @host.setter
    def host(self, host):
        self._host = host

    @port.setter
    def port(self, port):
        self._port = port

    @mcssocket.setter
    def mcssocket(self, mcssocket):
        self._mcssocket = mcssocket

    def create_server(self):
        #creates socket
        self._mcssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._mcssocket.bind(self._host,self._port)

    def run_server(self):
        pass

    def kill_server(self):
        
        pass

    async def await_connect(self):
        #needs to be updated for background runtime
        self._mcssocket.listen(5)
        clientsocket, address = self._mcssocket.accept()
        print("socket connection from {address} ")
        pass

    async def close_connect(self):

       # self."connection".close()
        pass

    async def await_recieve(self,clientsocket):
        data = clientsocket.recv(1024)
        if data is not None:
            return data
        else:
            pass
        pass

    async def await_send(self,data,clientsocket):
        #send data
        self.clientsocket.sendall(data)

        pass
