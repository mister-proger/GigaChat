import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
import json
import ctypes
import ABOTP
from typing import Optional
import handler


class Semaphore:

    def __init__(self, meaning: Optional[bool] = False):

        self.semaphore = meaning

    def __repr__(self):

        return f'Semaphore | Value: {self.semaphore}'

    def set(self, meaning: bool) -> None:

        self.semaphore = meaning

    def get(self) -> bool:

        return self.semaphore


def s_loader():

    packet = {}

    def load_lang(lang):

        with open(f'./langs/{lang}.lang', encoding='utf-8') as _file:

            for _line in _file.readlines():

                _param, _data = _line[:-1].split('=', 1)

                packet[_param] = _data

        return packet

    _setting = {'setting': {}}

    with open('GigaChat.setting', encoding='utf-8') as file:

        for line in file.readlines():

            param, data = line[:-1].split('=', 1)

            _setting['setting'][param] = data

    _setting['lang'] = load_lang(_setting['setting']['lang'])

    return _setting


setting = s_loader()

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')

window = tk.Tk()

window.title('GigaChat')

window.iconbitmap('GigaChad.ico')

connection = ABOTP.Client()

status = Semaphore(meaning = False)

func = [x[:-5] for x in handler.get_mods()]


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

                head = data[0].decode()

                if head in func:

                    req = eval(f'handler.call("{head}", {data})')

                    if type(req) is str:

                        window_chat(req)

                else:

                    print(f'Отсутствует метод обработки сообщений - {head}')

            except KeyError:

                window_chat(f'Проблема с получанием сообщения: {data}')

    except OSError as error:

        window_chat(f'----- DISCONNECT | ERROR {error} -----')

        connection.close()

        status.set(False)

        return None

    else:

        window_chat(f'----- DISCONNECT -----')

        connection.close()

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

    connection.__init__()

    host = input_str_HOST.get()

    try:

        port = int(input_str_PORT.get())

    except ValueError:

        window_chat(f'----- ERROR PORT | {input_str_PORT.get()} -----')

        return None

    try:

        connection.connect((host, port))

    except OSError as error:

        window_chat(f'----- ERROR CONNECT | {error} -----')

        return None

    status.set(True)

    window_chat(f'----- CONNECT -----')
    
    recv_thread = threading.Thread(target = recv_connect)

    recv_thread.start()


if True:

    tab_control = ttk.Notebook(window)

    tab_chat = ttk.Frame(tab_control)
    tab_control.add(tab_chat, text = setting['lang']['chat'].title())

    tab_setting = ttk.Frame(tab_control)
    tab_control.add(tab_setting, text = setting['lang']['param'].title())

if True:

    chat = Text(tab_chat, state = DISABLED, width = 80)
    chat.grid(column=0, row=1, columnspan=3)

    scrollbar = Scrollbar(chat)
    scrollbar.place(relheight = 1, relx = 0.974)

    input_str = Entry(tab_chat)
    input_str.grid(column = 0, row = 2, sticky='nesw')

    send_button = Button(tab_chat, text = setting['lang']['send'].title(), command = send_mess)
    window.bind('<Return>', send_mess)
    send_button.grid(column = 1, row = 2)

    input_recipient_str = Entry(tab_chat)
    input_recipient_str.grid(column = 2, row = 2, sticky='nesw')

if True:

    str_HOST = Label(tab_setting, text = setting['lang']['host'].title())
    str_HOST.grid(column = 0, row = 0)

    str_PORT = Label(tab_setting, text = setting['lang']['port'].title())
    str_PORT.grid(column = 0, row = 1)

    str_mask = Label(tab_setting, text = setting['lang']['name'].title())
    str_mask.grid(column = 0, row = 2)

    input_str_HOST = Entry(tab_setting)
    input_str_HOST.grid(column = 1, row = 0)

    input_str_PORT = Entry(tab_setting)
    input_str_PORT.grid(column = 1, row = 1)

    input_str_mask = Entry(tab_setting)
    input_str_mask.grid(column = 1, row = 2)

    button_start_connect = Button(tab_setting, text = setting['lang']['connect'].title(), command = start_connect)
    button_start_connect.grid(column = 2, row = 0, rowspan = 3, sticky = 'nsew')


tab_control.grid(row = 0, sticky = 'w')

window.mainloop()

status.set(False)
