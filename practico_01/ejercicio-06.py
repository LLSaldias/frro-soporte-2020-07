# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.

def multiplicar( lista ):
    total = 1
    for i in lista:
        total = total * i
    return total


nums = [1, 3, 4]
assert multiplicar(nums) == 12
