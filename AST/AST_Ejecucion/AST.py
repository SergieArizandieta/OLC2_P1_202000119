from ..Abstracto.Instruccion import Intruccion


class AST(Intruccion):
    def __init__(self, Lista_instrucciones):
        self.Lista_instrucciones = Lista_instrucciones

    def EjecutarInstruccion(self, controlador, ts):
        print("Iniciando ejecucion de instrucciones")
        #    print("Iniciando ejecucion de instrucciones")
        try:
            for intruccion in self.Lista_instrucciones:
                print("Ejecutando: ", intruccion)
                intruccion.EjecutarInstruccion(controlador, ts)

            print("======Termino=======")
            print(controlador.consola)

        except:
            print("Err")
