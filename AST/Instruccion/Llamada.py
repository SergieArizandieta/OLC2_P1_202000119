from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos, Simbolos
from AST.Instruccion import Funcion


class Llamada(Intruccion, Expresion):

    def __init__(self, identificador, parametos):
        self.identificador = identificador
        self.parametos = parametos

    def EjecutarInstruccion(self, controlador, ts: TablaDeSimbolos):
        print("La funcion se esta ejecuntado en la tabla: ", ts.name)
        if ts.Existe_id(self.identificador):
            ts_local = TablaDeSimbolos(ts, ts.name)
            simbolo_funcion: Funcion = ts.ObtenerSimbolo(self.identificador)

            if self.validar_parametros(self.parametos, simbolo_funcion.parametros, controlador, ts, ts_local):

                retorno = simbolo_funcion.EjecutarInstruccion(controlador, ts_local)

                if retorno is not None:
                    return retorno

    def ObtenerValor(self, controlador, ts):
        simbolo_funcion = ts.Obtener_Tipo_Simbolo(self.identificador)
        return simbolo_funcion.tipo

    def ObtenerTipo(self, controlador, ts):
        if ts.Existe_id(self.identificador):
            ts_local = TablaDeSimbolos(ts, ts.name)
            simbolo_funcion = ts.Obtener_Tipo_Simbolo(self.identificador)

            if self.validar_parametros(self.parametos, simbolo_funcion.parametos, controlador, ts, ts_local):
                retorno = simbolo_funcion.EjecutarInstruccion(controlador, ts_local)

                if retorno is not None:
                    return retorno

    def validar_parametros(self, parametros_llamada, parametros_funcion, controlador, ts, ts_loca):
        if len(parametros_llamada) == len(parametros_funcion):




            for i in range(0, len(parametros_llamada)):
                aux = parametros_funcion[i]
                aux_id = aux.identificador.id
                aux_tipo = aux.tipo
                print("Parametro de la funcion")
                print("aux id: ",aux_id)
                print("aux tipo: ", aux_tipo)

                aux_exp = parametros_llamada[i]
                aux_exp_valor = aux_exp.ObtenerValor(controlador, ts)
                aux_exp_tipo = aux_exp.ObtenerTipo(controlador, ts)

                print("Parametro de la llamada")
                print("aux valor: ", aux_exp_valor)
                print("aux tipo: ", aux_exp_tipo)

                if aux_tipo == aux_exp_tipo:
                    simbolo = Simbolos()
                    simbolo.SimboloPremitivo(aux_id, aux_exp_valor, aux_id, False)
                    ts_loca.Agregar_Simbolo(aux_id, simbolo)
                else:
                    return False

            return True
        else:
            return False
