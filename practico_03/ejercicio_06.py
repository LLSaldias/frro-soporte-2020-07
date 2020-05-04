# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import sqlite3 as db
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    query = "CREATE TABLE IF NOT EXISTS Peso(IdPersona int, Fecha Date NOT NULL, Peso int, PRIMARY KEY (Fecha), FOREIGN KEY (IdPersona) REFERENCES Persona(IdPersona))"
    cursor.execute(query)
    db_var.commit()
    db_var.close()
    pass


def borrar_tabla_peso():
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    cursor.execute("DROP TABLE IF EXISTS Peso")
    db_var.commit()
    db_var.close()
    pass

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
