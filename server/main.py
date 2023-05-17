import HPTP
import threading
import json


HOST = '127.0.0.1'

PORT = 1072

clients = {}

socket = HPTP.Server()

socket.bind((HOST, PORT))

socket.listen()

print('Сервер запущен на адресе', HOST + ':' + str(PORT))


def handle_client(conn):

    mask = str(conn)

    clients[mask] = conn

    print(f'Клиент {mask} подключён')

    while True:

        packet = conn.recv()

        head = packet[0].decode()

        if head == 'audio':

            for client in clients.keys():

                if client != mask:

                    clients[client].send(head.encode(), packet[1])

        elif head == 'mess':

            mess = json.loads(packet[1].decode())

            print(mess)

            if mess['recipient'] == 'all':

                for client in clients.keys():

                    clients[client].send('mess'.encode(), json.dumps({
                        'sender': mask,
                        'recipient': 'all',
                        'text': mess['text']
                    }).encode())

            else:

                try:

                    clients[mask].send('mess'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': mess['recipient'],
                        'sender': 'You'
                    }).encode())

                    clients[mess['recipient']].send('mess'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': 'You',
                        'sender': mess['recipient']
                    }).encode())

                except KeyError:

                    clients[mask].send('mess'.encode(), json.dumps({
                        'text': 'Ошибка отправки личного сообщения',
                        'recipient': 'server',
                        'sender': 'You'
                    }).encode())

        elif head == 'MASK':

            if packet[1].decode() in ['server', 'You'] + list(clients.keys()):

                clients[mask].send('mess'.encode(), json.dumps({
                    'text': 'Данный псевдоним занят или запрещён',
                    'recipient': 'server',
                    'sender': 'You'
                }).encode())

                continue

            old_mask = mask

            del clients[mask]

            mask = packet[1].decode()

            clients[mask] = conn

            print(f'Смена никнейма: {old_mask} -> {mask}')

            del old_mask

        else:

            print(f'Неизвестный формат сообщения {head}')


def console():

    while True:

        try:

            command = input().split(' ')

            if command[0] == 'kick':

                try:

                    del clients[' '.join(command[1:])]

                except KeyError:

                    print(f'Клиент {" ".join(command[1:])} не найден')

            else:

                raise TypeError

        except TypeError:

            print('Неверная команда')


command_thread = threading.Thread(target = console)

command_thread.start()

while True:

    connection, addr = socket.accept()

    client_thread = threading.Thread(target = handle_client, args = (connection,))

    client_thread.start()
