# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
import sqlite3 as db
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    var_db = db.connect('practico-03.db')
    cursor = var_db.cursor()
    naci = str(nacimiento)
    query = "UPDATE Persona SET Nombre = \"%s\", FechaNacimiento = datetime(\"%s\") ,DNI = %i, altura = %i WHERE IdPersona = %i" %(nombre,naci,dni,altura,id_persona )
    print(query)
    cursor.execute(query)
    #var_db.commit()
    return False if cursor.rowcount == 0 else True


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
