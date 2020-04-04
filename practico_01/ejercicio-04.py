# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor():
    celsius = float(input("Ingrese grados celsius: ")) * 9/5 + 32
    print(celsius)
    return celsius


