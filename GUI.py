
from tkinter import Tk, Label, Button, Entry


class VentanaEjemplo:

    def __init__(self, master):
        self.master = master
        master.title("CRUD")
        
        self.etiqueta = Label(master, text='BIENVENIDOS AL SISTEMA DE VENTAS')
        self.etiqueta.grid(row=0,column=0)
        self.etiqueta1 = Label(master, text='Qué deseas hacer hoy?')
        self.etiqueta1.grid(row=1,column=0)
        self.etiqueta2 = Label(master, text='[C]rear un cliente')
        self.etiqueta2.grid(row=2,column=0)
        self.etiqueta3 = Label(master, text='[L]istar clientes')
        self.etiqueta3.grid(row=3,column=0)
        self.etiqueta4 = Label(master, text='[A]ctualizar un cliente')
        self.etiqueta4.grid(row=4,column=0)
        self.etiqueta5 = Label(master, text='[E]liminar un cliente')
        self.etiqueta5.grid(row=5,column=0)
        self.etiqueta6 = Label(master, text='[B]uscar un cliente')
        self.etiqueta6.grid(row=6,column=0)

        self.entrada = Entry(master)
        self.entrada.grid(row=7, column=0)

        self.botonSaludo = Button(master, text="Ingresar opción", command=self.menu)
        self.botonSaludo.grid(row=8,column=0)
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.grid(row=9,column=0)

    def menu(self):
        print(f"Se eligió {self.entrada.get()}")


root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()