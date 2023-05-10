import socket # Сокеты для подключения
import threading # Многопоток для нескольких клиентов
# from database import main as hs # Запись истории действий и обработка параметров пользователей
import datetime # Для получения текущего времени и даты
import json # Для пересылки словарей



HOST = '127.0.0.1'

PORT = 1052

clients = {}



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()



print('Сервер запущен на адресе', HOST + ':' + str(PORT))




# Хандлер клиентов

def handle_client(connection):

    global clients

    mask = connection.recv(1024).decode()

    if mask in clients.keys() or mask == 'server' or ' ' in mask or mask == 'all':

        connection.sendall(json.dumps({
            'sender': 'server',
            'text': 'Данный никнейм занят или содержит запрещённые символы или слова',
            'recipient': 'You'
        }).encode())

        return None

    print('<' + str(datetime.datetime.now()) + '>', mask, 'подключился')

    clients[mask] = connection

    for c in clients.keys():
        clients[c].sendall(json.dumps({
            'sender': 'server',
            'text': mask + ' подключился',
            'recipient': 'all'
        }).encode())

    while clients.get(mask, False):

        try:

            messange = b''

            while True:

                data_chunk = connection.recv(1024)

                if not data_chunk:

                    break

                messange += data_chunk

            messange = json.loads(messange.decode())

            if not messange:

                OH_NO_CRINGE = 10 / 0

            else:

                if messange.get('recipient', 'all') == 'all':

                    print('<' + str(datetime.datetime.now()) + '>', mask + ':', messange['text'])

                    for c in clients.keys():

                        del_c = c

                        try:

                            clients[c].sendall(json.dumps({
                                'type': 'text',
                                'sender': mask,
                                'text': messange['text'],
                                'recipient': 'all'
                            }).encode())

                        except:

                            del clients[del_c]

                else:

                    print('<' + str(datetime.datetime.now()) + '>', mask, '->', messange['recipient'] + ':', messange['text'])

                    try:

                        clients[messange['recipient']].sendall(json.dumps({
                            'sender': mask,
                            'recipient': 'You',
                            'text': messange['text']
                        }).encode())

                        clients[mask].sendall(json.dumps({
                            'sender': 'You',
                            'recipient': messange['recipient'],
                            'text': messange['text']
                        }).encode())

                    except:

                        clients[mask].send(json.dumps({
                            'sender': 'server',
                            'recipient': 'You',
                            'text': 'Не удалось отправить сообщение пользователю'
                        }).encode())

        except:

            print('<' + str(datetime.datetime.now()) + '>', mask, 'отключился')

            del clients[mask]

            for c in clients.keys():

                clients[c].sendall(json.dumps({
                    'sender': 'server',
                    'text': mask + ' отключился',
                    'recipient': 'all'
                }).encode())

            return None

    print('<' + str(datetime.datetime.now())[11:-10] + '>', mask, 'отключился')

    try:

        del clients[mask]

    finally:

        for c in clients.keys():
            clients[c].sendall(json.dumps({
                'sender': 'server',
                'text': mask + ' отключился',
                'recipient': 'all'
            }).encode())

    return None


def command():

    global clients

    while True:

        try:

            command = input().split(' ')

            if command[0] == 'kick':

                try:

                    del clients[' '.join(command[1:])]

                except:

                    print(f'Клиент {" ".join(command[1:])} не найден')

            else:

                assert OSError

        except:

            print('Неверная команда')


command_thread = threading.Thread(target = command)

command_thread.start()

# Цикл ожидания подключения клиентов

while True:

    connection, addr = s.accept()

    client_thread = threading.Thread(target = handle_client, args = (connection,))
    client_thread.start()
