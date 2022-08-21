from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import Operacion, operador
from AST.TablaSimbolos.Tipos import tipo as t
from AST.TablaSimbolos.Tipos import RetornoType

class Relacional(Operacion, Expresion):

    def __init__(self, exp1, signo, exp2, expU):
        super().__init__(exp1, signo, exp2, expU)

    def ObtenerValor(self, controlador, ts):
        return_exp1:RetornoType = self.exp1.ObtenerValor(controlador, ts)
        return_exp2:RetornoType = self.exp2.ObtenerValor(controlador, ts)

        valor_exp1 = return_exp1.valor
        valor_exp2 = return_exp2.valor

        tipo_exp1 = return_exp1.tipo
        tipo_exp2 = return_exp2.tipo

        if self.operador == operador.MAYORIGUAL:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 >= valor_exp2,t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 >= valor_exp2,t.BOOLEANO)

            else:
                return "No son el mismo formato"

        elif self.operador == operador.MAYORQUE:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 > valor_exp2, t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 > valor_exp2, t.BOOLEANO)

            else:
                return "No son el mismo formato"

        elif self.operador == operador.MENORIGUAL:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 <= valor_exp2, t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 <= valor_exp2, t.BOOLEANO)

            else:
                return "No son el mismo formato"

        elif self.operador == operador.MENORQUE:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 < valor_exp2, t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 < valor_exp2, t.BOOLEANO)

            else:
                return "No son el mismo formato"

        elif self.operador == operador.IGUALIGUAL:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 == valor_exp2, t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 == valor_exp2, t.BOOLEANO)

            else:
                return "No son el mismo formato"

        elif self.operador == operador.DIFERENCIA:

            if isinstance(valor_exp1, int) and isinstance(valor_exp2, int):
                return RetornoType(valor_exp1 != valor_exp2, t.BOOLEANO)

            elif isinstance(valor_exp1, float) and isinstance(valor_exp2, float):
                return RetornoType(valor_exp1 != valor_exp2, t.BOOLEANO)

            else:
                return "No son el mismo formato"

