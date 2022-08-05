from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo


class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):
        valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
        valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

        tipo_exp1 = type(self.exp1.ObtenerValor(controlador, ts))
        tipo_exp2 = type(self.exp2.ObtenerValor(controlador, ts))

        if self.operador == operador.SUMA:
            if tipo_exp1 == tipo_exp2:
                return valor_exp1 + valor_exp2
            else:
                return "Error no son iguales"

    def ObtenerTipo(self, controlador, ts):
        valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
        valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

        if isinstance(valor_exp1, int):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return tipo.ENTERO

        elif isinstance(valor_exp1, float):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return tipo.DECIMAL

    def validacion_tipos(self,valor_exp1, valor_exp2):
        if type(valor_exp1) == type(valor_exp2):
            return True

        return False
