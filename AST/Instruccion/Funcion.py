from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos


class Funcion(Intruccion):

    def __init__(self, identificador, tipo, parametros, instrucciones):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        print("================== Ejecucion main ================")
        ts_local = TablaDeSimbolos(ts, self.identificador)

        for instruccion in self.instrucciones:
            retorno = instruccion.EjecutarInstruccion(controlador, ts_local)
            if retorno is not None:
                return retorno

        return None

    def agregarFuncion(self,ts):
        print("================== Se guardo funcion ================")
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador,self)
