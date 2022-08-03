from AST.Abstracto.Instruccion import Intruccion


class Imprimir(Intruccion):

    def __init__(self,  expresion, tipo):
        self.expresion = expresion
        self.tipo = tipo

    def EjecutarInstruccion(self, controlador, ts):
        valor = self.expresion.ObtenerValor(controlador,ts)
        controlador.imprimir(str(round(valor, 15)),self.tipo)
