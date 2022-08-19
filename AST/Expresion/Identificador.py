from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo as t


class Identificador(Expresion):

    def __init__(self, id):
        self.id = id

    def ObtenerValor(self, controlador, ts):
        existe_id:Simbolos = ts.ObtenerSimbolo(self.id)

        if  existe_id is not None:
            print("!!=== tratando de recuperar dato : ", existe_id, " id buscado: ", self.id)
            print("Tabla donde se busca el valor : ", ts.name)
            return existe_id.valor
        else:
            return "No se encontro valor"


    def ObtenerTipo(self, controlador, ts):
        existe_id:Simbolos = ts.ObtenerSimbolo(self.id)

        if existe_id is not None:
            return existe_id.tipo
        else:
            return None
