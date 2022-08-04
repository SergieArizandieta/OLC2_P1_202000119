from AST.Abstracto.Instruccion import Intruccion
from AST.TablaSimbolos.Tipos import tipo as t

class Imprimir(Intruccion):

    def __init__(self,  expresion, tipo, lista):
        self.expresion = expresion
        self.tipo = tipo
        self.lista =lista

    def EjecutarInstruccion(self, controlador, ts):


        if len(self.lista) > 0:
            texto_salida = ""
            print(" Esta llena casdena: ", self.expresion )

            if  self.expresion.count("{}") > 0:
                formato_nomal = self.expresion.split("{}")
                contador_nomal = self.expresion.count("{}")

                if contador_nomal == len(self.lista):

                    for i in range (0,len(formato_nomal)):
                        texto_salida += str(formato_nomal[i])
                        if i <= len(self.lista)-1:
                            texto_salida += str(self.lista[i].ObtenerValor(controlador,ts))

                else:
                    # Error
                    pass


            formato_lista = self.expresion.split("{:?}")
            contador_lista  = self.expresion.count("{:?}")

            controlador.imprimir(texto_salida, self.tipo)
        else:
            print(" Esta vacia ")
            valor = self.expresion.ObtenerValor(controlador,ts)
            tipo = self.expresion.ObtenerTipo(controlador,ts)

            print("======!!!! ", tipo.tipo , " !!!!======")
            if tipo.tipo == t.CADENA:
                print("Se confirmo")
                controlador.imprimir(valor , self.tipo)
            else:
                #error
                pass
