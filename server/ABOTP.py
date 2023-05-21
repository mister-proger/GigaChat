import socket
import struct
from typing import Optional, List


class Client:

    def __init__(self, family: Optional[int] = socket.AF_INET):

        self.address = None

        self.sock = socket.socket(family, socket.SOCK_STREAM)

    def connect(self, address: tuple) -> None:

        self.sock.connect(address)

    def recv(self) -> List[bytes]:

        def picking(n):

            data = b''

            while len(data) < n:

                packet = self.sock.recv(n - len(data))

                if not packet:

                    return None

                data += packet

            return data

        num_objects = struct.unpack('>I', picking(4))[0]

        objects = []

        for _ in range(num_objects):

            len_data = struct.unpack('>I', picking(4))[0]

            obj_data = picking(len_data)

            objects.append(obj_data)

        return objects

    def send(self, objects: List[bytes]) -> None:

        num_objects = len(objects)

        packet = struct.pack('>I', num_objects)

        for obj in objects:
            packet += struct.pack('>I', len(obj)) + obj

        self.sock.sendall(packet)

    def close(self):

        self.sock.close()

    def __del__(self):

        self.sock.close()


class Server:
    class Client:

        def __init__(self, conn):

            self.conn = conn

        def recv(self) -> List[Optional[bytes]]:

            def picking(n):

                data = b''

                while len(data) < n:

                    packet = self.conn.recv(n - len(data))

                    if not packet:
                        return None

                    data += packet

                return data

            num_objects = struct.unpack('>I', picking(4))[0]

            objects = []

            for _ in range(num_objects):
                len_data = struct.unpack('>I', picking(4))[0]

                obj_data = picking(len_data)

                objects.append(obj_data)

            return objects

        def send(self, objects: List[bytes]) -> None:

            num_objects = len(objects)

            packet = struct.pack('>I', num_objects)

            for obj in objects:
                packet += struct.pack('>I', len(obj)) + obj

            self.conn.sendall(packet)

        def close(self):

            self.conn.close()

        def __del__(self):

            self.close()

    def __init__(self, family: Optional[int] = socket.AF_INET):

        self.address = None

        self.sock = socket.socket(family, socket.SOCK_STREAM)

    def bind(self, param: tuple) -> None:

        try:

            self.sock.bind(param)

        except TypeError as error:

            raise error

        except socket.gaierror as error:

            raise error

        else:

            self.address = param

    def accept(self) -> tuple:

        conn, addr = self.sock.accept()

        conn = self.Client(conn)

        return conn, addr

    def listen(self, backlog: Optional[int] = None) -> None:

        if backlog is None:

            self.sock.listen()

        else:

            self.sock.listen(backlog)

    def close(self):

        self.sock.close()

    def __del__(self):

        self.close()
