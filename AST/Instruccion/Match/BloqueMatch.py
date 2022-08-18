from AST.Abstracto.Instruccion import Intruccion

class BloqueMatch(Intruccion):

    def __init__(self,matches,instrucciones):
        self.matches=matches
        self.instrucciones=instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        return self