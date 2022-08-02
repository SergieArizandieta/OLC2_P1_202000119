reservadas = {
    # ACCESO
    'pub': 'PUBLICO',
    # TIPOS
    'i64': 'TIPOINT',
    'f64': 'TIPOFLOAT',
    'bool': 'TIPOBOOL',
    'char': 'TIPOCHAR',
    'String': 'TIPOSTRING',
    '&str': 'DIRSTRING',
    # CASTEO
    'as': 'AS',
    # IMPRIMIR
    'println!': 'PRINTLN',
    # DECLARAR
    'let': 'LET',
    'mut': 'MUT',
    # FUNCIONES
    'fn': 'FUNCION',
    'main': 'MAIN',
    # FUNCIONES NATIVAS
    'abs': 'ABS',
    'sqrt': 'SQRT',
    'to_string()': 'TOSTRING',
    'to_owned()': 'TOOWNED',
    'clone()': 'CLONE',
    # VECTORES
    'Vec': 'VECTOR',
    'vec!': 'VECT',
    # FUNCIONES NATIVAS VECTORES
    '::new()': 'NEW',
    'len()': 'LEN',
    'push': 'PUSH',
    'remove': 'REMOVE',
    'contains': 'CONTAINS',
    'insert': 'INSERT',
    'capacity()': 'CAPACITY',
    '::with_capacity': 'WCAPACITY',
    # SENTENCIAS
    'if': 'IF',
    'else': 'ELSE',
    'match': 'MATCH',
    # CICLOS
    'loop': 'LOOP',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    # SENTENCIAS DE RETORNO
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    # STRUCT
    'struct': 'STRUCT',
    # MODULO
    'mod': 'MOD',
    # POTENCIAS
    '::pow': 'POW',
    '::powf': 'POWF',
    # BOOLS
    'true': 'TRUE',
    'false': 'FALSE'
}

tokens = [
             # ** ** ** ** ** OPERACION MATEMATICA ** ** ** ** **
             'SUMA',
             'RESTA',
             'MULTI',
             'DIVI',
             'MODULO',
             # ** ** ** ** ** OPERACION RELACIONAL ** ** ** ** **
             'MENORIGUAL',
             'MAYORIGUAL',
             'IGUALDAD',
             'DESIGUALDAD',
             'MENOR',
             'MAYOR',
             # ** ** ** ** ** OPERACION LOGICA ** ** ** ** **
             'OR',
             'AND',
             'NOT',
             # ** ** ** ** ** SIMBOLOS LENGUAJE ** ** ** ** **
             'LI',
             'LD',
             'CI',
             'CD',
             'PI',
             'PD',
             'PYC',
             'DP',
             'COMA',
             'PUNTO',
             'IGUAL',
             'BARRA',
             'GBAJO',
             'REFER',
             # ********** EXPRESIONES REGUALES **********
             'FLOAT',
             'ENTERO',
             'CADENA',
             'CARACTER',
             'ID',
             'ERR'
         ] + list(reservadas.values())

# Tokens
# ********** OPERACION MATEMATICA **********
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTI = r'\*'
t_DIVI = r'/'
t_MODULO = r'%'
# ********** OPERACION RELACIONAL **********
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUALDAD = r'=='
t_DESIGUALDAD = r'!='
t_MENOR = r'<'
t_MAYOR = r'>'
# ********** OPERACION LOGICA **********
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
# ********** SIMBOLOS LENGUAJE **********
t_LI = r'\{'
t_LD = r'\}'
t_CI = r'\['
t_CD = r'\]'
t_PI = r'\('
t_PD = r'\)'
t_PYC = r';'
t_DP = r':'
t_COMA = r','
t_PUNTO = r'\.'
t_IGUAL = r'='
t_BARRA = r'\|'
t_GBAJO = r'_'
t_REFER = r'&'


def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        print("Se reconcio FLOAT ", t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        print("Se reconcio ENTERO ", t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_Especiales_0(t):
    r'::[a-zA-Z_][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_1(t):
    r'[a-zA-Z][a-zA-Z_0-9]*\(\)'
    return revicion_reservadas(t)


def t_Especiales_2(t):
    r'::[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


def t_Especiales_3(t):
    r'[a-zA-Z][a-zA-Z_0-9]*!'
    return revicion_reservadas(t)


def t_Especiales_4(t):
    r'&[a-zA-Z][a-zA-Z_0-9]*'
    return revicion_reservadas(t)


# [a-zA-Z_][a-zA-Z_0-9]*
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def revicion_reservadas(t):
    t.type = reservadas.get(t.value, 'ERR')
    print("Se reconcio: ", t.type, ": ", t.value)
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    print("Se reconcio cadena ", t.value)
    return t


# Comentario simple // ...
def t_COMENTARIO(t):
    r'//.*\n'
    print("Se reconcio comentario ", t.value.replace('\n', ''))
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t\r"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Error lexico ", t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()


# Definición de la gramática
def p_init(t):
    'init            : CADENA'
    t[0] = t[1]


def p_error(t):
    # print(t)
    # print("Error sintáctico en '%s'" % t.value)
    pass


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
