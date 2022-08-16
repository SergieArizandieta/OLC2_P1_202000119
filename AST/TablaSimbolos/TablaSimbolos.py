from AST.TablaSimbolos.Simbolos import Simbolos


class TablaDeSimbolos():

    def __init__(self, padre, name):
        self.padre = padre
        self.name = name
        self.tabla = {}

        # Solo para reportes
        self.siguiente = None
        if padre != None:
            padre.siguiente = self

    def Agregar_Simbolo(self, id, simbolo: Simbolos):
        print("Agregando: ", id, " con simbolo: ", simbolo)
        if not self.Existe_id(id):
            self.tabla[id] = simbolo
        else:
            print("Ya existe la variable")

    def Existe_id(self, id):
        ts = self
        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:
                return True

            ts = ts.padre

        return False

    def Obtener_Val_Simbolo(self, id):

        ts = self

        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:
                return existe.valor

            ts = ts.padre

        return None

    def Obtener_Tipo_Simbolo(self, id):
        ts = self

        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:
                return existe.tipo

            ts = ts.padre

        return None

    def Actualizar_Simbolo(self,id, tipo,valor):
        ts = self
        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:

                if existe.tipo == tipo and existe.mut:
                    ts.tabla[id].valor = valor
                    break


            ts = ts.padre
