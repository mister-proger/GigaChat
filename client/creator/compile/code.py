from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextOption
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton


class Main:

    def __init__(self, socket, lang = 'RU_ru'):
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
        if self.widgets['input']['mess'].text() and self.socket.status:
            self.socket.send(['mess'.encode(), self.widgets['input']['mess'].text().encode()])
            self.widgets['input']['mess'].clear()

    def handler(self, packet):
        self.widgets['show'].setReadOnly(False)
        self.widgets['show'].append(packet[1].decode())
        self.widgets['show'].setReadOnly(True)

    def layout(self):
        return self.widget
