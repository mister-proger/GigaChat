import threading
import time
import tkinter as tk

def do_work():
    # Эта функция будет выполнена в другом потоке
    while True:

        while check_var.get():
                # Цикл будет продолжаться, пока флажок не будет сброшен
                print("Working...")

        time.sleep(0.02)

root = tk.Tk()

check_var = tk.BooleanVar()
check_button = tk.Checkbutton(root, text="Start", variable=check_var)
check_button.pack()

threading.Thread(target=do_work).start()

root.mainloop()
