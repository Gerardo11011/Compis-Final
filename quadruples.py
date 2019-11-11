# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import sys

from tabla_master import simbolos
from semantic_cube import semantic

# Declaración de pilas
POper = []
PilaO = []
PTypes = []
Quad = []
AVAIL = []
PJumps = []


# Clase Cuadruplo
class quadruple(object):
    def __init__(self, num, operator, left_operand, right_operand, result):
        self.num = num
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result


# Funciones para producir representación intermedia para operadores
def pushID(id, funcion):
    encontro = False
    for keys in simbolos:
        if funcion == keys:
            if simbolos[keys].value is not None:
                for var in simbolos[keys].value:
                    if id == var:
                        encontro = True
                        PilaO.append(id)
                        PTypes.append(simbolos[keys].value[var].type_data)
                        AVAIL.append(simbolos[keys].value[var].value)
    if encontro is False:
        print('ERROR: Variable no declarada.', id)
        sys.exit()


def pushCte(cte):
    PilaO.append(cte)
    tipo = str(type(cte))
    if tipo == "<class 'float'>":
        PTypes.append('float')
    if tipo == "<class 'int'>":
        PTypes.append('int')
    if tipo == "<class 'str'>":
        PTypes.append('string')
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
            PilaO.pop()
            left_type = PTypes.pop()
            AVAIL.pop()
            operator = POper.pop()
            result_type = semantic(left_type, right_type, operator)
            if(result_type != 'error'):
                result = right_value
                quadr = quadruple(len(Quad), operator, right_operand, None, result)
                Quad.append(quadr)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()
    return result


def popTerm():
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
                if(operator == '+'):
                    result = left_value + right_value
                else:
                    result = left_value - right_value
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


def popFact():
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
                if(operator == '*'):
                    result = left_value * right_value
                else:
                    result = left_value / right_value
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


def popRelop():
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
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


def popLog():
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
                if(operator == 'and'):
                    result = left_value and right_value
                else:
                    result = left_value or right_value
                quadr = quadruple(len(Quad), operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
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



def show():
    for i in range(0, len(Quad)):
        print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
