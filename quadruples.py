# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import sys

import tabla_master as tabla
from tabla_master import simbolos
from semantic_cube import semantic
import memoria as memo

# Declaración de pilas
POper = []
PilaO = []
PTypes = []
Quad = []
AVAIL = []
PJumps = []

paramCont = 0


# Clase Cuadruplo
class quadruple(object):
    def __init__(self, num, operator, left_operand, right_operand, result):
        self.num = num
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result


# ################ REPRESENTACIÓN INTERMEDIA PARA MAIN ####################

# Función que agrega a la pila de cuádruplo el goto main con el número de
# cuádruplo correspondiente.
def gotoMain():
    quadr = quadruple(len(Quad), 'goto', None, None, None)
    Quad.append(quadr)


# Función que agrega a la pila de cuádruplos el endprog de la función.
def endprog():
    quadr = quadruple(len(Quad), 'end', None, None, None)
    Quad.append(quadr)


# ############## REPRESENTACIÓN INTERMEDIA PARA OPERADORES ##################

# Función que recibe una variable y su función, y agrega su dirección a la
# pila de operandos, su tipo a la pila de tipos y su valor a la pila AVAIL.
def pushID(id, funcion):
    encontro = False
    for keys in simbolos:
        if funcion == keys:
            if simbolos[keys].value is not None:
                for var in simbolos[keys].value:
                    if id == var:
                        encontro = True
                        PilaO.append(tabla.getDireccion(id, funcion))
                        PTypes.append(simbolos[keys].value[var].type_data)
                        AVAIL.append(simbolos[keys].value[var].value)
    if encontro is False:
        if tabla.isVarGlobal(id):
            encontro = True
            PilaO.append(tabla.getDireccion(id, 'global'))
            PTypes.append(simbolos['global'].value[id].type_data)
            AVAIL.append(simbolos['global'].value[id].value)
    if encontro is False:
        print('ERROR: Variable no declarada.', id)
        sys.exit()


# Función que recibe una constante, su dirección y tipo, y agrega su dirección
# tipo y valor a sus respectiva pilas.
def pushCte(cte, dir, tipo):
    PilaO.append(dir)
    tipo = str(type(cte))
    if cte == 'true' or cte == 'false':
        tipo = "<class 'bool'>"
    if tipo == "<class 'float'>":
        PTypes.append('float')
    if tipo == "<class 'int'>":
        PTypes.append('int')
    if tipo == "<class 'str'>":
        PTypes.append('string')
    if tipo == "<class 'bool'>":
        PTypes.append('bool')
    AVAIL.append(cte)


# Función que recibe un operador y lo agrega a la pila de operadores.
def pushPoper(operator):
    POper.append(operator)


# Función que saca el último operador de la pila de operadores.
def popPoper():
    POper.pop()


# Función que obtiene los atributos del cuádruplo de asignación, realiza la
# verificación semántica, genera el cuádruplo de asignación y regresa el valor
# que se le asignará a la variable.
def popAssign():
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == '=':
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                if right_value is not None:
                    result = right_value
                    quadr = quadruple(len(Quad), operator, right_operand, None, left_operand)
                    Quad.append(quadr)
                else:
                    print("ERROR: Variable sin valor asignado.")
                    sys.exit()
            else:
                print("ERROR: Type mismatch.")
                sys.exit()
    return result


# Función que recibe main para saber qué direción temporal asignar, obtiene los
# atributos del cuádruplo de suma o resta, realiza la verificación semántica y
# genera el cuádruplo de correspondiente.
def popTerm(main):
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == '+' or POper[POperSize-1] == '-':
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                if left_value is not None and right_value is not None:
                    if(operator == '+'):
                        result = left_value + right_value
                    else:
                        result = left_value - right_value
                    if main:
                        dir = memo.getVirtualMainTemp(result_type)
                        memo.updateMainTempInMemory(result, dir, result_type)
                    else:
                        dir = memo.getVirtualTemp(result_type)
                        memo.updateTempInMemory(result, dir, result_type)
                    quadr = quadruple(len(Quad), operator, left_operand, right_operand, dir)
                    Quad.append(quadr)
                    PilaO.append(dir)
                    AVAIL.append(result)
                    PTypes.append(result_type)
                else:
                    print("ERROR: Variable sin valor asignado")
                    sys.exit()
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


# Función que recibe main para saber qué direción temporal asignar, obtiene los
# atributos del cuádruplo de multiplicación o división, realiza la verificación
# semántica y genera el cuádruplo correspondiente.
def popFact(main):
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == '*' or POper[POperSize-1] == '/':
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                if left_value is not None and right_value is not None:
                    if(operator == '*'):
                        result = left_value * right_value
                    else:
                        result = left_value / right_value
                    if main:
                        dir = memo.getVirtualMainTemp(result_type)
                        memo.updateMainTempInMemory(result, dir, result_type)
                    else:
                        dir = memo.getVirtualTemp(result_type)
                        memo.updateTempInMemory(result, dir, result_type)
                    quadr = quadruple(len(Quad), operator, left_operand, right_operand, dir)
                    Quad.append(quadr)
                    PilaO.append(dir)
                    AVAIL.append(result)
                    PTypes.append(result_type)
                else:
                    print("ERROR: Variable sin valor asignado.")
                    sys.exit()
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


