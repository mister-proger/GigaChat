import ABOTP
import threading
import loader


properties = loader.properties_loader('./server.properties')

clients = []


def handler(conn):
    print(f'{conn} подключился')
    while True:
        try:
            data = conn.recv()
        except (ConnectionResetError, TypeError):
            print(f'{conn} отключился')
            break
        print(data)
        if not data:
            clients.remove(conn)
            print(f'{conn} отключился')
            break
        else:
            for client in clients:
                try:
                    client.send(data)
                except (ConnectionResetError, BrokenPipeError):
                    print(f'{client} отключился')
                    clients.remove(client)


sock = ABOTP.Server()
sock.bind((properties['HOST'], properties['PORT']))
sock.listen()

print(f'Сервер запущен на {properties["HOST"]}:{properties["PORT"]}')

while True:
    conn, addr = sock.accept()
    clients.append(conn)
    threading.Thread(target=handler, args=(conn,)).start()
