from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo as t


class Identificador(Expresion):

    def __init__(self, id):
        self.id = id

    def ObtenerValor(self, controlador, ts):
        existe_id:Simbolos = ts.ObtenerSimbolo(self.id)
        print("!!=== tratando de recuperar dato")
        return existe_id.valor

    def ObtenerTipo(self, controlador, ts):
        existe_id:Simbolos = ts.ObtenerSimbolo(self.id)
        return existe_id.tipo
