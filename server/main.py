import ABOTP
import threading
import json


HOST = '127.0.0.1'

PORT = 1042

clients = {}

socket = ABOTP.Server()

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

        if head == 'AUDIO':

            for client in clients.keys():

                if client != mask:

                    clients[client].send([head.encode(), packet[1]])

        elif head == 'MESS':

            mess = json.loads(packet[1].decode())

            print(mess)

            if mess['recipient'] == 'all':

                for client in clients.keys():

                    clients[client].send(['MESS'.encode(), json.dumps({
                        'sender': mask,
                        'recipient': 'all',
                        'text': mess['text']
                    }).encode()])

            else:

                try:

                    clients[mask].send(['MESS'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': mess['recipient'],
                        'sender': 'You'
                    }).encode()])

                    clients[mess['recipient']].send(['MESS'.encode(), json.dumps({
                        'text': mess['text'],
                        'recipient': 'You',
                        'sender': mess['recipient']
                    }).encode()])

                except KeyError:

                    clients[mask].send(['MESS'.encode(), json.dumps({
                        'text': 'Ошибка отправки личного сообщения',
                        'recipient': 'server',
                        'sender': 'You'
                    }).encode()])

        elif head == 'COMMAND':

            command = packet[1].decode()

            if command == 'mask':

                exm_mask = ' '.join([x.decode() for x in packet[2:]])

                if exm_mask in ['server', 'You'] + list(clients.keys()):

                    clients[mask].send(['MESS'.encode(), json.dumps({
                        'text': 'Данный псевдоним занят или запрещён',
                        'recipient': 'server',
                        'sender': 'You'
                    }).encode()])

                    continue

                old_mask = mask

                del clients[mask]

                mask = exm_mask

                clients[mask] = conn

                print(f'Смена никнейма: {old_mask} -> {mask}')

                for client in clients.keys():

                    clients[client].send(['MESS'.encode(), json.dumps({
                        'sender': 'server',
                        'recipient': 'all',
                        'text': f'Смена никнейма: {old_mask} -> {mask}'
                    }).encode()])

                del old_mask

            elif command == 'users':

                print(list(clients.keys()))

                clients[mask].send(['COMMAND'.encode(), 'users'.encode()] + [x.encode() for x in list(clients.keys())])

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
