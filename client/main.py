import socket
import sys
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication
import handler


mods = handler.mods
del handler

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App(mods)
    eventer = EventFilter(mods.keys())
    del mods
    window.installEventFilter(eventer)
    window.show()
    sys.exit(app.exec_())
