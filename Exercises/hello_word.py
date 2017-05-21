#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class App:

    def __init__(self):
        root = Tk()
        root.geometry("300x200")
        root.configure(bg = 'beige')
        root.title('App Hello word')
        ttk.Button(root, text = 'Salir', command = root.destroy).pack(side = BOTTOM)
        root.mainloop()

def main():
    app = App()

if __name__ == '__main__':
    main()
