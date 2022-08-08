from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo


class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):

        if not self.expU:
            valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
            valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

            if self.operador == operador.SUMA:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 + valor_exp2)
                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 + valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.RESTA:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 - valor_exp2)
                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 - valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.MULTIPLICACION:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 * valor_exp2)
                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 * valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.DIVISION:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 / valor_exp2)
                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 / valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.MOD:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 % valor_exp2)
                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 % valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.POT:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return int(valor_exp1 ** valor_exp2)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.POTF:

                if isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return float(valor_exp1 ** valor_exp2)
                else:
                    return "No son el mismo formato"

        else:

            if self.operador == operador.RESTA:
                valor_exp1 = self.exp1.ObtenerValor(controlador, ts)

                print("!!!===UNARIOOOOOOOOOOOOOOOOOOOOOOO")
                if isinstance(valor_exp1, int):
                    return int(valor_exp1 * -1)
                elif isinstance(valor_exp1, float):
                    return float(valor_exp1 * -1)
                else:
                    return "No es digito"

    def ObtenerTipo(self, controlador, ts):

        if not self.expU:
            valor_exp1 = self.exp1.ObtenerValor(controlador, ts)
            valor_exp2 = self.exp2.ObtenerValor(controlador, ts)

            if isinstance(valor_exp1, int):
                if self.validacion_tipos(valor_exp1, valor_exp2):
                    return tipo.ENTERO

            elif isinstance(valor_exp1, float):
                if self.validacion_tipos(valor_exp1, valor_exp2):
                    return tipo.DECIMAL

            elif isinstance(valor_exp1, str):
                if self.validacion_tipos(valor_exp1, valor_exp2):
                    return tipo.CADENA

        else:

            valor_exp1 = self.exp1.ObtenerValor(controlador, ts)

            if isinstance(valor_exp1, int):
                    return tipo.ENTERO

            elif isinstance(valor_exp1, float):
                    return tipo.DECIMAL

    def validacion_tipos(self, valor_exp1, valor_exp2):
        if type(valor_exp1) == type(valor_exp2):
            return True

        return False
