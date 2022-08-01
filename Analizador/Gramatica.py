import ply.yacc as yacc

# Seccion de analizador lexico
# ********** PALABRAS RESERVADAS **********
reservadas = {

}

tokens = [
             # ACCESO
             'TK_PUBLICO',
             # TIPOS
             'TK_TIPOINT',
             'TK_TIPOFLOAT',
             'TK_TIPOBOOL',
             'TK_TIPOCHAR',
             'TK_TIPOSTRING',
             'TK_DIRSTRING',
             # CASTEO
             'TK_AS',
             # IMPRIMIR
             'TK_PRINTLN',
             # DECLARAR
             'TK_LET',
             'TK_MUT',
             # FUNCIONES
             'TK_FUNCION',
             'TK_MAIN',
             # FUNCIONES NATIVAS
             'TK_ABS',
             'TK_SQRT',
             'TK_TOSTRING',
             'TK_TOOWNED',
             'TK_CLONE',
             # VECTORES
             'TK_VECTOR',
             'TK_VECT',
             # FUNCIONES NATIVAS VECTORES
             'TK_NEW',
             'TK_LEN',
             'TK_PUSH',
             'TK_REMOVE',
             'TK_CONTAINS',
             'TK_INSERT',
             'TK_CAPACITY',
             'TK_WCAPACITY',
             # SENTENCIAS
             'TK_IF',
             'TK_ELSE',
             'TK_MATCH',
             # CICLOS
             'TK_LOOP',
             'TK_WHILE',
             'TK_FOR',
             'TK_IN',
             # SENTENCIAS DE RETORNO
             'TK_BREAK',
             'TK_CONTINUE',
             'TK_RETURN',
             # STRUCT
             'TK_STRUCT',
             # MODULO
             'TK_MOD',
             # POTENCIAS
             'TK_POW',
             'TK_POWF',
             # BOOLS
             'TK_TRUE',
             'TK_FALSE',
             'TK_PTCOMA',
             # ** ** ** ** ** OPERACION MATEMATICA ** ** ** ** **
             'TK_SUMA',
             'TK_RESTA',
             'TK_MULTI',
             'TK_DIVI',
             'TK_MODULO',
             # ** ** ** ** ** OPERACION RELACIONAL ** ** ** ** **
             'TK_MENORIGUAL',
             'TK_MAYORIGUAL',
             'TK_IGUALDAD',
             'TK_DESIGUALDAD',
             'TK_MENOR',
             'TK_MAYOR',
             # ** ** ** ** ** OPERACION LOGICA ** ** ** ** **
             'TK_OR',
             'TK_AND',
             'TK_NOT',
             # ** ** ** ** ** SIMBOLOS LENGUAJE ** ** ** ** **
             'TK_LI',
             'TK_LD',
             'TK_CI',
             'TK_CD',
             'TK_PI',
             'TK_PD',
             'TK_PYC',
             'TK_DP',
             'TK_COMA',
             'TK_PUNTO',
             'TK_IGUAL',
             'TK_BARRA',
             'TK_GBAJO',
             'TK_REFER',
             # ********** EXPRESIONES REGUALES **********
             'TK_FLOAT',
             'TK_ENTERO',
             'TK_CADENA',
             'TK_CARACTER',
             'TK_IDENTIFICADOR',
             # ********** IGNORAR **********
             'COMENTARIO_LIN',
             'WHITESPACE'
         ] + list(reservadas.values())

# ACCESO
TK_PUBLICO = r'pub'
# TIPOS
TK_TIPOINT = r'i64'
TK_TIPOFLOAT = r'f64'
TK_TIPOBOOL = r'bool'
TK_TIPOCHAR = r'char'
TK_TIPOSTRING = r'String'
TK_DIRSTRING = r'&str'
# CASTEO
TK_AS = r'as'
# IMPRIMIR
TK_PRINTLN = r'println!'
# DECLARAR
TK_LET = r'let'
TK_MUT = r'mut'
# FUNCIONES
TK_FUNCION = r'fn'
TK_MAIN = r'main'
# FUNCIONES NATIVAS
TK_ABS = r'abs'
TK_SQRT = r'sqrt'
TK_TOSTRING = r'to_string()'
TK_TOOWNED = r'to_owned()'
TK_CLONE = r'clone()'
# VECTORES
TK_VECTOR = r'Vec'
TK_VECT = r'vec!'
# FUNCIONES NATIVAS VECTORES
TK_NEW = r'::new()'
TK_LEN = r'len()'
TK_PUSH = r'push'
TK_REMOVE = r'remove'
TK_CONTAINS = r'contains'
TK_INSERT = r'insert'
TK_CAPACITY = r'capacity()'
TK_WCAPACITY = r'::with_capacity'
# SENTENCIAS
TK_IF = r'if'
TK_ELSE = r'else'
TK_MATCH = r'match'
# CICLOS
TK_LOOP = r'loop'
TK_WHILE = r'while'
TK_FOR = r'for'
TK_IN = r'in'
# SENTENCIAS DE RETORNO
TK_BREAK = r'break'
TK_CONTINUE = r'continue'
TK_RETURN = r'return'
# STRUCT
TK_STRUCT = r'struct'
# MODULO
TK_MOD = r'mod'
# POTENCIAS
TK_POW = r'::pow'
TK_POWF = r'::powf'
# BOOLS
TK_TRUE = r'true'
TK_FALSE = r'false'

# Tokens
TK_PTCOMA = r','

# ********** OPERACION MATEMATICA **********
TK_SUMA = r'\+'
TK_RESTA = r'-'
TK_MULTI = r'\*'
TK_DIVI = r'/'
TK_MODULO = r'%'
# ********** OPERACION RELACIONAL **********
TK_MENORIGUAL = r'<='
TK_MAYORIGUAL = r'>='
TK_IGUALDAD = r'=='
TK_DESIGUALDAD = r'!='
TK_MENOR = r'<'
TK_MAYOR = r'>'
# ********** OPERACION LOGICA **********
TK_OR = r'||'
TK_AND = r'&&'
TK_NOT = r'!'
# ********** SIMBOLOS LENGUAJE **********
TK_LI = r'\{'
TK_LD = r'\}'
TK_CI = r'\['
TK_CD = r'\]'
TK_PI = r'\('
TK_PD = r'\)'
TK_PYC = r';'
TK_DP = r':'
TK_COMA = r','
TK_PUNTO = r'.'
TK_IGUAL = r'='
TK_BARRA = r'|'
TK_GBAJO = r'_'
TK_REFER = r'&'

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()
