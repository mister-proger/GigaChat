import tkinter as tk
from tkinter import *
from tkinter import ttk
import socket
import threading
import datetime
import json
import ctypes



ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')



# json.loads: str -> dict
# json.dumps: dict -> str



window = tk.Tk()

window.title('Добро пожаловать в ГигаЧат!')

window.iconbitmap('GigaChad.ico')



connection = ()

status = False


def window_chat(string):

    chat.configure(state = tk.NORMAL)

    chat.insert(END, string + '\n')

    chat.configure(state = tk.DISABLED)

    return None



def recv_connect():

    global connection

    global status

    while status:

        data = json.loads(connection.recv(1024).decode())

        try:

            print(data)

            if data.get('all', False):

                edit_data = str(datetime.datetime.now()) + ' ' + data['sender'] + ': ' + data['text']

            else:

                edit_data = str(datetime.datetime.now()) + ' ' + data['sender'] + ' -> You: ' + data['text']

        except:

            edit_data = str(datetime.datetime.now()) + ' Не удалось получить сообщение'

        window_chat(edit_data)



def send_mess(event = None):

    global connection

    if not input_str.get() or not status:

        return None

    else:

        connection.sendall(input_str.get().encode())

        input_str.delete(0, 'end')



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

        window_chat('----- ERROR CONNECT {' + input_str_server_mask.get() + '} | Ошибка данных подключения -----')

        return None


    window_chat('----- CONNECT {' + input_str_server_mask.get() + '} -----')

    connection.send(input_str_mask.get().encode())

    recv_connect = threading.Thread(target = recv_connect)

    recv_connect.start()

    status = True



if True:   # Создаём вкладки

    tab_control = ttk.Notebook(window)

    tab_chat = ttk.Frame(tab_control)
    tab_control.add(tab_chat, text = 'Чат')

    tab_setting = ttk.Frame(tab_control)
    tab_control.add(tab_setting, text = 'Параметры')



if True:   # Создаём виджеты для вкладки 'Чат'

    chat = Text(tab_chat, state = DISABLED, width = 80)

    scrollbar = Scrollbar(chat)
    scrollbar.place(relheight = 1, relx = 0.974)

    chat.grid(column = 0, row = 1, columnspan = 2)


    input_str = Entry(tab_chat)

    input_str.grid(column = 0, row = 2, sticky='nesw')


    send_button = Button(tab_chat, text = 'Отправить', command = send_mess, width = 15)

    window.bind('<Return>', send_mess)

    send_button.grid(column = 1, row = 2)



if True:   # Создаём виджеты параметров подключения

    str_HOST = Label(tab_setting, text = 'Адрес')

    str_HOST.grid(column=0, row=0)


    str_PORT = Label(tab_setting, text = 'Порт')

    str_PORT.grid(column=0, row=1)


    str_server_mask = Label(tab_setting, text = 'Псевдоним')

    str_server_mask.grid(column=0, row=2)


    str_mask = Label(tab_setting, text = 'Логин')

    str_mask.grid(column = 0, row = 3)


    input_str_HOST = Entry(tab_setting)

    input_str_HOST.grid(column = 1, row = 0)


    input_str_PORT = Entry(tab_setting)

    input_str_PORT.grid(column = 1, row = 1)


    input_str_server_mask = Entry(tab_setting)

    input_str_server_mask.grid(column = 1, row = 2)


    input_str_mask = Entry(tab_setting)

    input_str_mask.grid(column=1, row=3)


    button_start_connect = Button(tab_setting, text = 'Подключиться', command = start_connect)

    button_start_connect.grid(column = 2, row = 0, rowspan = 4, sticky = 'nsew')



tab_control.grid(row = 0, sticky = 'w')

window.mainloop()
