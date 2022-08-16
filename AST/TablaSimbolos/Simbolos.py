class Simbolos() :

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.id = ""
        self.valor = 0
        self.tipo =  None
        self.mut = False

        self.parametros= []
        self.instrucciones = []

    def SimboloPremitivo(self,id,valor,tipo,mut):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mut = mut

    def SimboloFuncion(self,id,parametros,instrucciones,tipo):
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones

    def Asignar_valor(self, valor):
        self.valor = valor