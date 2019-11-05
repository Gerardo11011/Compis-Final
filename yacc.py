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
# Leer archivo de prueba.
prueba = open("Exito3.txt", "r")
entrada = prueba.read()


idTemporal = None


# Declaración de funciones.
def p_programa(p):
    '''
    programa : BEGIN globalfunc vars modulo2 programa2 funcfalse MAIN mainfunc LKEY vars programa3 RKEY END
             | BEGIN globalfunc vars modulo2 MAIN mainfunc LKEY vars programa3 RKEY END
             | BEGIN programa2 funcfalse MAIN mainfunc LKEY vars programa3 RKEY END
             | BEGIN MAIN mainfunc LKEY vars programa3 RKEY END
    '''


# ############################# INICIAN FUNCIONES F ##########################
def p_globalfunc(p):
    '''
    globalfunc :
    '''
    master.insert("global", None)
    master.funciones.append("global")


def p_programa2(p):
    '''
    programa2 : functrue modulo
              | functrue modulo programa2
    '''


def p_functrue(p):
    '''
    functrue :
    '''
    master.esFuncion = True


def p_funcfalse(p):
    '''
    funcfalse :
    '''
    master.esFuncion = False


def p_modulo(p):
    '''
    modulo : FUNC tipo ID seen_ID declararFunc LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3
    '''


def p_seen_ID(p):
    '''
    seen_ID :
    '''
    master.miIdFunciones = p[-1]
    master.funciones.append(p[-1])


def p_declararFunc(p):
    '''
    declararFunc :
    '''
    master.insert(master.miIdFunciones, master.miTipo)


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
    master.esMain = True
    master.insert("main", None)
    master.funciones.append("main")


def p_programa3(p):
    '''
    programa3 : bloque
              | bloque programa3
    '''


# ############################ CIERRA VARIABLES MAIN #########################


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
    if master.esFuncion:
        master.insertIdToFunc(p[1], master.miTipo, master.miIdFunciones)
    elif master.esMain:
        master.insertIdToFunc(p[1], master.miTipo, "main")
    else:
        master.insertIdToFunc(p[1], master.miTipo, "global")


def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | STRING
         | BOOL
    '''
    master.miTipo = p[1]


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
    asignacion : ID push_id EQUAL push_poper logico pop_assign SEMICOLON
               | ID push_id EQUAL push_poper array pop_assign SEMICOLON
               | ID push_id EQUAL push_poper funcion pop_assign SEMICOLON
               | ID push_id LCORCH exp RCORCH EQUAL push_poper logico pop_assign SEMICOLON
    '''


def p_pop_assign(p):
    "pop_assign :"
    master.miValor = quad.popAssign()
    if master.esFuncion:
        master.updateIdInFunc(p[-5], master.miIdFunciones, master.miValor)
    elif master.esMain:
        master.updateIdInFunc(p[-5], "main", master.miValor)
    else:
        master.updateIdInFunc(p[-5], "global", master.miValor)


def p_logico(p):
    '''
    logico : expresion pop_log
           | expresion pop_log logico1
    '''


def p_pop_log(p):
    "pop_log :"
    quad.popLog()


def p_logico1(p):
    '''
    logico1 : AND push_poper logico
            | OR push_poper logico
    '''


def p_expresion(p):
    '''expresion : exp
                 | exp relop exp pop_relop
    '''


# def p_expresion1(p):
#     '''expresion1 : relop exp
#                   | empty
#     '''


def p_pop_relop(p):
    "pop_relop :"
    quad.popRelop()


def p_relop(p):
    '''relop : GT
             | LT
             | GTE
             | LTE
             | DOUBLEEQUAL
             | NE
    '''
    quad.pushPoper(p[1])


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
    quad.pushPoper(p[-1])


def p_factor(p):
    '''
    factor : LPAREN logico RPAREN
           | PLUS var_cte
           | MINUS var_cte
           | var_cte
    '''


def p_var_cte(p):
    '''
    var_cte : ID push_id
            | CTE_I push_cte
            | CTE_F push_cte
            | CTE_S push_cte
            | TRUE push_cte
            | FALSE push_cte
    '''
    # master.miValor = p[1]
    if len(p) == 2:
        master.miValor = p[1]


def p_push_id(p):
    "push_id :"
    if master.esFuncion:
        quad.pushID(p[-1], master.miIdFunciones)
    elif master.esMain:
        quad.pushID(p[-1], 'main')
    else:
        quad.pushID(p[-1], 'global')


def p_push_cte(p):
    "push_cte :"
    quad.pushCte(p[-1])


def p_condicion(p):
    '''
    condicion : IF LPAREN logico RPAREN ifelse1 LKEY modulo2 RKEY ifelse2
              | IF LPAREN logico RPAREN ifelse1 LKEY modulo2 RKEY ELSE ifelse3 LKEY modulo2 RKEY ifelse2
    '''


def p_ifelse1(p):
    "ifelse1 :"
    quad.ifelseUno()


def p_ifelse2(p):
    "ifelse2 :"
    quad.ifelseDos()


def p_ifelse3(p):
    "ifelse3 :"
    quad.ifelseTres()


def p_lectura(p):
    '''
    lectura : INPUT push_poper LPAREN ID push_id RPAREN pop_out SEMICOLON
    '''


def p_escritura(p):
    '''
    escritura : OUTPUT push_poper LPAREN exp RPAREN pop_out SEMICOLON
    '''


def p_pop_out(p):
    "pop_out :"
    quad.popOut()


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
    loop : LOOP loop1 LPAREN logico RPAREN loop2 LKEY modulo2 RKEY loop3
    '''


def p_loop1(p):
    "loop1 :"
    quad.loopUno()


def p_loop2(p):
    "loop2 :"
    quad.loopDos()


def p_loop3(p):
    "loop3 :"
    quad.loopTres()


def p_funcion(p):
    '''
    funcion : ID LPAREN funcion1 RPAREN SEMICOLON
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


quad.show()
master.show()
# pprint.pprint(master.simbolos)
# funciones.imp()
