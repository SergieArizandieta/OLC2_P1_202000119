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

        print("== -Match Expresiones- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:
                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return match.ObtenerValor(controlador, ts)
                else:
                    return match.ObtenerValor(controlador, ts)

    def ObtenerTipo(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        for match in self.matches:
            for validation in match.matches:
                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return match.ObtenerTipo(controlador, ts)
                else:
                    return match.ObtenerTipo(controlador, ts)

    def EjecutarInstruccion(self, controlador, ts):
        valor_Exp = self.expresion.ObtenerValor(controlador, ts)
        tipo_Exp = self.expresion.ObtenerTipo(controlador, ts)

        print("== -Match Instrucciones- ==")
        print("varible: ", self.expresion)
        print(" valor: ", valor_Exp, " tipo: ", tipo_Exp)

        for match in self.matches:
            print("match: ", match)

            for validation in match.matches:
                if validation != '_':
                    valor_v = validation.ObtenerValor(controlador, ts)
                    tipo_v = validation.ObtenerTipo(controlador, ts)
                    if valor_Exp == valor_v and tipo_Exp == tipo_v:
                        return match.EjecutarInstruccion(controlador, ts)
                else:
                    return match.EjecutarInstruccion(controlador, ts)






