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
    programa : BEGIN vars programa2 MAIN LKEY vars programa3 RKEY END
             | BEGIN vars MAIN LKEY vars programa3 RKEY END
             | BEGIN programa2 MAIN LKEY vars programa3 RKEY END
             | BEGIN MAIN LKEY vars programa3 RKEY END
    '''

def p_programa2(p):
    '''
    programa2 : modulo
              | modulo programa2
    '''

def p_programa3(p):
    '''
    programa3 : bloque
              | bloque programa3
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

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | STRING
         | BOOL
    '''

def p_bloque(p):
    '''
    bloque : asignacion
           | condicion
           | lectura
           | escritura
           | loop
           | funcion
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUAL expresion SEMICOLON
               | ID EQUAL array SEMICOLON
               | ID EQUAL funcion SEMICOLON
               | ID LCORCH exp RCORCH EQUAL expresion SEMICOLON
    '''

def p_expresion(p):
    '''expresion : exp
                 | exp relop exp expresion1
    '''

def p_expresion1(p):
    '''expresion1 : relop exp
                  | empty
    '''

def p_relop(p):
    '''relop : GT
             | LT
             | GTE
             | LTE
             | DOUBLEEQUAL
             | NE
             | AND
             | OR
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
            | CTE_S
            | TRUE
            | FALSE
    '''

def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN LKEY bloque RKEY
              | IF LPAREN expresion RPAREN LKEY bloque RKEY ELSE LKEY bloque RKEY
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
    loop : LOOP LPAREN expresion RPAREN LKEY bloque RKEY
    '''

def p_funcion(p):
    '''
    funcion : ID LPAREN funcion1 RPAREN
    '''

def p_funcion1(p):
    '''
    funcion1 : exp
             | exp COMMA funcion1
    '''

def p_modulo(p):
    '''
    modulo : FUNC ID LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3
    '''

def p_modulo1(p):
    '''
    modulo1 : tipo ID
            | tipo ID COMMA modulo1
    '''

def p_modulo2(p):
    '''
    modulo2 : bloque
            | bloque modulo2
    '''
def p_modulo3(p):
    '''
    modulo3 : RETURN exp SEMICOLON RKEY
            | RKEY
    '''

def p_empty(p):
    'empty :'
    pass

# Regla de error para errores de sintaxis.
def p_error(p):
    print("Error de sintaxis en linea '%s'" % p.lexpos)
    sys.exit()


# Construir el parser.
print("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(entrada)
print(result)

# varsTable.show()
