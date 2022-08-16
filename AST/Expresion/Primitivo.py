from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import Tipos


class Primitivo(Expresion):

    def __init__(self, valor, tipo):
        self.valor = valor
        print("tIPO ", tipo)
        self.tipo = Tipos(tipo)
        print("Se declaro  un primitivo: ", self.valor, " de tipo: ", self.tipo.tipo)

    def ObtenerValor(self, controlador, ts):
        return self.valor

    def ObtenerTipo(self, controlador, ts):
        return self.tipo.tipo