# Función que recibe main para saber qué direción temporal asignar, obtiene los
# atributos del cuádruplo de operaciones relacionales, realiza la verificación
# semántica y genera el cuádruplo correspondiente.
def popRelop(main):
    POperSize = len(POper)
    if POperSize > 0:
        if(POper[POperSize-1] == '>' or POper[POperSize-1] == '>='
            or POper[POperSize-1] == '<' or POper[POperSize-1] == '<='
            or POper[POperSize-1] == '==' or POper[POperSize-1] == '<>'):
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                if left_value is not None and right_value is not None:
                    if(operator == '>'):
                        result = left_value > right_value
                    elif(operator == '>='):
                        result = left_value >= right_value
                    elif(operator == '<'):
                        result = left_value < right_value
                    elif(operator == '<='):
                        result = left_value <= right_value
                    elif(operator == '=='):
                        result = left_value == right_value
                    elif(operator == '<>'):
                        result = left_value != right_value
                    if main:
                        dir = memo.getVirtualMainTemp(result_type)
                        memo.updateMainTempInMemory(result, dir, result_type)
                    else:
                        dir = memo.getVirtualTemp(result_type)
                        memo.updateTempInMemory(result, dir, result_type)
                    quadr = quadruple(len(Quad), operator, left_operand, right_operand, dir)
                    Quad.append(quadr)
                    PilaO.append(dir)
                    AVAIL.append(result)
                    PTypes.append(result_type)
                else:
                    print("ERROR: Variable sin valor asignado.")
                    sys.exit()
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


# Función que recibe main para saber qué direción temporal asignar, obtiene los
# atributos del cuádruplo de operaciones lógicas, realiza la verificación
# semántica y genera el cuádruplo correspondiente.
def popLog(main):
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == 'and' or POper[POperSize-1] == 'or':
            right_operand = PilaO.pop()
            right_type = PTypes.pop()
            right_value = AVAIL.pop()
            left_operand = PilaO.pop()
            left_type = PTypes.pop()
            left_value = AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                if left_value is not None and right_value is not None:
                    if(operator == 'and'):
                        result = left_value and right_value
                    else:
                        result = left_value or right_value
                    if main:
                        dir = memo.getVirtualMainTemp(result_type)
                        memo.updateMainTempInMemory(result, dir, result_type)
                    else:
                        dir = memo.getVirtualTemp(result_type)
                        memo.updateTempInMemory(result, dir, result_type)
                    quadr = quadruple(len(Quad), operator, left_operand, right_operand, dir)
                    Quad.append(quadr)
                    PilaO.append(dir)
                    AVAIL.append(result)
                    PTypes.append(result_type)
                else:
                    print("ERROR: Variable sin valor asignado.")
                    sys.exit()
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


# ######### REPRESENTACIÓN INTERMEDIA PARA LECTURA Y ESCRITURA ###############

# Función que genera los cuádruplos de lectura o escritura dependiendo del
# operador obtenido de la pila de operadores.
def popIO():
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == 'output' or POper[POperSize-1] == 'input':
            right_operand = PilaO.pop()
            PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            quadr = quadruple(len(Quad), operator, None, None, right_operand)
            Quad.append(quadr)


# ######### REPRESENTACIÓN INTERMEDIA PARA IF Y IF ELSE ###############

# Función que recibe el número de cuádruplo donde se encuentra el goto y el
# número de cuádruplos a donde se realizará el salto y actualiza el cuádruplo.
def fill(cuadruplo, salto):
    Quad[cuadruplo].result = salto


# Función que verifica que el último operando en la pila sea booleano y genera
# el cuádruplo de gotof.
def ifelseUno():
    exp_type = PTypes.pop()
    if exp_type == "bool":
        result = PilaO.pop()
        quadr = quadruple(len(Quad), "gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR: Type mismatch.")
        sys.exit()


# Función que manda a actualizar el cuádruplo del goto o gotof con el número
# de cuádruplo donde se realizará el salto.
def ifelseDos():
    end = PJumps.pop()
    fill(end, len(Quad))


# Función que genera el cuádruplo goto y manda llenar el cuádruplo de gotof
# generado en un if else.
def ifelseTres():
    quadr = quadruple(len(Quad), "goto", None, None, None)
    Quad.append(quadr)
    false = PJumps.pop()
    PJumps.append(len(Quad)-1)
    fill(false, len(Quad))


# ################### REPRESENTACIÓN INTERMEDIA PARA LOOP ###################

