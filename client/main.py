import sys
import threading
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication
import ABOTP
import handler


mods = handler.mods
del handler

sock = ABOTP.Client()


class EventFilter(QObject):
    def __init__(self, tabs):
        super().__init__()
        self.tabs = tabs

    def eventFilter(self, obj, event):
        if isinstance(obj, QTabWidget):
            if event.type() == QEvent.Show:
                index = obj.currentIndex()
                print("Current Tab Index:", index)
        return super().eventFilter(obj, event)


class App(QMainWindow):
    def __init__(self, mods):
        super().__init__()
        self.mods = mods
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)
        self.start_setup()

    def start_setup(self):
        for key, value in self.mods.items():
            print(key, value['code'], mods, sep = ' | ')
            self.mods[key]['widget'] = value['code'](sock)
            self.tab.addTab(self.mods[key]['widget'].layout(), key)
        print('О да', mods)

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
