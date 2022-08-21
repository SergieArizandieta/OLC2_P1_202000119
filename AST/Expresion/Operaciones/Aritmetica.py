from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo,RetornoType


class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):

        return_exp1: RetornoType = self.exp1.ObtenerValor(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo

        if not self.expU:

            return_exp2: RetornoType = self.exp2.ObtenerValor(controlador, ts)
            valor_exp2 = return_exp2.valor
            tipo_exp2 = return_exp2.tipo

            if self.operador == operador.SUMA:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 + valor_exp2),tipo.ENTERO)

                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 + valor_exp2), tipo.DECIMAL)

                elif tipo_exp1 == tipo.STRING and tipo_exp2 == tipo.DIRSTRING:
                    return RetornoType(str(valor_exp1 + valor_exp2),tipo.STRING)

                else:
                    return "No son el mismo formato"

            elif self.operador == operador.RESTA:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 - valor_exp2), tipo.ENTERO)

                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 - valor_exp2), tipo.DECIMAL)
                else:
                    return "No son el mismo formato"

            elif self.operador == operador.MULTIPLICACION:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 * valor_exp2), tipo.ENTERO)

                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 * valor_exp2), tipo.DECIMAL)

                else:
                    return "No son el mismo formato"

            elif self.operador == operador.DIVISION:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 / valor_exp2), tipo.ENTERO)

                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 / valor_exp2), tipo.DECIMAL)

                else:
                    return "No son el mismo formato"

            elif self.operador == operador.MOD:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 % valor_exp2), tipo.ENTERO)

                elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 % valor_exp2), tipo.DECIMAL)

                else:
                    return "No son el mismo formato"

            elif self.operador == operador.POT:

                if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                    return RetornoType(int(valor_exp1 ** valor_exp2), tipo.ENTERO)

                else:
                    return "No son el mismo formato"

            elif self.operador == operador.POTF:

                if isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                    return RetornoType(float(valor_exp1 ** valor_exp2), tipo.DECIMAL)

                else:
                    return "No son el mismo formato"

        else:

            if self.operador == operador.RESTA:
                valor_exp1 = self.exp1.ObtenerValor(controlador, ts)

                if isinstance(valor_exp1, int):
                    return RetornoType(int(valor_exp1 * -1), tipo.ENTERO)

                elif isinstance(valor_exp1, float):
                    return RetornoType(float(valor_exp1 * -1), tipo.DECIMAL)

                else:
                    return "No es digito"

