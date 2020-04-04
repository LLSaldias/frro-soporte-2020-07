# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.

def mitad( palabra ):
    palLen = len(palabra)
    palPos = palLen//2 if palLen % 2 == 0 else palLen//2 +1
    palabra = palabra[:palPos]
    return palabra


palPar = 'casa'
palImpar = 'perro'
assert mitad(palPar) == 'ca'
assert mitad(palImpar) == 'per'
