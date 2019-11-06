# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import ply.yacc as yacc
import sys
import memoria as memo
# Obtener la lista de tokens del lexer.
from lex import tokens
# import vars_table as master
import tabla_master as master
import quadruples as quad
# Leer archivo de prueba.
prueba = open("Exito1.txt", "r")
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


# Funcion que declarar cuantas funciones puede haber
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
    modulo : FUNC tipo ID seen_ID declararFunc LPAREN modulo1 RPAREN LKEY vars modulo2 modulo3 RKEY
    '''


def p_seen_ID(p):
    '''
    seen_ID :
    '''
    master.miIdFunciones = p[-1]


def p_declararFunc(p):
    '''
    declararFunc :
    '''
    master.insert(master.miIdFunciones, master.miTipo)


# Modulo que declara los parametros de la funcion
def p_modulo1(p):
    '''
    modulo1 : modulo1Aux
            | empty
    '''

# Modulo que declara los parametros de la funcion
def p_modulo1Aux(p):
    '''
    modulo1Aux : INT ID modulo1Repe
               | FLOAT ID modulo1Repe
               | STRING ID modulo1Repe
               | BOOL ID modulo1Repe
    '''
    master.insertIdToFunc(p[2], p[1], master.miIdFunciones, "Param")


def p_modulo1Repe(p):
    '''
    modulo1Repe : COMMA modulo1Aux
               | empty
    '''



# Modulo que declara el pedazo bloque
def p_modulo2(p):
    '''
    modulo2 : bloque
            | bloque modulo2
    '''


def p_modulo3(p):
    '''
    modulo3 : RETURN exp SEMICOLON
            | empty
    '''
    master.returnValor = master.returnValue(master.returnValor, master.miIdFunciones)
    #print("VALOR DE RETURN:", master.returnValor, "TYPE:", type(master.returnValor))
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
    if master.esFuncion:
        master.insertIdToFunc(p[1], master.miTipo, master.miIdFunciones, None)
    elif master.esMain:
        memo.memory_dir = memo.insertLocal(master.miTipo)
        master.insertIdToFunc(p[1], master.miTipo, "main", memo.memory_dir)
    else:
        memo.memory_dir = memo.insertGlobal(master.miTipo)
        master.insertIdToFunc(p[1], master.miTipo, "global", memo.memory_dir)



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
               | ID push_id LCORCH exp RCORCH EQUAL push_poper expresion pop_assign SEMICOLON
    '''


def p_pop_assign(p):
    "pop_assign :"
    master.miValor = quad.popAssign()
    # print(master.miValor)
    if master.esFuncion:
        master.updateIdInFunc(p[-5], master.miIdFunciones, master.miValor)
    elif master.esMain:
        master.updateIdInFunc(p[-5], "main", master.miValor)
        dir = master.getDireccion(p[-5], "main")
        type = master.getType(p[-5], "main")
        memo.updateLocal(master.miValor, dir, type)
    else:
        master.updateIdInFunc(p[-5], "global", master.miValor)
        dir = master.getDireccion(p[-5], "global")
        type = master.getType(p[-5], "global")
        memo.updateGlobal(master.miValor, dir, type)


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
             | AND
             | OR
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


def p_pop_poper(p):
    "pop_poper :"
    # quad.popTerm()
    # quad.popFact()
    # quad.popRelop()
    # quad.popLog()
    quad.popPoper()


def p_factor(p):
    '''
    factor : LPAREN push_poper logico RPAREN pop_poper
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
    master.returnValor = p[1]
    #print(p[1])
    if len(p) == 2:
        master.miValor = p[1]
    if master.esParam:
        temp = master.getValor(p[1], "main")
        master.updateIdInFunc(master.arrParam[-1], master.miParamFunc, temp)
        del(master.arrParam[-1])
        #master.updateIdInFunc(aux, master.miParamFunc, temp)



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
    lectura : INPUT push_poper LPAREN ID push_id RPAREN pop_io SEMICOLON
    '''


def p_escritura(p):
    '''
    escritura : OUTPUT push_poper LPAREN exp RPAREN pop_io SEMICOLON
    '''


def p_pop_io(p):
    "pop_io :"
    quad.popIO()


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
    funcion : ID getParamId LPAREN funcion1 RPAREN paramFalse SEMICOLON
    '''


def p_getParamId(p):
    '''
    getParamId :
    '''
    master.miParamFunc = p[-1]
    master.esParam = True
    master.arrParam = master.getidParam(p[-1])

def p_funcion1(p):
    '''
    funcion1 : exp
             | exp COMMA funcion1
    '''


def p_paramFalse(p):
    '''
    paramFalse :
    '''
    master.esParam = False

def p_empty(p):
    'empty :'
    pass
# Regla de error para errores de sintaxis.


def p_error(p):
    print(p)
    print("Error de sintaxis en linea '%s'" % p.lexpos)
    sys.exit()


# construir el parser.
print("Parsing . . . \n")
parser = yacc.yacc()
result = parser.parse(entrada)
print(result)


quad.show()
master.show()
# memo.show()
