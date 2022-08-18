from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo


class Logica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):

        valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
        tipo_exp1 = self.exp1.ObtenerTipo(controlador, ts)

        if not self.expU:

            valor_exp2 = self.exp2.ObtenerValor(controlador, ts)
            tipo_exp2 = self.exp2.ObtenerTipo(controlador, ts)

            if self.operador == operador.AND:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return valor_exp1 and valor_exp2
            elif self.operador == operador.OR:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return valor_exp1 or valor_exp2
        else:
            if self.operador == operador.NOT:
                if tipo_exp1 == tipo.BOOLEANO:
                    return not valor_exp1

    def ObtenerTipo(self, controlador, ts):

        tipo_exp1 = self.exp1.ObtenerTipo(controlador, ts)

        if not self.expU:

            tipo_exp2 = self.exp2.ObtenerTipo(controlador, ts)

            if self.operador == operador.AND:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return tipo.BOOLEANO
            elif self.operador == operador.OR:
                if tipo_exp1 == tipo_exp2 and tipo_exp1 == tipo.BOOLEANO:
                    return tipo.BOOLEANO
        else:
            if self.operador == operador.NOT:
                if tipo_exp1 == tipo.BOOLEANO:
                    return tipo.BOOLEANO
