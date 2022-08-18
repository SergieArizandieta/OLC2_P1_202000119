from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t

class Imprimir(Intruccion):

    def __init__(self,  expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista =lista

    def EjecutarInstruccion(self, controlador, ts):


        global valor, tipo
        if len(self.lista) > 0:
            texto_salida = ""


            if  self.expresion.count("{}") > 0:
                formato_nomal = self.expresion.split("{}")
                contador_nomal = self.expresion.count("{}")

                if contador_nomal == len(self.lista):

                    for i in range (0,len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])
                        if i <= len(self.lista)-1:
                            texto_salida += str(self.lista[i].ObtenerValor(controlador,ts))

                    print("Print final: ", texto_salida)
                            #print("Obtener tipo: ", self.lista[i].ObtenerTipo(controlador, ts))


                else:
                    # Error
                    pass


            formato_lista = self.expresion.split("{:?}")
            contador_lista  = self.expresion.count("{:?}")

            controlador.imprimir(texto_salida, self.tipo)
        else:

            valor = self.expresion.ObtenerValor(controlador,ts)
            tipo = self.expresion.ObtenerTipo(controlador,ts)

            print("======!!!! ", tipo , " !!!!======")
            if tipo == t.STRING or tipo == t.DIRSTRING:
                print("Se confirmo")
                controlador.imprimir(valor , self.tipo)
            else:
                #error
                pass
