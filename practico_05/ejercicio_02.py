# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio
from sqlalchemy import exc

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        if(self.session.query(Socio).filter(Socio.id == id_socio).count()==1):
            return self.session.query(Socio).filter(Socio.id == id_socio).first()
        else:
            return None

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        if (self.session.query(Socio).filter(Socio.dni == dni_socio).count() == 1):
            return self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        else:
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        sq = self.session.query(Socio).all()
        print(sq)
        return sq

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

        self.session.query(Socio).delete()
        self.session.commit()
        if(self.session.query(Socio).count()==0):
            return True
        else: return False

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        socio2 = Socio()
        socio2.dni = socio.dni
        socio2.nombre = socio.nombre
        socio2.apellido = socio.apellido
        try:
            self.session.add(socio2)
            self.session.commit()
        except exc.IntegrityError:
            self.session.rollback()
            socio2 = self.buscar_dni(socio.dni)
        return socio2

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        if(self.session.query(Socio).filter(Socio.id == id_socio).count()==1):
            self.session.query(Socio).filter(Socio.id == id_socio).delete()
            self.session.commit()
            return True
        else:
            return False

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """

        if(self.session.query(Socio).filter(Socio.id == socio.id).count() == 1):
            socioActualizado = self.session.query(Socio).filter(Socio.id == socio.id).first()
            socioActualizado.dni = socio.dni
            socioActualizado.nombre = socio.nombre
            socioActualizado.apellido = socio.apellido
            self.session.add(socioActualizado)
            self.session.commit()
            return socio
        else:
            return False


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()