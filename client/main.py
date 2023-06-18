import ctypes
import os
import sys
import threading
import ABOTP
import handler
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication

if os.name == 'nt':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('MrCompany.GigaChat')
del os
mods = handler.mods
del handler

sock = ABOTP.Client()


class EventFilter(QObject):
    def __init__(self, tabs):
        super().__init__()
        self.tabs = tabs

    def eventFilter(self, obj, event):
        return super().eventFilter(obj, event)


class App(QMainWindow):
    def __init__(self, mods):
        super().__init__()
        self.setWindowIcon(QIcon('GigaChad.ico'))
        self.mods = mods
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self.start_setup()

    def start_setup(self):
        for key, value in self.mods.items():
            self.mods[key]['widget'] = value['code'](sock)
            self.tab.addTab(self.mods[key]['widget'].layout(), key)
            del self.mods[key]['code']

    def handler(self, data):
        if data[0].decode() in self.mods.keys():
            self.mods[data[0].decode()]['widget'].handler(data)
        else:
            print(f'Странный и непонятный пакет: {data}')


def handler():
    while threading.main_thread().is_alive():
        if not sock.status:
            continue
        data = sock.recv()
        window.handler(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App(mods)
    eventer = EventFilter(mods.keys())
    del mods
    recv = threading.Thread(target=handler)
    recv.start()
    window.installEventFilter(eventer)
    window.show()
    sys.exit(app.exec_())
