#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual). """
from datetime import datetime
from ejercicio_03 import Persona


class Estudiante(Persona):

    def __init__( self,
                  nombre: str,
                  edad: int,
                  sexo: str,
                  peso: float, altura: float,
                  carrera: str,
                  anio: str,
                  cant_Materias: int,
                  mat_Aprobadas: int ):
        self.carrera = carrera
        self.anio = anio
        self.cant_Materias = cant_Materias
        self.mat_Aprobadas = mat_Aprobadas
        Persona.__init__(self, nombre, edad, sexo, peso, altura)

    def avance( self ):
        avg = (self.cant_Materias / self.mat_Aprobadas) * 100
        return round(avg, 2)

    # implementar usando modulo datetime
    def edad_ingreso( self ):
        ingreso = datetime.strptime(self.anio, "%Y").year
        actual = datetime.utcnow().year
        cursados = actual - ingreso
        return self.edad - cursados
