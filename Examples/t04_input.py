from tkinter import *

def hello():
    '''
        para ver el valor de la variable gurdada utilizar get()
    '''
    print('Hola ' + name_var.get() + " " + surname_var.get() + " " +  surname_m_var.get())


root = Tk()
root.title('t04_input')
root.geometry('450x350')
'''
    @declaracion de variables
    para unirlas con las entradas de datoos
'''
name_var = StringVar()
surname_var = StringVar()
surname_m_var = StringVar()

label1 = Label(root, text='Escribe tu nombre').place(x=10, y=10)
'''
    paratros de Entry ->
    Entry(donde se dibuja, variable que se le unira)
    Entry sirve para entradas de textos
'''
name = Entry(root, textvariable=name_var).place(x=125, y=10)

label2 = Label(root, text='Escribe tu apellido').place(x=10, y=40)
surname = Entry(root, textvariable=surname_var).place(x=125, y=40)

label3 = Label(root, text='Escribe tu edad').place(x=10, y=70)
surname_m = Entry(root, textvariable=surname_m_var).place(x=125, y=70)

button_hello = Button(root, text="Saluda!", command=hello).place(x=10, y=100)

root.mainloop()
