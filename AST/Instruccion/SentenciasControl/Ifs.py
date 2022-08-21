from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo,RetornoType
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class Ifs(Intruccion,Expresion):

    def __init__(self,condicion,bloque_if,bloque_else,bloques_elif):
        self.condicion=condicion
        self.bloque_if = bloque_if
        self.bloque_else = bloque_else
        self.bloques_elif = bloques_elif

    def EjecutarInstruccion(self, controlador, ts):
        return_exp: RetornoType = self.condicion.ObtenerValor(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO :

            if valor_Exp:

                ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
                return self.Recorrer_ins(controlador, ts_local, self.bloque_if)

            else:

                if self.bloques_elif is not None:

                    for list_if in self.bloques_elif:
                        return_if: RetornoType = list_if.condicion.ObtenerValor(controlador, ts)
                        valor_if = return_if.valor
                        tipo_if = return_if.tipo

                        if tipo_if == tipo.BOOLEANO :
                            if valor_if:
                                return self.Recorrer_ins(controlador, ts, self.bloques_elif)

                if self.bloque_else is not None:
                    ts_local = TablaDeSimbolos(ts, "Else" + str(id(self)))
                    return self.Recorrer_ins(controlador, ts_local,self.bloque_else)

    def Recorrer_ins(self,controlador,ts,lista):
        retorno = None
        for instruccion in lista:
            try:
                retorno = instruccion.EjecutarInstruccion(controlador, ts)
            except:
                pass

        return retorno

    def ObtenerValor(self, controlador, ts):
        return_exp: RetornoType = self.condicion.ObtenerValor(controlador, ts)
        valor_Exp = return_exp.valor
        tipo_Exp = return_exp.tipo

        if tipo_Exp == tipo.BOOLEANO:

            if valor_Exp:

                ts_local = TablaDeSimbolos(ts, "If" + str(id(self)))
                return self.Recorrer_exp_val(controlador, ts_local, self.bloque_if)

            else:

                if self.bloques_elif is not None:

                    for list_if in self.bloques_elif:
                        return_if: RetornoType = list_if.condicion.ObtenerValor(controlador, ts)
                        valor_if = return_if.valor
                        tipo_if = return_if.tipo

                        if tipo_if == tipo.BOOLEANO:
                            if valor_if:
                                return self.Recorrer_exp_val(controlador, ts, self.bloques_elif)

                if self.bloque_else is not None:
                    ts_local = TablaDeSimbolos(ts, "Else" + str(id(self)))
                    return self.Recorrer_exp_val(controlador, ts_local, self.bloque_else)

    def Recorrer_exp_val(self,controlador,ts,lista):
        retorno = None
        for instruccion in lista:
            try:
                retorno = instruccion.ObtenerValor(controlador, ts)
            except:
                instruccion.EjecutarInstruccion(controlador, ts)

        return retorno


