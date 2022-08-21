from AST.Abstracto.Instruccion import Intruccion


class Return(Intruccion):
    def __init__(self,  expresion):
        self.expresion = expresion

    def EjecutarInstruccion(self, controlador, ts):

        if self.expresion != None:

            valor_Exp = self.expresion.ObtenerValor(controlador, ts)
            return valor_Exp


