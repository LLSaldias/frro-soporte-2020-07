# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi


class Circulo:

    def __init__( self, radio: float ):
        self.radio = radio

    def area( self ):
        return self.radio ** 2 * pi

    def perimetro( self ):
        return self.radio * 2 * pi


assert Circulo(1).area() == pi
assert Circulo(0.5).perimetro() == pi
