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
        print("Agregando: ",id," con simbolo: ",simbolo)
        if self.Obtener_Val_Simbolo(id) is None:
            self.tabla[id] = simbolo
        else:
            print("Ya existe")

    def Obtener_Val_Simbolo(self, id):

        ts = self

        while ts != None:
            existe = ts.tabla.get(id)

            if existe != None:
                return existe.valor

            ts = ts.padre

        return None

    def Obtener_Tipo_Simbolo(self, id):
        ts = self

        while ts != None:
            existe = ts.tabla.get(id)

            if existe != None:
                return existe.tipo

            ts = ts.padre

        return None

    def Actualizar_Simbolo(self, simbolo: Simbolos):

        ts = self

        while ts is not None:
            existe = ts.tabla.get(id)

            if existe is not None:

                if existe.tipo == simbolo.tipo and existe.mut:
                    ts.tabla[id] = simbolo

            ts = ts.padre
