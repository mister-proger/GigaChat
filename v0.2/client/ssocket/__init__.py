import json
import socket
from typing import Optional, Literal
import threading


class sclient:

    class con_central:

        def __init__(self, socket: socket.socket):
            def recv(socket: socket.socket):

                while super().__init__():

                    data = json.loads(socket.recv(2048).decode())

                    print(data)

            self.socket = socket

            self.thread.recv = threading.Thread(target = recv)

    def __init__(self, ip: str, packet_port: int, audio_port: int):

        self.address.packet = (ip, packet_port)

        self.address.audio = (ip, audio_port)

        self.socket.packet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.audio = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.status.central = False

        self.status.packet = False

        self.status.audio = False

    def get_address(self, param: Optional[Literal['packet', 'audio', 'all']] = 'all'):

        if param == 'packet':

            return self.address.packet

        elif param == 'audio':

            return self.address.audio

        elif param == 'all':

            return (self.address.packet, self.address.audio)

        else:

            raise ValueError('Ожидался параметр "packet" или "audio"')

    def central_server(self, ip: str, port: int):

        self.address.center = (ip, port)

        self.socket.central = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def try_connect_central(self, client_id: str):

        try:

            self.socket.central.connect(self.address.center)

            data = self.socket.central.recv(256)

            if data:

                self.status.central = True

                return True

            else:

                return False

        except WindowsError:

            raise f'Ошибка при подключении к центральному серверу {self.address.center}'
