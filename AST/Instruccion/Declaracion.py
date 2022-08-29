from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo, RetornoType
from AST.Instruccion.DeclaracionArreglo import DeclaracionArreglo
class Declaracion(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo, mut,referencia = False):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo
        self.mut = mut
        self.referencia = referencia

    def EjecutarInstruccion(self, controlador, ts):
        print(" ==== Declarar === ",self.expresion)
        if self.expresion is not None:
            return_exp: RetornoType = self.expresion.ObtenerValor(controlador, ts)
            try:
                ValorExpresion = return_exp.valor
                TipoExpresion = return_exp.tipo
                if TipoExpresion == tipo.ARRAY:
                    declaracion_arreglo = DeclaracionArreglo(self.mut,self.identificador.id,None, self.expresion)
                    declaracion_arreglo.EjecutarInstruccion(controlador,ts)
                    return None
            except:
                print("Declaracion no se esta recuperando un dato")
                return None


            if self.tipo is not None:

                if type(self.tipo) == type(TipoExpresion):

                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

            else:
               # print("=== Se guardo aqui ===")
                self.tipo = TipoExpresion
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)
               # print(" Sin modificar Valor de la variable: ", newSimbolo.id, " valor de: ", newSimbolo.valor)
               # print(newSimbolo)

               # prueba: Simbolos = ts.ObtenerSimbolo("x")
               # prueba.valor = 999
               # print("Modificado Valor de la variable: ", prueba.id, " valor de: ", prueba.valor)
               # print(prueba)
               # print("=== Termino prueba ===")
                return None

        else:

            if self.tipo is not None:

                if self.tipo == tipo.ENTERO:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.DECIMAL:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, 0.0, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.CARACTER:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, '', self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.STRING or self.tipo == tipo.DIRSTRING:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, "", self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

                elif self.tipo == tipo.BOOLEANO:
                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, False, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

            else:
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, None, tipo.UNDEFINED, self.mut)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

       # print("=== SE DECLARO LA VARIABLES === ", self.identificador.id)
       # print("=== TIPO === ", self.tipo)
       # print("=== Expresion === ", self.expresion)
