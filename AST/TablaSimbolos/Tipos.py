from enum import Enum


class tipo(Enum):
    ENTERO = 0,
    DECIMAL = 1,
    BOOLEANO = 2,
    CARACTER = 3,
    STRING = 4,
    DIRSTRING = 5,
    UNDEFINED = 6,
    ERROR =7


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

        elif self.nombre == 'DIRSTRING':
            print("Se dectecto una DIRSTRING")
            return tipo.DIRSTRING

        elif self.nombre == 'STRING':
            print("Se dectecto una STRING")
            return tipo.STRING

        elif self.nombre == 'BOOLEANO':
            return tipo.BOOLEANO


        else:
            return tipo.ERROR
