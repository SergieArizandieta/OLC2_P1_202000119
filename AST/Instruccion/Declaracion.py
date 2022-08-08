from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos

class Declaracion(Intruccion):

    def __init__(self, id:Identificador, expresion, tipo ):
        self.id = id
        self.expresion = expresion
        self.tipo = tipo

    def EjecutarInstruccion(self, controlador, ts):

        retornoExpresion = self.expresion.ObtenerValor(controlador,ts)

        newSimbolo = Simbolos()
        newSimbolo.iniciarSimboloPrimitivo(self.id.id, retornoExpresion, tipo=self.tipo)
        ts.Agregar_Simbolo(self.id.id, newSimbolo)