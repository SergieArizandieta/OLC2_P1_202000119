from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion,operador
from AST.TablaSimbolos.Tipos import tipo as t


class Relacional(Operacion, Expresion ):

    def __init__(self, exp1, signo, exp2, expU):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):
        valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
        valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

        if self.operador == operador.MAYORIGUAL:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return valor_exp1 >= valor_exp2
            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return valor_exp1 >= valor_exp2
            else:
                return "No son el mismo formato"

        elif self.operador == operador.MAYORQUE:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return valor_exp1 > valor_exp2
            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return valor_exp1 > valor_exp2
            else:
                return "No son el mismo formato"

        elif self.operador == operador.MENORIGUAL:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return valor_exp1 <= valor_exp2
            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return valor_exp1 <= valor_exp2
            else:
                return "No son el mismo formato"

        elif self.operador == operador.MENORQUE:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return valor_exp1 < valor_exp2
            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return valor_exp1 < valor_exp2
            else:
                return "No son el mismo formato"



    def ObtenerTipo(self, controlador, ts):
        valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
        valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

        tipo_exp1 = self.exp1.ObtenerTipo(controlador, ts)
        tipo_exp2 = self.exp2.ObtenerTipo(controlador, ts)

        if tipo_exp1 == t.ERROR or tipo_exp2 == t.ERROR:
            return t.ERROR

        if isinstance(valor_exp1, int):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return t.BOOLEANO

        elif isinstance(valor_exp1, float):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return t.BOOLEANO

        elif isinstance(valor_exp1, str):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return t.BOOLEANO

        elif isinstance(valor_exp1, bool):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return t.BOOLEANO

        elif isinstance(valor_exp1, bool):
            if self.validacion_tipos(valor_exp1, valor_exp2):
                return t.BOOLEANO

        elif tipo_exp1 == t.CARACTER:
            if tipo_exp1 == tipo_exp2:
                return t.BOOLEANO

    def validacion_tipos(self, valor_exp1, valor_exp2):
        if type(valor_exp1) == type(valor_exp2):
            return True

        return False
