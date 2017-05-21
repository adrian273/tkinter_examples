from tkinter import *

root = Tk()
root.title('t03_posicionamiento')

'''
    para dar el ancho y alto a la ventana
'''
root.geometry("400x200")
'''
    @ se utiliza grid para pocicionar grid(row = fila, column = columna ) esta es una forma
    para aserlo como tabla
    ejemplo ->

    etiqueta2 = Label(root, text = 'Posicionamiento 2').grid(row = 1, column = 1)
    boton2 = Button(root, text = 'Posicionamiento').grid(row = 2, column = 1)
'''

'''
    otra forma para pocicionar es utilizando place(x = valor_int, y = valor_int)
'''
boton = Button(root, text = 'Posicionamiento').place(x = 10, y = 10)
etiqueta = Label(root, text = 'Posicionamiento').place(x = 200, y = 10)

boton2 = Button(root, text = 'Posicionamiento').place(x = 10, y = 40)
etiqueta2 = Label(root, text = 'Posicionamiento').place(x = 200, y = 40)

root.mainloop()
