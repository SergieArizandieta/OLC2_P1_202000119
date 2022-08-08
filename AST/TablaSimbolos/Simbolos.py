class Simbolos() :

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.id = ""
        self.valor = None
        self.tipo = None
        self.mut = False

    def iniciarSimboloPrimitivo(self, id, valor, tipo, mut=False):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mut = mut