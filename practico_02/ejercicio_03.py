"""# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni. """

from random import randint


class Persona:

    def __init__( self, nombre: str, edad: int, sexo: str, peso: float, altura: float ):
        """
        :param sexo:  H=hombre, M=mujer ,
        """
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo if sexo == "H" or sexo == "M" else ""
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def es_mayor_edad( self ):
        return self.edad >= 18

    # llamarlo desde __init__
    def generar_dni( self ):
        return randint(10000000, 99999999)

    def print_data( self ):
        print(self.nombre,
              self.edad,
              self.sexo,
              self.peso,
              self.altura,
              self.dni)
