# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final( lista ):
    for num in lista:
        if type(num) in (int, float, complex):
            lista.remove(num)
            lista.append(num)

    return lista


c1 = [1, 'a', 'b', 'c', 2]
assert numeros_al_final(c1) == ['a', 'b', 'c', 1, 2]
