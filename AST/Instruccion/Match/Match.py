from AST.Abstracto.Instruccion import Intruccion
from AST.Instruccion.Match.BloqueMatch import BloqueMatch


class Match(Intruccion):

    def __init__(self, expresion, matches):
        self.expresion = expresion
        self.matches = matches

    def EjecutarInstruccion(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        print("== Match ==")
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


    def EjecucionInstrucciones(self,instrucciones_match,controlador, ts):
        retorno = None
        for intruccion in instrucciones_match:
            retorno = intruccion.EjecutarInstruccion(controlador, ts)

        return retorno


