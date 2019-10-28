# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import sys

from tabla_master import simbolos_master
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
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result


# Funciones operadores
def pushID(id):
    for keys in simbolos_master:
        if id == keys:
            PilaO.append(id)
            PTypes.append(simbolos_master[keys].type_data)
            AVAIL.append(simbolos_master[keys].value)


def pushPoper(operator):
    POper.append(operator)


def popTerm():
    if len(POper) > 0:
        if POper[len(POper)-1] == '+' or POper[len(POper)-1] == '-':
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
                quadr = quadruple(operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


def popFact():
    if len(POper) > 0:
        if POper[len(POper)-1] == '*' or POper[len(POper)-1] == '/':
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
                quadr = quadruple(operator, left_operand, right_operand, result)
                Quad.append(quadr)
                PilaO.append(result)
                AVAIL.append(result)
                PTypes.append(result_type)
            else:
                print("ERROR: Type mismatch.")
                sys.exit()


# Funciones para producir representación intermedia para If Else
def fill(cuadruplo, salto):
    Quad[cuadruplo].result = salto


def ifelseUno():
    exp_type = PTypes.pop()
    if exp_type == "bool":
        result = PilaO.pop()
        quadr = quadruple("gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR: Type mismatch.")
        sys.exit()


def ifelseDos():
    end = PJumps.pop()
    fill(end, len(Quad))


def ifelseTres():
    quadr = quadruple("goto", None, None, None)
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
        quadr = quadruple("gotof", result, None, None)
        Quad.append(quadr)
        PJumps.append(len(Quad)-1)
    else:
        print("ERROR: Type mismatch.")
        sys.exit()


def loopTres():
    end = PJumps.pop()
    regresa = PJumps.pop()
    quadr = quadruple("goto", None, None, regresa)
    Quad.append(quadr)
    fill(end, len(Quad))


def show():
    for i in range(0, len(Quad)):
        print(Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
