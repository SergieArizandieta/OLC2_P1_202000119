from datetime import datetime

class TablaErrores():

    def __init__(self):

        self.contador = 0
        self.lista = []

    def agregar_error(self,descripcion,tipo,ambito,linea,columna):
        self.contador += 1

        if tipo == 0:
            tipo = "Lexico"
        elif tipo == 1:
            tipo = "Sintactico"
        elif tipo == 2:
            tipo = "Semantico"

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        error = Error_Obj(self.contador,descripcion,tipo,ambito,linea,columna,dt_string)
        self.lista.append(error)

    def print_errores(self):
        print("====COMENZANDO LITA ERR =======")
        for x in self.lista:
            print("no: ",x.no," descripcion: ",x.descripcion," tipo: ",x.tipo," ambito: ",x.ambito," L: ",x.linea," C: ",x.columna," T: ",x.time)


class Error_Obj():
    def __init__(self,no,descripcion,tipo,ambito,linea,columna,time):
        self.no =no
        self.descripcion = descripcion
        self.tipo =tipo
        self.ambito = ambito
        self.linea = linea
        self.columna = columna
        self.time = time




