import socket
import threading
import datetime
import json
import ctypes

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, BooleanProperty

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')

class ChatTab(TabbedPanel):
    chat = ObjectProperty(None)
    input_str = ObjectProperty(None)
    input_recipient_str = ObjectProperty(None)
    input_str_mask = ObjectProperty(None)
    input_str_HOST = ObjectProperty(None)
    input_str_PORT = ObjectProperty(None)
    input_str_server_mask = ObjectProperty(None)
    button_start_connect = ObjectProperty(None)

    connection = ObjectProperty()
    status = BooleanProperty(False)

    def window_chat(self, string):
        self.chat.editable = True
        self.chat.text += string + '\n'
        self.chat.editable = False

    def recv_connect(self):
        while self.status:
            data = json.loads(self.connection.recv(1024).decode())

            try:
                print(data)

                if data.get('recipient', 'all') == 'all':
                    edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + data['sender'] + ': ' + data['text']
                else:
                    edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + data['sender'] + ' -> ' + data['recipient'] + ': ' + data['text']

            except:
                edit_data = '<' + str(datetime.datetime.now())[11:-10] + '> ' + 'ERROR FOR RECV MESSENGE'

            self.window_chat(str(edit_data))

    def send_mess(self, event=None):
        if not self.input_str.text or not self.status:
            return None
        else:
            if not self.input_recipient_str.text:
                self.connection.send(json.dumps({
                    'text': self.input_str.text,
                    'sender': self.input_str_mask.text,
                    'recipient': 'all'
                }).encode())
                self.input_str.text = ''
            else:
                self.connection.send(json.dumps({
                    'text': self.input_str.text,
                    'sender': self.input_str_mask.text,
                    'recipient': self.input_recipient_str.text
                }).encode())
                self.input_str.text = ''

    def start_connect(self):
        self.status = False
        HOST = self.input_str_HOST.text

        try:
            PORT = int(self.input_str_PORT.text)
        except:
            self.window_chat('----- ERROR PORT | ' + self.input_str_PORT.text + ' -----')
            return None

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connection.connect((HOST, PORT))
        except:
            self.window_chat('----- ERROR CONNECT {' + self.input_str_server_mask.text + '} | ERROR-DATA -----')
            return None

        self.status = True
        self.window_chat('----- CONNECT {' + self.input_str_server_mask.text + '} -----')

        self.connection.send(self.input_str_mask.text.encode())
        recv_connect = threading.Thread(target=self.recv_connect)

        recv_connect.start()


class GigaChatApp(App):
    def build(self):
        return Builder.load_file('gigachat.kv')


