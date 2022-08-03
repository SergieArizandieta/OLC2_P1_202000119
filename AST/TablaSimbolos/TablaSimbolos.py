class TablaDeSimbolos():

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable ', simbolo.id, ' no definida.')
        else:
            self.simbolos[simbolo.id] = simbolo