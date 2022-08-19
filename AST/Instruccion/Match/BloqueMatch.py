from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class BloqueMatch(Intruccion,Expresion):


    def __init__(self, matches, instrucciones):
        self.matches = matches
        self.instrucciones = instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        ts_local = TablaDeSimbolos(ts, "Matc" + str(id(self.matches)))
        retorno = None
        print("== Ejcutando intruccion ==")
        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.EjecutarInstruccion(controlador, ts_local)
            except: pass
        return retorno

    def ObtenerValor(self, controlador, ts):
        retorno = None
        print("== Ejcutando Obtener valor ==")
        for intruccion in self.instrucciones:
            try:
                retorno = intruccion.ObtenerValor(controlador, ts)
            except:
                intruccion.EjecutarInstruccion(controlador, ts)
        return retorno

    def ObtenerTipo(self, controlador, ts):
        retorno = None
        for intruccion in self.instrucciones:
            retorno = intruccion.ObtenerTipo(controlador, ts)
        return retorno