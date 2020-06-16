## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
 
from tkinter import *


def sumar():
    total.set(v1.get()+v2.get())


def restar():
    total.set(v1.get()-v2.get())


def multiplicar():
    total.set(v1.get()*v2.get())


def dividir():
    total.set(v1.get()/v2.get())


root = Tk()
root.title("Calculadora")
Label(root,text="Primer numero").pack()
v1 = IntVar()
Entry(root,textvariable=v1).pack()
Label(root,text="segundo numero").pack()
v2 = IntVar()
Entry(root,textvariable=v2).pack()

Button(root,text = "+",command=sumar).pack(side=LEFT)
Button(root,text = "-",command=restar).pack(side=LEFT)
total = IntVar()
Label(root,text="",textvariable=total).pack(side=LEFT)
Button(root,text = "*",command=multiplicar).pack(side=LEFT)
Button(root,text = "/",command=dividir).pack(side=LEFT)

root.mainloop()