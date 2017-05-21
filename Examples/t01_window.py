from tkinter import *
from tkinter import ttk

def main():
    '''
        instancio TK
    '''
    window = Tk()
    '''
        Label(donde lo dibujo, texto a aparecer)
    '''
    label = Label(window, text="Hola Mundo tkinter")
    '''
        para adaptar la ventana:: metodo pack
    '''
    label.pack()
    '''
        para interactuar con la ventana
    '''
    window.title("Esta es mi primera ventana")
    '''
        @buuton = Button(donde se dibuja, texto, accion a realizar)
    '''
    buuton = Button(window, text="Minimizar", command= window.iconify)
    buuton.pack()
    
    window.mainloop()


if __name__ == '__main__':
    main()
