## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

from tkinter import *
from tkinter import ttk


def alta():
    e = Toplevel(root)
    e.title("Ingresar")
    e.geometry('380x200')
    Label(e, text="Ingrese la ciudad").grid(column=0, row=0)
    ciudad = StringVar()
    Entry(e, textvariable=ciudad).grid(column=0, row=1)
    Label(e, text="Ingrese el codigo postal").grid(column=0, row=2)
    codigo = StringVar()
    Entry(e, textvariable=codigo).grid(column=0, row=3)
    Button(e, text="Cargar", command= lambda : guardar(ciudad,codigo) ).grid(column=0, row=4)

    def guardar(ciudad, codigo):
        treeview.insert("", END, text=(ciudad.get() + " " + codigo.get()))
        e.destroy()

def editar(posicion):
    ciudadCodigo = treeview.item(posicion)["text"]
    e = Toplevel(root)
    e.title("Ingresar")
    e.geometry('380x200')
    Label(e, text="Ingrese la ciudad").grid(column=0, row=0)
    ciudad = StringVar()
    ciudad.set(ciudadCodigo[:ciudadCodigo.find(" ")])
    Entry(e, textvariable=ciudad).grid(column=0, row=1)
    Label(e, text="Ingrese el codigo postal").grid(column=0, row=2)
    codigo = StringVar()
    codigo.set(ciudadCodigo[ciudadCodigo.find(" "):])
    Entry(e, textvariable=codigo).grid(column=0, row=3)
    Button(e, text="Guardar", command= lambda : guardar(ciudad,codigo) ).grid(column=0, row=4)

    def guardar(ciudad, codigo):
        treeview.item(posicion, text=(ciudad.get() + " " + codigo.get()))
        e.destroy()

def baja():
    seleccionado = treeview.selection()[0]
    treeview.delete(seleccionado)
def modificar():
    seleccionado = treeview.selection()[0]
    editar(seleccionado)

root = Tk()
treeview = ttk.Treeview(root,selectmode=BROWSE)
treeview.insert("",END, text = "Rosario 2000")
treeview.insert("",END, text = "Rafaela 2300")
treeview.insert("",END, text = "Santa fe 3000")
treeview.insert("",END, text = "Rufino 6100")
treeview.insert("",END, text = "Obera 3360")
treeview.grid(column = 0, row = 0)

Button(root, text="Alta", command=alta, font=("Agency FB", 14), width=10).grid(column = 0, row = 1)
Button(root, text="Baja", command=baja, font=("Agency FB", 14), width=10).grid(column = 1, row = 1)
Button(root, text="Modificar", command=modificar, font=("Agency FB", 14), width=10).grid(column = 2, row = 1)

root.mainloop()