from tkinter import *

def imprimir():
    print("Has presinado boton imprimir")

root = Tk()
root.title('Buttons')

'''
    @root.quit = Es para salir
    @fg = es el color que se le asigna al botton
'''
button_exit = Button(root, text="Salir", fg="red", command= root.quit)
'''
    pack(side = POSICINAMIENTO EN PANTALLA)
'''
button_exit.pack(side= LEFT)

button_print = Button(root, text="Imprimir", fg="blue", command= imprimir)
button_print.pack(side = RIGHT)

root.mainloop()
