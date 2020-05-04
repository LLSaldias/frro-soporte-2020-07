# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3 as db
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona

def agregar_peso(id_persona, fecha, peso):
    db_var = db.connect('practico-03.db')
    cursor = db_var.cursor()
    persona = buscar_persona(id_persona)
    ult_fecha = True
    persona_peso = buscar_persona_peso(id_persona)
    if persona_peso != False: ult_fecha = persona_peso[1] < str(fecha)   #COMARO FECHAS PERO CON FORMATO STRING, CORREGIR
    if persona and ult_fecha:
        sql = 'INSERT OR REPLACE INTO Peso(IdPersona, Fecha, Peso) values(?,?,?)'
        query_data = (id_persona, fecha, peso,)
        cursor.execute(sql, query_data)
    else:
        return False
    db_var.commit()
    id_registro = cursor.lastrowid
    db_var.close()
    return id_registro

def buscar_persona_peso(id_persona):
    var_db = db.connect('practico-03.db')
    cursor = var_db.cursor()
    sql = '''SELECT * FROM Peso WHERE IdPersona = ?'''
    query_data = (id_persona,)
    result = cursor.execute(sql, query_data).fetchone()
    cursor.close()
    var_db.close()
    return result if result else False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
