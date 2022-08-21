from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos
from AST.TablaSimbolos.Tipos import RetornoType

class Funcion(Intruccion):

    def __init__(self, identificador, tipo, parametros, instrucciones):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        print("Intrucciones de : ", self.identificador)

        for instruccion in self.instrucciones:

            retorno = instruccion.EjecutarInstruccion(controlador, ts)

            if retorno is not None:
                if isinstance(retorno,RetornoType):
                    if retorno.tipo == self.tipo:
                        return retorno
                    else:
                        return RetornoType()


    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
