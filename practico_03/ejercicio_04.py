# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3 as db
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    var_db = db.connect('practico-03.db')
    cursor = var_db.cursor()
    sql = '''SELECT * FROM persona WHERE IdPersona = ?'''
    query_data = (id_persona,)
    result = cursor.execute(sql, query_data).fetchone()
    cursor.close()
    var_db.close()
    return result if result else False


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', str(datetime.datetime(1988, 5, 15)), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
