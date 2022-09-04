from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import Tipos, RetornoType

class Primitivo(Expresion):

    def __init__(self, valor, tipo,linea,columna) :
        self.valor = valor
        self.tipo = Tipos(tipo)
        self.linea=linea
        self.columna=columna

    def ObtenerValor(self, controlador, ts) -> RetornoType:
        return RetornoType(self.valor,self.tipo.tipo)



