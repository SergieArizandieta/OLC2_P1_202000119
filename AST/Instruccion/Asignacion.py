from AST.Abstracto.Instruccion import Intruccion


class Asignacion(Intruccion):
    def __init__(self,identificador,valor):
        self.identificador=identificador
        self.valor = valor

    def EjecutarInstruccion(self, controlador, ts):
        if(ts.Existe_id(self.identificador)):

            ValorExpresion = self.valor.ObtenerValor(controlador, ts)
            TipoExpresion = self.valor.ObtenerTipo(controlador, ts)

            ts.Actualizar_Simbolo(self.identificador,TipoExpresion,ValorExpresion)
