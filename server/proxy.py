import ABOTP
import threading

HOST, PORT = '127.0.0.1', 1042

clients = []


def handler(conn):
    print(f'{conn} подключился')
    while True:
        try:
            data = conn.recv()
        except ConnectionResetError:
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
                except ConnectionResetError:
                    print(f'{client} отключился')
                    clients.remove(client)


sock = ABOTP.Server()
sock.bind((HOST, PORT))
sock.listen()
while True:
    conn, addr = sock.accept()
    clients.append(conn)
    threading.Thread(target=handler, args=(conn,)).start()
