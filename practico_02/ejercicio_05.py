# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante as Es


def organizar_estudiantes( facultad: [Es] ) -> dict:
    dic_Carreras = dict()
    for estudiante in facultad:
        if estudiante.carrera not in dic_Carreras:
            dic_Carreras[estudiante.carrera] = 1
        else:
            dic_Carreras[estudiante.carrera] = dic_Carreras[estudiante.carrera] + 1
    return dic_Carreras


test = [Es("Lucas", 24, "H", 85, 18, "Sistemas", "2018", 18, 6),
                    Es("Juan", 24, "H", 85, 18, "Sistemas", "2018", 18, 6),
                    Es("Marcos", 24, "H", 85, 18, "Sistemas", "2018", 18, 6),
                    Es("Otro", 24, "H", 85, 18, "quimica", "2018", 18, 6),
                    Es("Otro", 24, "H", 85, 18, "civil", "2018", 18, 6),
                    Es("Otro", 24, "H", 85, 18, "civil", "2018", 18, 6)]

assert organizar_estudiantes(test) == {'Sistemas': 3, 'civil': 2, 'quimica': 1 }
