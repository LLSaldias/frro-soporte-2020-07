# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.

class Rectangulo:

    def __init__( self, base: float, altura: float ):
        self.base = base
        self.altura = altura

    def area( self ):
        return self.base * self.altura


assert Rectangulo(10, 10).area() == 100
