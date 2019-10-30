# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.yacc as yacc
import sys
import pprint

# Obtener la lista de tokens del lexer.
from lex import tokens
# import vars_table as master
import tabla_master as master
import quadruples as quad
import dirFunc as funciones
# Leer archivo de prueba.
prueba = open("Exito1.txt", "r")
entrada = prueba.read()


idTemporal = None


# Declaración de funciones.
def p_programa(p):
    '''
    programa : BEGIN globalfunc vars programa2 funcfalse MAIN mainfunc LKEY vars programa3 separar RKEY END
             | BEGIN globalfunc vars MAIN mainfunc LKEY vars programa3 separar RKEY END
             | BEGIN programa2 funcfalse MAIN mainfunc LKEY vars programa3 separar RKEY END
             | BEGIN MAIN mainfunc LKEY vars programa3 separar RKEY END
    '''


# ############################# INICIAN FUNCIONES F ##########################
def p_globalfunc(p):
    '''
    globalfunc :
    '''
    master.insert("global", "int")

def p_programa2(p):
    '''
    programa2 : functrue modulo
              | functrue modulo programa2
    '''


def p_functrue(p):
    '''
    functrue :
    '''
    funciones.esFuncion = True


def p_funcfalse(p):
    '''
    funcfalse :
    '''
    funciones.esFuncion = False


def p_separar(p):
    '''
    separar :
    '''
    if funciones.funciones:
        funciones.separar()
        funciones.esFuncion = False


def p_modulo(p):
    '''
    modulo : FUNC tipo ID LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3
    '''
    global idTemporal
    idTemporal = p[3]
    master.insert(p[3], master.miTipo)
    funciones.miIdFunciones = p[3]
    # print("inserto id funcion")
    for i in funciones.funciones:
        if funciones.funciones[i].id_funcion is None:
            funciones.funciones[i].id_funcion = p[3]
    funciones.separar()

    funciones.funciones = {}
            # print("Inserto ID")
    # print(funciones.miIdFunciones)

def p_modulo1(p):
    '''
    modulo1 : tipo ID
            | tipo ID COMMA modulo1
            | empty
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

# ########################### ACABA FUNCIONES  ##############################


# ############################ INICIA VARIABLES MAIN #########################






def p_mainfunc(p):
    '''
    mainfunc :
    '''
    funciones.esMain = True
    master.insert("main", "int")


def p_programa3(p):
    '''
    programa3 : bloque
              | bloque programa3
    '''


############################# CIERRA VARIABLES MAIN #########################


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
    if funciones.esFuncion:
        funciones.insert(p[1], funciones.miTipo_f, None)
    elif funciones.esMain:
        funciones.insert(p[1], funciones.miTipo_f, "main")
    else:
        funciones.insert(p[1], funciones.miTipo_f, "global")


def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | STRING
         | BOOL
    '''
    master.miTipo = p[1]
    funciones.miTipo_f = p[1]


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
    if funciones.esFuncion:
        funciones.update(p[1], funciones.miValor_f, funciones.miIdFunciones)
        funciones.miID_f = p[1]
    elif funciones.esMain:
        funciones.update(p[1], funciones.miValor_f, "main")
        funciones.miID_f = p[1]
    else:
        funciones.update(p[1], funciones.miValor_f, "global")



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
    exp : termino pop_term
        | termino pop_term exp1
    '''


def p_pop_term(p):
    "pop_term :"
    quad.popTerm()


def p_exp1(p):
    '''
    exp1 : PLUS push_poper exp
         | MINUS push_poper exp
    '''


def p_termino(p):
    '''
    termino : factor pop_fact
            | factor pop_fact termino1
    '''


def p_pop_fact(p):
    "pop_fact :"
    quad.popFact()


def p_termino1(p):
    '''
    termino1 : MULT push_poper termino
             | DIV push_poper termino
    '''


def p_push_poper(p):
    "push_poper :"
    # quad.pushPoper(p[-1])


def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | PLUS var_cte
           | MINUS var_cte
           | var_cte
    '''


def p_var_cte(p):
    '''
    var_cte : ID push_id
            | CTE_I
            | CTE_F
            | CTE_S
            | TRUE
            | FALSE
    '''
    funciones.miValor_f = p[1]
    if len(p) == 2:
        master.miValor = p[1]


def p_push_id(p):
    "push_id :"
    quad.pushID(p[-1])
    master.miValor = 0


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


def p_empty(p):
    'empty :'
    pass
# Regla de error para errores de sintaxis.


def p_error(p):
    print(p)
    print("Error de sintaxis en linea '%s'" % p.lexpos)
    sys.exit()


# onstruir el parser.
print("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(entrada)
print(result)


# quad.show()
# master.show()
pprint.pprint(master.simbolos)
# funciones.imp()
