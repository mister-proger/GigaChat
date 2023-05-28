import ABOTP
import struct
import threading
import json


HOST = '127.0.0.1'

PORT = 1052

socket = ABOTP.Server()

socket.bind((HOST, PORT))

socket.listen()

print('Сервер запущен на адресе', HOST + ':' + str(PORT))


class Clients:

    def __init__(self):

        self.masks = []

        self.sockets = []

    def append(self, mask, _socket):

        self.masks.append(mask)

        self.sockets.append(_socket)

    def close(self, mask):

        index = self.masks.index(mask)

        self.sockets[index].close()

        self.masks.pop(index)

        self.sockets.pop(index)

    def set_mask(self, old, new):

        self.masks[self.masks.index(old)] = new

    def __iter__(self):

        for _socket in self.sockets:

            yield _socket

    def __getitem__(self, item):

        # print(type(item), item, self.masks, self.sockets, sep = ' || ')

        if type(item) is str and item in self.masks:

            return self.sockets[self.masks.index(item)]

        else:

            raise KeyError(f'Неверная маска клиента: {item}')


clients = Clients()


def handle_client(conn):

    mask = str(conn)

    clients.append(mask, conn)

    print(f'Клиент {mask} подключён')

    while True:

        try:

            packet = conn.recv()

        except (ConnectionResetError, ConnectionAbortedError, ConnectionError, ConnectionRefusedError):

            break

        head = packet[0].decode()

        if head == 'AUDIO':

            for client in clients:

                if client != conn:

                    client.send([head.encode(), packet[1]])

        elif head == 'mess':

            mess = json.loads(packet[1].decode())

            # print(mess)

            if mess['recipient'] == 'all':

                for client in clients:

                    client.send(['mess'.encode(), json.dumps({
                        'sender': mask,
                        'recipient': 'all',
                        'text': mess['text']
                    }).encode()])

            else:

                try:

                    clients[mask].send(['mess'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': mess['recipient'],
                        'sender': 'You'
                    }).encode()])

                    clients[mess['recipient']].send(['mess'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': 'You',
                        'sender': mess['recipient']
                    }).encode()])

                except KeyError:

                    clients[mask].send(['mess'.encode(), json.dumps({
                        'text': 'Ошибка отправки личного сообщения',
                        'recipient': 'server',
                        'sender': 'You'
                    }).encode()])

        elif head == 'command':

            command = packet[1].decode()

            if command == 'mask':

                exm_mask = ' '.join([x.decode() for x in packet[2:]])

                if exm_mask in ['server', 'You'] + list(clients.masks):

                    clients[mask].send(['mess'.encode(), json.dumps({
                        'text': 'Данный псевдоним занят или запрещён',
                        'recipient': 'server',
                        'sender': 'You'
                    }).encode()])

                    continue

                clients.set_mask(mask, exm_mask)

                print(f'Смена никнейма: {mask} -> {exm_mask}')

                for client in clients:

                    client.send(['mess'.encode(), json.dumps({
                        'sender': 'server',
                        'recipient': 'all',
                        'text': f'смена никнейма | {mask} -> {exm_mask}'
                    }).encode()])

                mask = exm_mask

            elif command == 'users':

                print('Подключённые клиенты:', list(clients))

                clients[mask].send(['command'.encode(), 'users'.encode()] + [x.encode() for x in clients])

        else:

            print(f'Неизвестный формат сообщения {head}')

    try:

        clients.close(mask)

    except ValueError:

        pass

    print(f'Клиент {mask} отключился')

    return None


def console():

    while True:

        try:

            command = input().split(' ')

            # print(command, clients, clients.masks, clients.sockets, sep = ' || ')

            if command[0] == 'kick':

                try:

                    clients.close(' '.join(command[1:]))

                except KeyError:

                    print(f'Клиент {" ".join(command[1:])} не найден')

            else:

                raise TypeError

        except TypeError:

            print('Неверная команда')

        # print(command, clients, clients.masks, clients.sockets, sep = ' || ')


command_thread = threading.Thread(target = console)

command_thread.start()

while True:

    connection, addr = socket.accept()

    client_thread = threading.Thread(target = handle_client, args = (connection,))

    client_thread.start()
