from AST.Abstracto.Expresion import Expresion
from AST.TablaSimbolos.Tipos import tipo as t


class Identificador(Expresion):

    def __init__(self, id):
        self.id = id

    def ObtenerValor(self, controlador, ts):
        existe_id = ts.Obtener_Val_Simbolo(self.id)
        print("!!=== tratando de recuperar dato")
        return existe_id

    def ObtenerTipo(self, controlador, ts):
        existe_id = ts.Obtener_Tipo_Simbolo(self.id)
        return existe_id
