from tkinter import *

def hello():
    print('holaaaaa adrian')

root = Tk()
root.geometry('450x350')
root.title('aplicando lo aprendido')

button_print = Button(root, text='Saluda', fg='green', command=hello).place(x=10, y=30)
button_minify = Button(root, text='Minimizar', fg='orange', command=root.iconify).place(x=10, y=60)
button_exit = Button(root, text='Salir', fg='red', command=root.quit).place(x=10, y=90)
root.mainloop()
