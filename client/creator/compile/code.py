import threading

import pyaudio
from PyQt5.QtWidgets import QWidget, QCheckBox, QVBoxLayout


class Main:
    def __init__(self, socket):
        self.socket = socket
        self.widget = QWidget()
        self.widgets = {
            'checkboxes': {
                'play': QCheckBox("Play"),
                'handler': QCheckBox("Handler")
            },
            'layout': QVBoxLayout()
        }

        self.audio = {
            'format': pyaudio.paInt16,
            'channels': 2,
            'rate': 44100,
            'frames_per_buffer': 1024
        }

        self.widgets['checkboxes']['play'].stateChanged.connect(self.changer)
        self.widgets['checkboxes']['handler'].stateChanged.connect(self.changer)

        self.widgets['layout'].addWidget(self.widgets['checkboxes']['handler'])
        self.widgets['layout'].addWidget(self.widgets['checkboxes']['play'])
        self.widget.setLayout(self.widgets['layout'])

        self.thread_send = threading.Thread(target=self.sender)

        self.p = pyaudio.PyAudio()
        self.streams = {
            'input': self.p.open(
                **(self.audio | {'input': True})
            ),
            'output': self.p.open(
                **(self.audio | {'output': True})
            ),
        }

        self.thread_send.start()

    def sender(self):
        while threading.main_thread().is_alive():
            if not self.socket.status:
                continue
            self.socket.send([
                'ms-audio'.encode(),
                self.streams['input'].read(self.audio['frames_per_buffer'])
            ])

    def handler(self, packet):
        self.streams['output'].write(packet[1])

    def changer(self):
        if not self.widgets['checkboxes']['play'].isChecked():
            self.widgets['checkboxes']['handler'].setChecked(False)
            self.widgets['checkboxes']['handler'].setEnabled(False)
        else:
            self.widgets['checkboxes']['handler'].setEnabled(True)

    def layout(self):
        return self.widget
