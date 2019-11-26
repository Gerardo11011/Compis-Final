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


# Funciones para producir representación inetermedia para Main
def gotoMain():
    quadr = quadruple(len(Quad), 'goto', None, None, None)
    Quad.append(quadr)


def endprog():
    quadr = quadruple(len(Quad), 'end', None, None, None)
    Quad.append(quadr)


# Funciones para producir representación intermedia para operadores
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


def pushPoper(operator):
    POper.append(operator)


def popPoper():
    POper.pop()


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


# Función para producir representación intermedia para lectura y escritura
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


# Funciones para producir representación intermedia para If Else
def fill(cuadruplo, salto):
    Quad[cuadruplo].result = salto


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


def ifelseDos():
    end = PJumps.pop()
    fill(end, len(Quad))


def ifelseTres():
    quadr = quadruple(len(Quad), "goto", None, None, None)
    Quad.append(quadr)
    false = PJumps.pop()
    PJumps.append(len(Quad)-1)
    fill(false, len(Quad))


# Funciones para producir representación intermedia para Loop
def loopUno():
    PJumps.append(len(Quad))


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


def loopTres():
    end = PJumps.pop()
    regresa = PJumps.pop()
    quadr = quadruple(len(Quad), "goto", None, None, regresa)
    Quad.append(quadr)
    fill(end, len(Quad))


# Funciones para producir representación intermedia para Módulos
def moduloDos(id):
    quadr = quadruple(len(Quad), 'era', None, None, id)
    Quad.append(quadr)
    global paramCont
    paramCont = 1


def moduloTres():
    argument = PilaO.pop()
    PTypes.pop()
    valor = AVAIL.pop()
    num = str(paramCont)
    quadr = quadruple(len(Quad), 'param', argument, None, 'param'+num)
    Quad.append(quadr)
    return valor


def moduloCuatro():
    global paramCont
    paramCont = paramCont + 1


def moduloSeis(id, addr):
    quadr = quadruple(len(Quad), 'gosub', id, None, addr)
    Quad.append(quadr)


def miReturn():
    result = PilaO.pop()
    PTypes.pop()
    AVAIL.pop()
    quadr = quadruple(len(Quad), 'return', None, None, result)
    Quad.append(quadr)


def endproc(id):
    quadr = quadruple(len(Quad), 'endproc', None, None, id)
    Quad.append(quadr)


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


def pushFunc(funcion):
    PilaO.append(150000)
    PTypes.append(simbolos[funcion].type_data)
    AVAIL.append(0)


# Funciones para producir representación intermedia para Arreglos
def arregloDos(funcion, id):
    if simbolos[funcion].value[id].dimensionada > 0:
        pushPoper('[')


def arregloTres(tam):
    quadr = quadruple(len(Quad), 'ver', PilaO[-1], 0, tam-1)
    Quad.append(quadr)


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


def show():
    for i in range(0, len(Quad)):
        print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
