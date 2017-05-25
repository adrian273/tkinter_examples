#!/usr/bin/env python
# coding=utf-8

'''
    github: adrian273
'''
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    print('Modulo TKINTER requerido')

def cal_suma():
    suma = number1.get() + number2.get()
    messagebox.showinfo('Resultados', str(suma))

def cal_rest():
    res = number1.get() - number2.get()
    messagebox.showinfo('Resultados', str(res))

def cal_mul():
    mul = number1.get() * number2.get()
    messagebox.showinfo('Resultados', str(mul))

def cal_div():
    div = number1.get() / number2.get()
    messagebox.showinfo('Resultados', str(div))

def widgets(ROOT):
    label_n1 = Label(ROOT, text='Ingrese un numero').place(x=10, y=10)
    label_n2 = Label(ROOT, text='Ingrese un numero').place(x=10, y=50)
    text_box_n1 = Entry(ROOT, textvariable=number1).place(x=150, y=10)
    text_box_n2 = Entry(ROOT, textvariable=number2).place(x=150, y=50)
    button_sum = Button(ROOT, text='Sumar', command=cal_suma, bg='#13c9e2').place(x=10, y=125)
    button_rest = Button(ROOT, text='Restar', command=cal_rest, bg='#13c9e2').place(x=70, y=125)
    button_mul = Button(ROOT, text='Multiplicar', command=cal_mul, bg='#13c9e2').place(x=140, y=125)
    button_div = Button(ROOT, text='Dividir', command=cal_div, bg='#13c9e2').place(x=220, y=125)
    button_exit = Button(ROOT, text='Salir', command=ROOT.quit, bg='#e80000').place(x=380, y=125)

if __name__ == '__main__':
    ROOT  = Tk()
    ROOT.title('Adrian Examples')
    ROOT.geometry('450x350')
    number1 = IntVar()
    number2 = IntVar()
    widgets(ROOT)
    ROOT.mainloop()
    ROOT.destroy()
