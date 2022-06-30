"""
File to handle the overall server instance.
A singleton of MCSServer will be created to communicate with each client
"""
import socket
import threading


class MCSServer():
    def __init__(self, host, port):
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
        self._mcssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run_server(self):
        pass

    def kill_server(self):
        pass

    async def await_connect(self):
        pass

    async def await_recieve(self):
        pass

    async def await_send(self):
        pass
