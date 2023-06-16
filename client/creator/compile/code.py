import datetime
import json
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton


class Main:
    def __init__(self, socket, lang='RU_ru'):
        self.socket = socket
        self.lang = lang

        self.widget = QWidget()
        self.widgets = {
            'layouts': {
                'main': QVBoxLayout(),
                'input': QHBoxLayout()
            },
            'show': QTextEdit(),
            'input': {
                'mess': QLineEdit(),
                'button': QPushButton('Send'),
                'recipient': QLineEdit()
            }
        }

        self.widgets['show'].setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.widgets['show'].setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.widgets['show'].setWordWrapMode(QTextOption.NoWrap)
        self.widgets['show'].setReadOnly(True)
        self.widgets['input']['button'].clicked.connect(self.send)
        self.widgets['input']['recipient'].setMaximumWidth(220)

        self.widgets['layouts']['input'].addWidget(self.widgets['input']['mess'])
        self.widgets['layouts']['input'].addWidget(self.widgets['input']['button'])
        self.widgets['layouts']['input'].addWidget(self.widgets['input']['recipient'])
        self.widgets['layouts']['main'].addWidget(self.widgets['show'])
        self.widgets['layouts']['main'].addLayout(self.widgets['layouts']['input'])

        self.widget.setLayout(self.widgets['layouts']['main'])

    def send(self):
        mess = self.widgets['input']['mess'].text()
        recipient = self.widgets['input']['recipient'].text()

        if not mess or not self.socket.status:
            return

        try:
            if not recipient:
                self.socket.send(['mess'.encode(), json.dumps({
                    'text': mess,
                    'sender': 'Me',
                    'recipient': 'all'
                }).encode()])
            else:
                self.socket.send(['mess'.encode(), json.dumps({
                    'text': mess,
                    'sender': 'Me',
                    'recipient': recipient
                }).encode()])

            self.widgets['input']['mess'].clear()
        except OSError as error:
            self.widgets['show'].append(f'----- SENDING ERROR {error} -----')

    def handler(self, packet):
        mess = json.loads(packet[1].decode())
        time = f'<{datetime.datetime.now().strftime("%H:%M")}>'

        if mess['recipient'] == 'all':
            opp = mess['sender']
        else:
            opp = f"{mess['sender']} -> {mess['recipient']}"

        self.widgets['show'].append(time + ' ' + opp + ': ' + mess['text'])

    def layout(self):
        return self.widget
