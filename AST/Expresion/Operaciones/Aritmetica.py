from AST.Abstracto.Expresion import Expresion
from AST.Expresion.Operaciones.Operacion import operador, Operacion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from Analizador.Gramatica import *

class Aritmetica(Operacion, Expresion):
    def __init__(self, exp1, signo, exp2, expU=False,linea=0,columna=0):
        super().__init__(exp1, signo, exp2, expU,linea,columna)

    def ObtenerValor(self, controlador, ts):

        return_exp1: RetornoType = self.exp1.ObtenerValor(controlador, ts)
        valor_exp1 = return_exp1.valor
        tipo_exp1 = return_exp1.tipo

        if not self.expU:

            return_exp2: RetornoType = self.exp2.ObtenerValor(controlador, ts)
            valor_exp2 = return_exp2.valor
            tipo_exp2 = return_exp2.tipo

            if self.operador == operador.SUMA:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 + valor_exp2),tipo.ENTERO)

                elif tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 + valor_exp2), tipo.DECIMAL)

                elif (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO) and (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO):
                    return RetornoType(int(valor_exp1 + valor_exp2), tipo.USIZE)

                elif tipo_exp1 == tipo.STRING and tipo_exp2 == tipo.DIRSTRING:
                    return RetornoType(str(valor_exp1 + valor_exp2),tipo.STRING)

                elif tipo_exp1 == tipo.USIZE and tipo_exp2 == tipo.USIZE:
                    return RetornoType(int(valor_exp1 + valor_exp2),tipo.USIZE)

                else:
                    E_list.agregar_error("No se puede sumar datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2, ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.RESTA:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 - valor_exp2), tipo.ENTERO)

                elif tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 - valor_exp2), tipo.DECIMAL)

                elif (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO) and (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO):
                    return RetornoType(int(valor_exp1 - valor_exp2), tipo.USIZE)

                elif tipo_exp1 == tipo.USIZE and tipo_exp2 == tipo.USIZE:
                    return RetornoType(int(valor_exp1 - valor_exp2),tipo.USIZE)

                else:
                    E_list.agregar_error("No se puede resta datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.MULTIPLICACION:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 * valor_exp2), tipo.ENTERO)

                elif tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 * valor_exp2), tipo.DECIMAL)

                elif (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO) and (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO):
                    return RetornoType(int(valor_exp1 * valor_exp2), tipo.USIZE)

                elif tipo_exp1 == tipo.USIZE and tipo_exp2 == tipo.USIZE:
                    return RetornoType(int(valor_exp1 * valor_exp2),tipo.USIZE)

                else:
                    E_list.agregar_error("No se puede multiplicar datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,
                                         ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.DIVISION:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 / valor_exp2), tipo.ENTERO)

                elif tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 / valor_exp2), tipo.DECIMAL)

                elif (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO) and (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO):
                    return RetornoType(int(valor_exp1 / valor_exp2), tipo.USIZE)

                elif tipo_exp1 == tipo.USIZE and tipo_exp2 == tipo.USIZE:
                    return RetornoType(int(valor_exp1 / valor_exp2),tipo.USIZE)

                else:
                    E_list.agregar_error("No se puede dividir datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,
                                         ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.MOD:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 % valor_exp2), tipo.ENTERO)

                elif tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 % valor_exp2), tipo.DECIMAL)

                elif (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO) and (tipo_exp2 == tipo.USIZE or tipo_exp2 == tipo.ENTERO):
                    return RetornoType(int(valor_exp1 % valor_exp2), tipo.USIZE)

                elif tipo_exp1 == tipo.USIZE and tipo_exp2 == tipo.USIZE:
                    return RetornoType(int(valor_exp1 % valor_exp2),tipo.USIZE)

                else:
                    E_list.agregar_error("No se puede realizar modulo entre datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,
                                         ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.POT:

                if tipo_exp1 == tipo.ENTERO and  tipo_exp2 == tipo.ENTERO:
                    return RetornoType(int(valor_exp1 ** valor_exp2), tipo.ENTERO)

                else:
                    E_list.agregar_error(
                        "No se puede realizar potencia entre datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,
                        ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

            elif self.operador == operador.POTF:

                if tipo_exp1 == tipo.DECIMAL and tipo_exp2 == tipo.DECIMAL:
                    return RetornoType(float(valor_exp1 ** valor_exp2), tipo.DECIMAL)

                else:
                    E_list.agregar_error(
                        "No se puede realizar potencia F entre datos " + str(tipo_exp1) + " y " + str(tipo_exp2), 2,
                        ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No son el mismo formato"

        else:

            if self.operador == operador.RESTA:

                if isinstance(valor_exp1, int):
                    return RetornoType(int(valor_exp1 * -1), tipo.ENTERO)

                elif isinstance(valor_exp1, float):
                    return RetornoType(float(valor_exp1 * -1), tipo.DECIMAL)

                else:
                    E_list.agregar_error("No se puede realizar unario de dato " + str(tipo_exp1) , 2,ts.name, self.linea, self.columna)
                    E_list.print_errores()
                    return "No es digito"

