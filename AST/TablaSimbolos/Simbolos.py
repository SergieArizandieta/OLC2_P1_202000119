class Simbolos() :

    def __init__(self,id,valor,tipo,mut):
        self.linea = 0
        self.columna = 0
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mut = mut

    def Asignar_valor(self, valor):
        self.valor = valor