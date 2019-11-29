# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.lex as lex
import ply.yacc as yacc
import sys

archivo = None

# Lista de palabras reservadas.
reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'loop': 'LOOP',
    'func': 'FUNC',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'bool': 'BOOL',
    'input': 'INPUT',
    'output': 'OUTPUT',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'void': 'VOID'
}

# Lista de Tokens.
tokens = [

    'PLUS',
    'MINUS',
    'MULT',
    'DIV',

    'EQUAL',
    'DOUBLEEQUAL',
    'GT',
    'GTE',
    'LT',
    'LTE',
    'NE',

    'SEMICOLON',
    'COMMA',
    'LKEY',
    'RKEY',
    'LPAREN',
    'RPAREN',
    'LCORCH',
    'RCORCH',

    'CTE_S',
    'CTE_I',
    'CTE_F',

    'ID'

]


# Declaración de Tokens.
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

t_EQUAL = r'\='
t_DOUBLEEQUAL = r'\=='
t_GT = r'\>'
t_GTE = r'\>='
t_LT = r'\<'
t_LTE = r'\<='
t_NE = r'\<>'

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'

t_CTE_S = r'\"([^\\\n]|(\\.))*?\"'

tokens += list(reserved.values())


# Ignorar caracteres especiales.
t_ignore = ' \t\n'


# Declaración de funciones.
def t_CTE_F(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CTE_I(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)


# Construir lexer.
lexer = lex.lex()

# Leer archivo de prueba.
x = (input('''¿Qué archivo desea leer?
    1.- Exito1
    2.- Exito2
    3.- Exito3
    4.- Exito4
    5.- Exito5
    6.- Exito6
    f.- Fibonacci
    fac.- Factorial
    s.- Sort
    find.- Find
'''))
if x == "1":
    prueba = open('Pruebas/Exito1.txt', "r")
    archivo = 'Pruebas/Exito1.txt'
    entrada = prueba.read()
elif x == "2":
    prueba = open('Pruebas/Exito2.txt', "r")
    archivo = 'Pruebas/Exito2.txt'
    entrada = prueba.read()
elif x == "3":
    prueba = open('Pruebas/Exito3.txt', "r")
    archivo = 'Pruebas/Exito3.txt'
    entrada = prueba.read()
elif x == "4":
    prueba = open('Pruebas/Exito4.txt', "r")
    archivo = 'Pruebas/Exito4.txt'
    entrada = prueba.read()
elif x == "5":
    prueba = open('Pruebas/Exito5.txt', "r")
    archivo = 'Pruebas/Exito5.txt'
    entrada = prueba.read()
elif x == "6":
    prueba = open('Pruebas/Exito6.txt', "r")
    archivo = 'Pruebas/Exito6.txt'
    entrada = prueba.read()
elif x == 'f':
    prueba = open('Pruebas/fibonacchi.txt', "r")
    archivo = 'Pruebas/fibonacchi.txt'
    entrada = prueba.read()
elif x == 'fac':
    prueba = open('Pruebas/Factorial.txt', "r")
    archivo = 'Pruebas/Factorial.txt'
    entrada = prueba.read()
elif x == 's':
    prueba = open('Pruebas/Sort.txt', "r")
    archivo = 'Pruebas/Sort.txt'
    entrada = prueba.read()
elif x == 'find':
    prueba = open('Pruebas/Find.txt', "r")
    archivo = 'Pruebas/Find.txt'
    entrada = prueba.read()
else:
    print("ERROR")
    sys.exit()

# Entrada del lexer.
lexer.input(entrada)

# Mostrar tokens.
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
