
from AST.Abstracto.Expresion import Expresion
from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import RetornoType
class AccesoStruct(Intruccion,Expresion):

    def __init__(self,id,expresiones,exp):
        self.identificador = id
        self.expresiones =expresiones
        self.exp=exp
        self.ts = None

    def EjecutarInstruccion(self, controlador, ts):
        print(self.identificador)
        print(self.expresiones)
        print(self.exp)

        struck_ccr = ts.ObtenerSimbolo(self.identificador.id)
        struck_dic = struck_ccr.valor.diccionario

        if len(self.expresiones) == 1:
            id = self.expresiones[0].id
            valor_acc = struck_dic.get(id)
            if valor_acc is not  None:
                struck_dic[id].valor = self.exp.valor

        print("Se asigno a struct")

    def ObtenerValor(self, controlador, ts):
        print(self.identificador)
        print(self.expresiones)
        print(self.exp)
        self.ts = ts
        return self.fn_obtner_valor(self.identificador,self.expresiones)


    def fn_obtner_valor(self,identificador,expresiones):

        struck_ccr =  self.ts.ObtenerSimbolo(identificador.id)
        struck_dic = struck_ccr.valor.diccionario

        while(True):
            if not isinstance(expresiones[0], AccesoStruct):
                if len(expresiones) == 1:
                    id = expresiones[0].id
                    valor_acc = struck_dic.get(id)
                    if valor_acc is not None:
                        return RetornoType(valor_acc.valor, valor_acc.tipo)
                else:
                    id = expresiones[0].id
                    valor_acc = struck_dic.get(id)
                    if valor_acc is not None:

                        struck_dic = valor_acc.valor.diccionario
                        expresiones.pop(0)

            else:

                expr = expresiones[0].identificador
                expresiones = expresiones[0].expresiones
                if not isinstance(expr, AccesoStruct):
                    if len(expresiones) == 1:
                        id = expr.id
                        valor_acc = struck_dic.get(id)
                        struck_dic = valor_acc.valor.diccionario



