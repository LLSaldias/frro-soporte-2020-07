# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        self.base = Base.metadata
        self.engine = engine

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).get(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.dni == dni_socio).one_or_none()

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios_searched = self.session.query(Socio).all()
        list_socios = []
        for s in socios_searched:
            list_socios.append(s)
        return list_socios

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Socio).delete()
            self.session.commit()
        except:
            return False
        finally:
            return True

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()
        return self.buscar_dni(socio.dni)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            socio_deleted = self.session.query(Socio).get(id_socio)
            self.session.delete(socio_deleted)
            self.session.commit()
        except:
            return False
        finally:
            return True

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """

        a_user = self.session.query(Socio).filter(Socio.id == socio.id).one_or_none()
        if a_user is None:
            return None
        a_user.dni = socio.dni
        a_user.nombre = socio.nombre
        a_user.apellido = socio.apellido
        self.session.commit()
        return self.session.query(Socio).get(socio.id)

    def resetTabla(self):
        self.base.drop_all(self.engine)



def pruebas():
    try:
        # alta
        datos = DatosSocio()
        socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        assert socio.id > 0
        print("test 1 Aprobado")

        # baja
        assert datos.baja(socio.id) is True
        print("test 2 Aprobado")

        # buscar
        socio2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
        assert datos.buscar(socio2.id) == socio2
        print("test 3 Aprobado")

        # buscar dni
        assert datos.buscar_dni(socio2.dni) == socio2
        print("test 4 Aprobado")

        # modificacion
        socio3 = datos.alta(Socio(dni=11222333, nombre='Lucas', apellido='Saldias'))
        socio3.nombre = 'Juan'
        socio3.apellido = 'Docampo'
        socio3.dni = 33222111
        datos.modificacion(socio3)
        socio3_1 = datos.buscar(socio3.id)
        assert socio3_1.id == socio3.id
        assert socio3_1.nombre == 'Juan'
        assert socio3_1.apellido == 'Docampo'
        assert socio3_1.dni == 33222111
        print("test 5 Aprobado")

        # todos
        assert len(datos.todos()) == 2
        print("test 6 Aprobado")

        # borrar todos
        datos.borrar_todos()
        assert len(datos.todos()) == 0
        print("test 7 Aprobado")

    finally:
        datos.resetTabla()




if __name__ == '__main__':
    pruebas()