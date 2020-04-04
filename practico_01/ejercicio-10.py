# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop( lista_1, lista_2 ):
    for num1 in lista_1:
        for num2 in lista_2:
            if num1 == num2:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set( lista_1, lista_2 ):
    dic1, dic2 = set(lista_1), set(lista_2)
    return True if dic1.intersection(dic2) is not None else False


assert (superposicion_loop([1,2,3], [3,4,5]))
assert not (superposicion_loop([1,2,3], [4,5,6]))