# Función que agrega el número de cuádruplo en la pila PJumps donde se hará la
# evaluación de la expresión del loop.
def loopUno():
    PJumps.append(len(Quad))


# Función que verifica que el último operando en la pila sea booleano y genera
# el cuádruplo de gotof.
def loopDos():
    exp_type = PTypes.pop()
    if exp_type == "bool":
        result = PilaO.pop()
        quadr = quadruple(len(Quad), "gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR: Type mismatch.")
        sys.exit()


# Función que genera el cuádruplo goto y manda llenar el cuádruplo de gotof
# generado en el loop.
def loopTres():
    end = PJumps.pop()
    regresa = PJumps.pop()
    quadr = quadruple(len(Quad), "goto", None, None, regresa)
    Quad.append(quadr)
    fill(end, len(Quad))


# ################ REPRESENTACIÓN INTERMEDIA PARA MÓDULOS #####################

# Función que recibe el id de la función, genera el cuádruplo era de dicha
# función e incializa el contador de parámetros en 1.
def moduloDos(id):
    quadr = quadruple(len(Quad), 'era', None, None, id)
    Quad.append(quadr)
    global paramCont
    paramCont = 1


# Función que genera el cuádruplo param con el parámetro obtenido de la pila
# de operandos y el número de de parámetros, y regresa el valor para ctualizar.
def moduloTres():
    argument = PilaO.pop()
    PTypes.pop()
    valor = AVAIL.pop()
    num = str(paramCont)
    quadr = quadruple(len(Quad), 'param', argument, None, 'param'+num)
    Quad.append(quadr)
    return valor


# Función que actualiza el contador de parámetros.
def moduloCuatro():
    global paramCont
    paramCont = paramCont + 1


# Función que recibe el id de la función y su número de cuádruplo y genera el
# cuádruplo gosub.
def moduloSeis(id, addr):
    quadr = quadruple(len(Quad), 'gosub', id, None, addr)
    Quad.append(quadr)


# Función que genera el cuádruplo return con el resultado a regresar
# obtenido de la pila de operandos.
def miReturn():
    result = PilaO.pop()
    PTypes.pop()
    AVAIL.pop()
    quadr = quadruple(len(Quad), 'return', None, None, result)
    Quad.append(quadr)


# Función que recibe el id de la función y genera el cuádruplo endproc de
# dicha función.
def endproc(id):
    quadr = quadruple(len(Quad), 'endproc', None, None, id)
    Quad.append(quadr)


# Función que recibe el id de una función para obtener su tipo y asigna el
# valor de su return a la variable obtenida de la pila de operandos.
def assignFunc(id):
    tipoFunc = simbolos[id].type_data
    POperSize = len(POper)
    if POperSize > 0:
        if POper[POperSize-1] == '=':
            result = PilaO.pop()
            type = PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(type, tipoFunc, operator)
            if result_type != 'error':
                quadr = quadruple(len(Quad), '=', 150000, None, result)
                Quad.append(quadr)
            else:
                print('ERROR: Type mismatch.')
                sys.exit()


# Función que mete el valor regresado de una función a la pila de operandos,
# así como su tipo, obtenidos de su id que ingresa como parámetro.
def pushFunc(funcion):
    PilaO.append(150000)
    PTypes.append(simbolos[funcion].type_data)
    AVAIL.append(0)


# ################ REPRESENTACIÓN INTERMEDIA PARA ARREGLOS ###################

# Función que mete a la pila de operadores el corchete izquierdo de un arreglo
# como un fondo falso.
def arregloDos(funcion, id):
    pushPoper('[')


# Función que recibe el tamaño del arreglo y genera el cuádruplo ver con el
# último valor de la pila de operandos.
def arregloTres(tam):
    quadr = quadruple(len(Quad), 'ver', PilaO[-1], 0, tam-1)
    Quad.append(quadr)


# Función que recibe el main, la base y el tipo del arreglo para generar los
# cuádruplos de la operación s + k + dirBase, agregando la dirección que tendrá
# otra dirección almacenada al final del cuádruplo.
def arregloCinco(main, base, tipo):
    aux1 = PilaO.pop()
    if main:
        t = memo.getVirtualMainTemp('int')
    else:
        t = memo.getVirtualTemp('int')
    quadr = quadruple(len(Quad), '+', aux1, 0, t)
    Quad.append(quadr)
    if main:
        dir = memo.getVirtualMainTemp('int')
        memo.updateMainTempInMemory(aux1, dir, 'int')
    else:
        dir = memo.getVirtualTemp('int')
        memo.updateTempInMemory(aux1, dir, 'int')
    quadr = quadruple(len(Quad), '+', t, base, dir)
    Quad.append(quadr)
    PilaO.append('('+str(dir)+')')
    PTypes.append(tipo)
    POper.pop()


# Función que imprime los cuádruplos dentro de la pila de cuádruplos.
def show():
    for i in range(0, len(Quad)):
        print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
