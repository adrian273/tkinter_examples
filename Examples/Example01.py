from tkinter import *
import time

def parpadear():
    root.iconify()
    time.sleep(3)
    root.deiconify()

root = Tk()
root.title('Ventana con evento')
boton = Button(root, text="Evento", command= parpadear)
boton.pack()

root.mainloop()
