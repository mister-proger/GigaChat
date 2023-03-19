import socket # Сокеты для подключения
import threading # Многопоток для нескольких клиентов
# from database import main as hs # Запись истории действий и обработка параметров пользователей
import datetime # Для получения текущего времени и даты
import json # Для пересылки словарей



HOST = '26.44.12.34'

PORT = 1042

clients = {}



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(10)



print('Сервер запущен на адресе', HOST + ':' + str(PORT))



# Хандлер клиентов

def handle_client(connection):

    global clients

    mask = connection.recv(1024).decode()

    print('<' + str(datetime.datetime.now()) + '>', mask, 'подключился')

    clients[mask] = connection

    for c in clients.keys():
        clients[c].send(json.dumps({
            'sender': 'server',
            'text': mask + ' подключился',
            'all': True
        }).encode())

    while clients.get(mask, False):

        try:

            messange = json.loads(connection.recv(1024).decode())

            if not messange:

                OH_NOT_CRINGE = 10 / 0

            else:

                if messange.get('recipient', 'all') == 'all':

                    print('<' + str(datetime.datetime.now()) + '>', mask + ':', messange['text'])

                    for c in clients.keys():

                        del_c = c

                        try:

                            clients[c].send(json.dumps({
                                'sender': mask,
                                'text': messange['text'],
                                'recipient': 'all'
                            }).encode())

                        except:

                            del clients[del_c]

                else:

                    print('<' + str(datetime.datetime.now()) + '>', mask, '->', messange['recipient'] + ':', messange['text'])

                    try:

                        clients[messange['recipient']].send(json.dumps({
                            'sender': mask,
                            'recipient': messange['You'],
                            'text': messange['text']
                        }).encode())

                        clients[mask].send(json.dumps({
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

                clients[c].send(json.dumps({
                    'sender': 'server',
                    'text': mask + ' отключился',
                    'recipient': 'all'
                }).encode())

            return None

    print('<' + str(datetime.datetime.now())[11:-10] + '>', mask, 'отключился')

    del clients[mask]

    for c in clients.keys():
        clients[c].send(json.dumps({
            'sender': 'server',
            'text': mask + ' отключился',
            'recipient': 'all'
        }).encode())

    return None



# Цикл ожидания подключения клиентов

while True:

    connection, addr = s.accept()

    client_thread = threading.Thread(target=handle_client, args=(connection))
    client_thread.start()