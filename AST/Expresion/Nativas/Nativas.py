from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo
import math
import copy

class Nativas(Expresion):

    def __init__(self, expresion, funcion):
        self.expresion = expresion
        self.funcion = funcion

    def ObtenerValor(self, controlador, ts):

        valor_exp1 = self.expresion.ObtenerValor(controlador, ts)
        tipo_exp1 = self.expresion.ObtenerTipo(controlador, ts)
        print("=== exp === ", self.expresion)
        print("=== exp valor === ",valor_exp1)
        print("=== exp tipo === ", tipo_exp1)
        print("=== exp tipo py === ", type(valor_exp1))
        print("=== exp tipo py === ", type(2))

        if self.funcion == "abs":
            if tipo_exp1 == tipo.ENTERO or tipo_exp1 == tipo.DECIMAL:
                return abs(valor_exp1)

        elif self.funcion == "sqrt":
            if tipo_exp1 == tipo.DECIMAL:
                return math.sqrt(valor_exp1)

        elif self.funcion == "to_string()" or self.funcion == "to_owned()":
            if tipo_exp1 == tipo.DIRSTRING:
                return valor_exp1

        elif self.funcion == "clone()":
            return copy.deepcopy(valor_exp1)
           # return copy.deepcopy(self.expresion)

    def ObtenerTipo(self, controlador, ts):

        tipo_exp1 = self.expresion.ObtenerTipo(controlador, ts)

        if self.funcion == "abs":
            if tipo_exp1 == tipo.ENTERO or tipo_exp1 == tipo.DECIMAL:
                return tipo_exp1

        elif self.funcion == "sqrt":
            if tipo_exp1 == tipo.DECIMAL:
                return tipo_exp1

        elif self.funcion == "to_string()" or self.funcion == "to_owned()":
            if tipo_exp1 == tipo.DIRSTRING:
                return tipo.STRING

        elif self.funcion == "clone()":
            return tipo_exp1
