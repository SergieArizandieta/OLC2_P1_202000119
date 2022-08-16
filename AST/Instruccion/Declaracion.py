from AST.Abstracto.Instruccion import Intruccion
from AST.Expresion import Identificador
from AST.TablaSimbolos.Simbolos import Simbolos
from AST.TablaSimbolos.Tipos import tipo

class Declaracion(Intruccion):

    def __init__(self, id: Identificador, expresion, tipo, mut):
        self.identificador = id
        self.expresion = expresion
        self.tipo = tipo
        self.mut = mut

    def EjecutarInstruccion(self, controlador, ts):

        if self.expresion is not None:

            ValorExpresion = self.expresion.ObtenerValor(controlador, ts)
            TipoExpresion = self.expresion.ObtenerTipo(controlador, ts)

            if self.tipo is not None:
                if type(self.tipo) == type(TipoExpresion):

                    newSimbolo = Simbolos()
                    newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                    ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

            else:

                self.tipo = TipoExpresion
                newSimbolo = Simbolos()
                newSimbolo.SimboloPremitivo(self.identificador.id, ValorExpresion, self.tipo, self.mut)
                ts.Agregar_Simbolo(self.identificador.id, newSimbolo)

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
