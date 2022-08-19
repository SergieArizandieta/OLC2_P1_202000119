from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.Instruccion.Match.BloqueMatch import BloqueMatch


class Match(Intruccion,Expresion):
    def __init__(self, expresion, matches):
        self.expresion = expresion
        self.matches = matches

    def ObtenerValor(self, controlador, ts):

        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        print("== -Match- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:

                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return self.EjecicionExpresiones_valor(match.instrucciones, controlador, ts)
                else:

                    return self.EjecicionExpresiones_valor(match.instrucciones, controlador, ts)

    def ObtenerTipo(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        for match in self.matches:
            for validation in match.matches:
                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return self.EjecicionExpresiones_tipo(match.instrucciones, controlador, ts)
                else:
                    return self.EjecicionExpresiones_tipo(match.instrucciones, controlador, ts)


    def EjecicionExpresiones_tipo(self,Expresiones_match,controlador, ts):
        retorno = None
        for intruccion in Expresiones_match:
            retorno = intruccion.ObtenerTipo(controlador, ts)
        return retorno

    def EjecicionExpresiones_valor(self,Expresiones_match,controlador, ts):
        retorno = None
        for intruccion in Expresiones_match:
            retorno = intruccion.ObtenerValor(controlador, ts)
        return retorno

    def EjecutarInstruccion(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        print("== -Match- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:

                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return self.EjecucionInstrucciones(match.instrucciones,controlador, ts)
                else:
                    print("Se llego al brazo de salida ")
                    return self.EjecucionInstrucciones(match.instrucciones, controlador, ts)

        print("Algo paso ")

    def EjecucionInstrucciones(self,instrucciones_match,controlador, ts):
        retorno = None
        print("expresiones ejecutadas")
        for intruccion in instrucciones_match:
            print(intruccion)
            retorno = intruccion.EjecutarInstruccion(controlador, ts)
        print("Lo que se devolvio: ", retorno)
        return retorno


