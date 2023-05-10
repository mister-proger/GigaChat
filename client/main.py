import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import socket
import threading
import datetime
import json
import ctypes
import pyaudio
from THAudio import encode_audio, decode_audio


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')



# json.loads: str -> dict
# json.dumps: dict -> str



window = tk.Tk()

window.title('GigaChat')

window.iconbitmap('GigaChad.ico')



connection = ()

status = False


def window_chat(string):

    chat.configure(state = tk.NORMAL)

    chat.insert(END, string + '\n')

    chat.configure(state = tk.DISABLED)

    return None



def recv_connect():

    try:

        while status:

            data = json.loads(connection.recv(1024).decode())

            try:

                print(data)

                if data.get('type', None) == 'text':

                    if data.get('recipient', 'all') == 'all':

                        edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + data['sender'] + ': ' + data['text']

                    else:

                        edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + data['sender'] + ' -> ' + data['recipient'] + ': ' + data['text']

                elif data.get('type', None) == 'audio':

                    play(decode_audio(data['data']))

            except:

                edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + 'ERROR FOR RECV MESSENGE'

            window_chat(str(edit_data))

        window_chat('----- DISCONNECT {' + input_str_server_mask.get() + '} -----')

        return None

    except:

        window_chat('----- DISCONNECT {' + input_str_server_mask.get() + '} | SERVER KICK -----')

    window_chat('----- DISCONNECT {' + input_str_server_mask.get() + '} -----')

    return None



def send_mess(event = None):

    global status

    if not input_str.get() or not status:

        return None

        if not status:

            status = False

    else:

        if not input_recipient_str.get():

            connection.sendall(json.dumps({
                'text': input_str.get(),
                'sender': input_str_mask.get(),
                'recipient': 'all'
            }).encode())

            input_str.delete(0, 'end')

        else:

            connection.sendall(json.dumps({
                'text': input_str.get(),
                'sender': input_str_mask.get(),
                'recipient': input_recipient_str.get()
            }).encode())

            input_str.delete(0, 'end')

def play(audio_data):

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    p = pyaudio.PyAudio()

    stream.write(audio_data)

    stream.stop_stream()

    stream.close()

    p.terminate()

def record():

    """Записывает один чанк аудио с микрофона и возвращает его в виде строки"""
    CHUNK = 1024  # Размер блока записываемых данных
    FORMAT = pyaudio.paInt16  # Формат записываемых данных (16-битный целочисленный)
    CHANNELS = 1  # Количество каналов (моно)
    RATE = 44100  # Частота дискретизации (44100 Гц)

    p = pyaudio.PyAudio()  # Создаем объект PyAudio

    # Открываем поток записи аудио
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Записываем один чанк аудио
    data = stream.read(CHUNK)

    # Останавливаем поток записи аудио и закрываем объект PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    return encode_audio(data)

def send_audio():

    while True:

        while audio_status.get() and status:

            connection.sendall(json.dumps({
                'type': 'audio',
                'data': record()
            }).encode())

        time.sleep(0.2)



def start_connect():

    global recv_connect

    global status

    status = False

    HOST = input_str_HOST.get()

    try:

        PORT = int(input_str_PORT.get())

    except:

        window_chat('----- ERROR PORT | ' + input_str_PORT.get() + ' -----')

        return None


    global connection


    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        connection.connect((HOST, PORT))

    except:

        window_chat('----- ERROR CONNECT {' + input_str_server_mask.get() + '} | ERROR-DATA -----')

        return None

    status = True
    window_chat('----- CONNECT {' + input_str_server_mask.get() + '} -----')

    connection.sendall(input_str_mask.get().encode())
    
    recv_thread = threading.Thread(target = recv_connect)

    recv_thread.start()




if True:

    tab_control = ttk.Notebook(window)

    tab_chat = ttk.Frame(tab_control)
    tab_control.add(tab_chat, text = 'Чат')

    tab_setting = ttk.Frame(tab_control)
    tab_control.add(tab_setting, text = 'Параметры')

    tab_audio = ttk.Frame(tab_control)
    tab_control.add(tab_audio, text = 'Звонок')



if True:

    chat = Text(tab_chat, state = DISABLED, width = 80)

    scrollbar = Scrollbar(chat)
    scrollbar.place(relheight = 1, relx = 0.974)

    chat.grid(column = 0, row = 1, columnspan = 3)


    input_str = Entry(tab_chat)

    input_str.grid(column = 0, row = 2, sticky='nesw')


    send_button = Button(tab_chat, text = 'send', command = send_mess)

    window.bind('<Return>', send_mess)

    send_button.grid(column = 1, row = 2)


    input_recipient_str = Entry(tab_chat)

    input_recipient_str.grid(column = 2, row = 2, sticky='nesw')



if True:

    str_HOST = Label(tab_setting, text = 'IP')

    str_HOST.grid(column=0, row=0)


    str_PORT = Label(tab_setting, text = 'Port')

    str_PORT.grid(column=0, row=1)


    str_server_mask = Label(tab_setting, text = 'Server mask')

    str_server_mask.grid(column=0, row=2)


    str_mask = Label(tab_setting, text = 'Login')

    str_mask.grid(column = 0, row = 3)


    input_str_HOST = Entry(tab_setting)

    input_str_HOST.grid(column = 1, row = 0)


    input_str_PORT = Entry(tab_setting)

    input_str_PORT.grid(column = 1, row = 1)


    input_str_server_mask = Entry(tab_setting)

    input_str_server_mask.grid(column = 1, row = 2)


    input_str_mask = Entry(tab_setting)

    input_str_mask.grid(column=1, row=3)


    button_start_connect = Button(tab_setting, text = 'Try connect', command = start_connect)

    button_start_connect.grid(column = 2, row = 0, rowspan = 4, sticky = 'nsew')



if True:

    audio_status = tk.BooleanVar()

    CB_audio_status = tk.Checkbutton(tab_setting, text = 'Включить аудио', variable = audio_status)

    CB_audio_status.grid(column = 0, row = 4, columnspan = 3, sticky = 'nsew')

threading.Thread(target=send_audio).start()


tab_control.grid(row = 0, sticky = 'w')

status = False


window.mainloop()

status = False
