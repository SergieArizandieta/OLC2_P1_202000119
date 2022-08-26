from AST.TablaSimbolos.Simbolos import Simbolos

class InstanciaArreglo(Simbolos):

    def __init__(self,tipo, dimensiones, valores:[]):
        super().__init__()
        super().iniciarSimboloArreglo(tipo,dimensiones, valores)

    def ObtenerValor(self, listaDimensiones, index, valores):

        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                return None

            else:

                subArreglo = valores[indiceDimension]
                return self.ObtenerValor(listaDimensiones, index+1, subArreglo)

        else:
            if indiceDimension > (tamanoDimension-1):
                return None
            else:
                return valores[indiceDimension]

