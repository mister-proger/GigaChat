import socket # Сокеты для подключения
import threading # Многопоток для нескольких клиентов
# from database import main as hs # Запись истории действий и обработка параметров пользователей
import datetime # Для получения текущего времени и даты
import json # Для пересылки словарей



HOST = '192.168.0.169'

PORT = 1042

clients = {}



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(10)



print('Сервер запущен на адресе', HOST + ':' + str(PORT))



# Хандлер клиентов

def handle_client(connection, addr):

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

    while True:

        try:

            messange = json.loads(connection.recv(1024).decode())

            if not messange:

                break

            else:

                if messange.get('recipient', 'all') == 'all':

                    print('<' + str(datetime.datetime.now()) + '>', mask + ':', messange['text'])

                    for c in clients.keys():

                        clients[c].send(json.dumps({
                            'sender': mask,
                            'text': messange['text'],
                            'recipient': 'all'
                        }).encode())

                else:

                    print('<' + str(datetime.datetime.now()) + '>', mask, '->', messange['recipient'] + ':', messange['text'])

                    clients[messange['recipient']].send(json.dumps({
                        'sender': mask,
                        'recipient': messange['recipient'],
                        'text': messange['text']
                    }))

                    clients[mask].send(json.dumps({
                        'sender': mask,
                        'recipient': messange['recipient'],
                        'text': messange['text']
                    }))

        except:

            print('<' + str(datetime.datetime.now()) + '>', mask, 'отключился')

            del clients[mask]

            for c in clients.keys():

                clients[c].send(json.dumps({
                    'sender': 'server',
                    'text': mask + ' отключился',
                    'recipient': 'all'
                }).encode())



# Цикл ожидания подключения клиентов

while True:

    connection, addr = s.accept()

    client_thread = threading.Thread(target=handle_client, args=(connection, str(addr)))
    client_thread.start()