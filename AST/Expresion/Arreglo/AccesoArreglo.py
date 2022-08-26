from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import  RetornoType,tipo
from AST.TablaSimbolos.InstanciaArreglo import InstanciaArreglo
from AST.TablaSimbolos.TablaSimbolos import TablaDeSimbolos

class AccesoArreglo(Expresion):

    def __init__(self, idArreglo, listaExpresiones):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones

    def ObtenerValor(self, controlador,ts:TablaDeSimbolos) -> RetornoType:
        print("Llego a accesoL ",self.idArreglo, " lista dimensiones: ",self.listaExpresiones)
        ts.Print_Table()
        if ts.Existe_id(self.idArreglo) is not True:
            return RetornoType()

        arreglo = ts.ObtenerSimbolo(self.idArreglo)
        if isinstance(arreglo, InstanciaArreglo) is not True:
            return RetornoType()

        if len(self.listaExpresiones) != len(arreglo.dimensiones):
            return RetornoType()

        dimensiones = self.compilarDimensiones(controlador,ts)

        valor = arreglo.ObtenerValor(dimensiones,0,arreglo.valores)
        return RetornoType(valor,arreglo.tipo)


    def compilarDimensiones(self,controlador, ts ):
        listaDimensiones = []

        for dim in self.listaExpresiones:
            dimVal = dim.ObtenerValor(controlador,ts)
            # operador ternario      hacer_si_true if condicion else hacer_si_false
            if dimVal.tipo != tipo.ENTERO:
                return
            else:
                listaDimensiones.append(dimVal.valor)

        return listaDimensiones
