from AST.Abstracto.Instruccion import Intruccion
from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.Instruccion.DeclaracionArreglo import DeclaracionArreglo
from colorama import Fore
from colorama import Style

class DeclaracionVector(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo  , mut = False, referencia = False):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo
        self.capacidad = 0
        self.mut = mut
        self.referencia = referencia


    def EjecutarInstruccion(self, controlador, ts):
        print(Fore.BLUE + Style.BRIGHT + "Llegpo a declaracion arreglo" + Style.RESET_ALL)
        print("Llego bien a declarar vector jdsjdasfjkdfsa")
        if  not isinstance(self.expresion,list):
            Exp_arreglo: RetornoType = self.expresion.ObtenerValor(controlador, ts)
            objetoVector = Exp_arreglo.valor

            if self.tipo != objetoVector.tipo:
                return None

            objetoVector.identificador = self.identificador
            objetoVector.mut = self.mut
            ts.Agregar_Simbolo(self.identificador, objetoVector)
            ts.Print_Table()
            print("Hola: ",objetoVector)
        else:
            if len( self.expresion) ==0:
                print("Llego solo con decalracion normal" )
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador, [], self.tipo, self.mut)
                ts.Agregar_Simbolo(self.identificador, newSimbolo)
            else:
                print("Llego solo con decalracion capacity")
                newSimbolo = Simbolos()
                self.capacidad= self.expresion.pop(0).ObtenerValor(controlador, ts).valor
                newSimbolo.SimboloPremitivo(self.identificador, [], self.tipo, self.mut)
                ts.Agregar_Simbolo(self.identificador, newSimbolo)