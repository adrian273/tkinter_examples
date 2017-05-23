from tkinter import *

def hello():
    print(name.get())

ROOT = Tk()

ROOT.title('App 2')
ROOT.geometry('800x600')

name = StringVar()
surname = StringVar()

name_label = Label(text='Ingresa nombre').place(x=10, y=10)
name_input = Entry(ROOT, textvariable=name).place(x=150, y=10)
surname_label = Label(text='Ingresa apellido').place(x=10, y=50)
surname_input = Entry(ROOT, textvariable=surname).place(x=150, y=50)
button = Button(ROOT, text='Saludar', command=hello).place(x=10, y=150)
ROOT.mainloop()
