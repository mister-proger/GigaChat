import socket
import time
import pyaudio
import threading

# конфигурация сервера
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1042

# конфигурация аудио
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# инициализация PyAudio
audio = pyaudio.PyAudio()

# открытие захвата микрофона
input_stream = audio.open(format=FORMAT, channels=CHANNELS,
    rate=RATE, input=True,
    frames_per_buffer=CHUNK_SIZE)

# открытие вывода аудио
output_stream = audio.open(format=FORMAT, channels=CHANNELS,
    rate=RATE, output=True,
    frames_per_buffer=CHUNK_SIZE)

# создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# подключение к серверу
client_socket.connect((SERVER_HOST, SERVER_PORT))


def send_audio(conn, input_stream):

    try:

        while True:

            conn.sendall(input_stream.read(1024))

    except:

        return None



def recv_audio(conn, output_stream):

    try:

        while True:

            output_stream.write(conn.recv(1024))

    except:

        return None


thread_input_stream = threading.Thread(target=send_audio, args=(client_socket, input_stream))
thread_output_stream = threading.Thread(target=recv_audio, args=(client_socket, output_stream))

thread_output_stream.start()
thread_input_stream.start()

while True:

    time.sleep(1)
