# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.yacc as yacc
import sys

# Obtener la lista de tokens del lexer.
from lex import tokens
import vars_table as varsTable

# Leer archivo de prueba.
prueba = open("Exito1.txt", "r")
entrada = prueba.read()

# Declaración de funciones.
def p_programa(p):
    '''
    programa : BEGIN vars programa1 END
    '''

def p_programa1(p):
    '''
    programa1 : bloque
    | bloque programa1
    '''

def p_vars(p):
    '''
    vars : tipo vars1 SEMICOLON
    | tipo vars1 SEMICOLON vars
    '''

def p_vars1(p):
    '''
    vars1 : ID
    | ID COMMA vars1
    '''
    varsTable.insert(p[1], varsTable.miTipo)

def p_tipo(p):
    '''
    tipo : INT
    | FLOAT
    | CHAR
    '''
    varsTable.miTipo = p[1]

def p_bloque(p):
    '''
    bloque : asignacion
    | condicion
    | lectura
    | escritura
    | loop
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUAL expresion SEMICOLON
    | ID EQUAL array SEMICOLON
    '''
    varsTable.update(p[1], varsTable.miValor)

def p_expresion(p):
    '''expresion : exp
    | exp relop exp
    | exp relop exp AND expresion
    | exp relop exp OR expresion
    '''

def p_relop(p):
    '''relop : GT
    | LT
    | GTE
    | LTE
    | DOUBLEEQUAL
    | NE
    '''

def p_exp(p):
    '''
    exp : termino
        | termino exp1
    '''

def p_exp1(p):
    '''
    exp1 : PLUS exp
        | MINUS exp
    '''

def p_termino(p):
    '''
    termino : factor
            | factor termino1
    '''

def p_termino1(p):
    '''
    termino1 : MULT termino
             | DIV termino
    '''

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
            | PLUS var_cte
            | MINUS var_cte
            | var_cte
    '''

def p_var_cte(p):
    '''
    var_cte : ID
            | CTE_I
            | CTE_F
            | CTE_CH
    '''
    varsTable.miValor = p[1]

def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN THEN bloque condicion1
    '''

def p_condicion1(p):
    '''
    condicion1 : SEMICOLON
                | ELSE bloque SEMICOLON
    '''

def p_lectura(p):
    '''
    lectura : INPUT LPAREN ID RPAREN SEMICOLON
    '''

def p_escritura(p):
    '''
    escritura : OUTPUT LPAREN exp RPAREN SEMICOLON
    '''

def p_array(p):
    '''
    array : LCORCH array1 RCORCH
    '''

def p_array1(p):
    '''
    array1 : exp
            | exp COMMA array1
    '''

def p_loop(p):
    '''
    loop : LOOP LPAREN expresion RPAREN THEN bloque SEMICOLON
    '''


# Regla de error para errores de sintaxis.
def p_error(p):
    print(p.value)
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()


# Construir el parser.
print("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(entrada)
print(result)

varsTable.show()
