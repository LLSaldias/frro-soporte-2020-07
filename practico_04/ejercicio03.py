## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

from tkinter import *
from tkinter import ttk

root = Tk()

treeview = ttk.Treeview(root)
treeview.insert("",END, text = "Rosario 2000")
treeview.insert("",END, text = "Rafaela 2300")
treeview.insert("",END, text = "Santa fe 3000")
treeview.insert("",END, text = "Rufino 6100")
treeview.insert("",END, text = "Obera 3360")


treeview.pack()

root.mainloop()