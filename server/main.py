import socket # Сокеты для подключения
import threading # Многопоток для нескольких клиентов
from database import main as hs # Запись истории действий и обработка параметров пользователей
import datetime # Для получения текущего времени и даты
import json # Для пересылки словарей



HOST = '127.0.0.1'

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

    print(str(datetime.datetime.now()), mask, 'подключился')

    clients[mask] = connection

    for c in clients.keys():
        clients[c].send(json.dumps({
            'sender': 'server',
            'text': mask + 'подключился',
            'all': True
        }).encode())

    while True:

        try:

            messange = connection.recv(1024).decode()

            if not messange:

                print(str(datetime.datetime.now()), mask, 'отключился')

                for c in clients.keys():

                    clients[c].send(json.dumps({
                        'sender': 'Сервер',
                        'text': mask + ' отключился',
                        'all': True
                    }).encode())

                break

            else:

                print(str(datetime.datetime.now()), mask + ':', messange)

                for c in clients.keys():

                    clients[c].send(json.dumps({
                        'sender': mask,
                        'text': messange,
                        'all': True
                    }).encode())

        except:

            print(str(datetime.datetime.now()), mask, 'отключился')

            del clients[mask]

            for c in clients.keys():

                clients[c].send(json.dumps({
                    'sender': 'Сервер',
                    'text': mask + ' отключился',
                    'all': True
                }).encode())



# Цикл ожидания подключения клиентов

while True:

    connection, addr = s.accept()

    client_thread = threading.Thread(target=handle_client, args=(connection, str(addr)))
    client_thread.start()
