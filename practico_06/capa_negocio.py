# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):
    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        :return: Socio | None
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        :return: Socio | None
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        :return: list
        """
        return self.datos.todos()

    def alta(self, socio: Socio):
        """
        Si se cumplen las validaciones se agrega un socios.
        :return: Boolean
        """
        if (self.regla_1(socio) and self.regla_2(socio) and self.regla_3()):
            self.datos.alta(socio)
            return True
        else:
            return None

    def baja(self, id_socio):
        """
        :return: Boolean
        """
        toDelete = self.buscar(id_socio)
        if toDelete is None:
            return False
        return self.datos.baja(id_socio)

    def modificacion(self, socio : Socio):
        """
        Si las validaciones son exitosas modifica al socio.
        :return: Boolean
        """
        if self.regla_2(socio) and (self.datos.modificacion(socio) is not None):
            return True
        return False

    def resetTabla(self):
        self.base.drop_all(self.engine)

    def regla_1(self, socio : Socio):
        """
        valida que el dni sea unico
        :raise: Se repite DNI
        :return: Boolean
        """
        socio_repe = self.buscar_dni(socio.dni)
        if socio_repe == None:
            return True
        else:
            raise DniRepetido('El DNI ya se ha utilizado')

    def regla_2(self, socio : Socio):
        """
        valida la longitud del nombre y apellido 3 < Len < 15
        :raise: Longitud incorrecta
        :return: Boolean
        """
        if (len(socio.nombre) < self.MIN_CARACTERES or len(socio.nombre) > self.MAX_CARACTERES):
            raise LongitudInvalida('ERROR: el nombre debe tener entre 3 y 15 caracteres.')
        elif (len(socio.apellido) < self.MIN_CARACTERES or len(socio.apellido) > self.MAX_CARACTERES):
            raise LongitudInvalida('ERROR: el apellido debe tener entre 3 y 15 caracteres.')
        return True

    def regla_3(self):
        """
        Validar que no se exceda la cantidad de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) > self.MAX_SOCIOS:
            raise MaximoAlcanzado('ERROR: ah superado el numero de socios maximo')
        else:
            return True
