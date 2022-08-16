from ..Abstracto.Instruccion import Intruccion
from AST.Instruccion import Funcion

class AST(Intruccion):
    def __init__(self, Lista_instrucciones):
        self.Lista_instrucciones = Lista_instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        #print("Iniciando ejecucion de instrucciones")
            print("Iniciando ejecucion de instrucciones")
        #try:


            '''for intruccion in self.Lista_instrucciones:
                print("======inicio ======= ",intruccion)
                if isinstance(intruccion,Funcion.Funcion):
                    funcion = intruccion
                    funcion.agregarFuncion(ts)'''

            for intruccion in self.Lista_instrucciones:
                if isinstance(intruccion,Funcion.Funcion):
                    if intruccion.identificador == "main":
                        intruccion.EjecutarInstruccion(controlador, ts)


            print("======Termino=======")
            print(controlador.consola)

        #except:
            #print("Err")
