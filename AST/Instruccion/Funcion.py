from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos,Simbolos
from AST.Instruccion.Llamada import Llamada

class Funcion(Intruccion):

    def __init__(self, identificador, tipo, parametros, instrucciones):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        print("Intrucciones de : ", self.identificador)

        for instruccion in self.instrucciones:
            if isinstance(instruccion,Llamada):
               # retorno = instruccion.EjecutarInstruccion(controlador, ts.padre)
               retorno = instruccion.EjecutarInstruccion(controlador, ts)
            else:
                print("Instuccion: ",instruccion)
                retorno = instruccion.EjecutarInstruccion(controlador, ts)

            if retorno is not None:
                return retorno

        return None


    def agregarFuncion(self, ts: TablaDeSimbolos):
        print("================== Se guardo funcion ================ ", self.identificador)
        if not ts.Existe_id(self.identificador):
            ts.Agregar_Simbolo(self.identificador, self)

        # print("Se supone que se guardo")
        # ts.Print_Table()
