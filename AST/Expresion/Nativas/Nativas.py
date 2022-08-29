from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
import math
import copy

class Nativas(Expresion):

    def __init__(self, expresion, funcion):
        self.expresion = expresion
        self.funcion = funcion

    def ObtenerValor(self, controlador, ts):

        return_exp1: RetornoType = self.expresion.ObtenerValor(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo
        print("=== exp === ", self.expresion)
        print("=== exp valor === ",valor_exp1)
        print("=== exp tipo === ", tipo_exp1)
        print("=== exp tipo py === ", type(valor_exp1))
        print("=== exp tipo py === ", type(2))

        if self.funcion == "abs()":
            if tipo_exp1 == tipo.ENTERO or tipo_exp1 == tipo.DECIMAL:
                return RetornoType(abs(valor_exp1),tipo_exp1)

        elif self.funcion == "sqrt()":
            if tipo_exp1 == tipo.DECIMAL:
                return RetornoType(math.sqrt(valor_exp1), tipo_exp1)

        elif self.funcion == "to_string()" or self.funcion == "to_owned()":
            if tipo_exp1 == tipo.DIRSTRING:
                return RetornoType(valor_exp1, tipo.STRING)

        elif self.funcion == "clone()":
            return RetornoType(copy.deepcopy(valor_exp1), tipo_exp1)

        elif self.funcion == "len()":
            return_exp1: RetornoType = ts.ObtenerSimbolo(self.expresion.id)
            if isinstance(return_exp1,InstanciaArreglo):
                return RetornoType(len(return_exp1.valores), tipo.ENTERO)





