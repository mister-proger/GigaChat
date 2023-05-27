import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
import json
import ctypes
import ABOTP
import handler


class Semaphore:

    def __init__(self, meaning: bool):

        self.semaphore = meaning

    def set(self, meaning: bool) -> None:

        self.semaphore = meaning

    def get(self) -> bool:

        return self.semaphore

    def __repr__(self):

        return f'Semaphore | Value: {self.semaphore}'


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')

window = tk.Tk()

window.title('GigaChat')

window.iconbitmap('GigaChad.ico')

connection = ABOTP.Client()

status = Semaphore(meaning = False)

func = [x[:-5] for x in handler.get_mods()]

# print(func)


def window_chat(string):

    chat.configure(state = tk.NORMAL)

    chat.insert(END, string + '\n')

    chat.configure(state = tk.DISABLED)

    return None


def recv_connect():

    try:

        while status.get():

            data = None

            try:

                data = connection.recv()

                print(data)

                head = data[0].decode()

                if head in func:

                    # print(head, data, sep = ' | ')

                    # print(f'handler.call({head}, {data})')

                    exec(eval(f'handler.call("{head}", {data})'))

                else:

                    print(f'Отсутствует метод обработки сообщений - {head}')

            except KeyError:

                window_chat(f'Проблема с получанием сообщения: {data}')

    except OSError as error:

        window_chat(f'----- DISCONNECT {input_str_server_mask.get()} | ERROR {error} -----')

        status.set(False)

        return None

    else:

        window_chat(f'----- DISCONNECT {input_str_server_mask.get()} -----')

        status.set(False)

        return None


def send_mess(event = None):

    mess = input_str.get()

    if mess.startswith('/'):

        connection.send(['command'.encode()] + [x.encode() for x in mess[1:].split()])

        input_str.delete(0, 'end')

    else:

        if not mess or not status.get():

            return None

        else:

            try:

                if not input_recipient_str.get():

                    connection.send(['mess'.encode(), json.dumps({
                        'text': mess,
                        'sender': input_str_mask.get(),
                        'recipient': 'all'
                    }).encode()])

                else:

                    connection.send(['mess'.encode(), json.dumps({
                        'text': mess,
                        'sender': input_str_mask.get(),
                        'recipient': input_recipient_str.get()
                    }).encode()])

                input_str.delete(0, 'end')

            except OSError as error:

                window_chat(f'----- SENDING ERROR {error} -----')


def start_connect():

    host = input_str_HOST.get()

    try:

        port = int(input_str_PORT.get())

    except ValueError:

        window_chat(f'----- ERROR PORT | {input_str_PORT.get()} -----')

        return None

    try:

        connection.connect((host, port))

    except OSError as error:

        window_chat(f'----- ERROR CONNECT {input_str_server_mask.get()} | ERROR {error} -----')

        return None

    status.set(True)

    window_chat(f'----- CONNECT {input_str_server_mask.get()} -----')
    
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
    chat.grid(column=0, row=1, columnspan=3)

    scrollbar = Scrollbar(chat)
    scrollbar.place(relheight = 1, relx = 0.974)

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

# if True:
#
#     audio_status = tk.BooleanVar()
#
#     CB_audio_status = tk.Checkbutton(tab_setting, text = 'Включить аудио', variable = audio_status)
#
#     CB_audio_status.grid(column = 0, row = 4, columnspan = 3, sticky = 'nsew')


tab_control.grid(row = 0, sticky = 'w')

window.mainloop()

status.set(False)
