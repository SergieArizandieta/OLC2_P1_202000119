from enum import Enum


class tipo(Enum):
    ENTERO = 0,
    DECIMAL = 1,
    BOOLEANO = 2,
    CARACTER = 3,
    CADENA = 4,
    ERROR = 5


class Tipos():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = self.ObtenerTipo()

    def ObtenerTipo(self):
        if self.nombre == 'ENTERO':
            print("Se dectecto un entero")
            return tipo.ENTERO

        elif self.nombre == 'DECIMAL':
            print("Se dectecto un decimal")
            return tipo.DECIMAL

        elif self.nombre == 'CADENA':
            return tipo.CADENA

        elif self.nombre == 'BOOLEANO':
            return tipo.BOOLEANO

        elif self.nombre == 'CARACTER':
            return tipo.CARACTER

        else:
            return tipo.ERROR
