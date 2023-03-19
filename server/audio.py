import socket
import threading

# конфигурация сервера
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1052

# создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключение сокета к хосту и порту
server_socket.bind((SERVER_HOST, SERVER_PORT))

# прослушивание сокета
server_socket.listen()

# список клиентов
clients = []

# отправка данных другим клиентам
def broadcast_data(client_socket, data):
    for c in clients:
        if c != client_socket:
            try:
                c.sendall(data)  # отправка данных
            except:
                clients.remove(c)  # удалить отключенных клиентов

# обработка клиентских соединений
def handle_client(client_socket):
    while True:
        try:
            # получение данных от клиента
            data = client_socket.recv(2048)

            # отправка данных другим клиентам
            broadcast_data(client_socket, data)
        except:
            # удаление отключенных клиентов
            clients.remove(client_socket)
            client_socket.close()
            break

# принятие клиентских подключений
while True:
    # ожидание подключения
    client_socket, client_address = server_socket.accept()

    # добавление клиента в список клиентов
    clients.append(client_socket)

    # запуск обработчика клиента в отдельном потоке
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

# закрытие сокета
server_socket.close()
