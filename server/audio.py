import socket
import threading
import time

# конфигурация сервера
SERVER_HOST = '192.168.0.165'
SERVER_PORT = 1052

# создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключение сокета к хосту и порту
server_socket.bind((SERVER_HOST, SERVER_PORT))

# прослушивание сокета
server_socket.listen()

# список клиентов
clients = []

# обработка клиентских соединений
def handle_client(client_socket):
    while True:
        try:
            # получение данных от клиента
            data = client_socket.recv(2048)
            for c in clients:
                try:
                    c.sendall(data)  # отправка данных
                except:
                    clients.remove(c)  # удалить отключенных клиентов
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
