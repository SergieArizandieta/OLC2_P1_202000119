from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class While(Intruccion):
    def __init__(self,expresion,lista_instrucciones):
        self.expresion = expresion
        self.lista_instrucciones = lista_instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)


        if tipo_Exp == tipo.BOOLEANO:
            if valor_Exp:

                while self.expresion.ObtenerValor(controlador, ts):
                    ts_local = TablaDeSimbolos(ts, "While" + str(id(self)))
                    for instruccion in self.lista_instrucciones:
                        retorno = instruccion.EjecutarInstruccion(controlador,ts_local)
