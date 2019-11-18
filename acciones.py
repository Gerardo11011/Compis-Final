# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

from quadruples import Quad
from ast import literal_eval
import memoria as memo


# Función para obtener el tipo de un valor ingresado por el usuario.
def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


# Funciones de ejecución.
def goto(quadr, i):
    return quadr.result


def gotof(quadr, i):
    value = memo.getValor(quadr.left_operand, None)
    if value == 'false' or value is False:
        return quadr.result
    else:
        return i + 1


def plus(quadr, i):
    res = memo.getValor(quadr.left_operand, None) + memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def minus(quadr, i):
    res = memo.getValor(quadr.left_operand, None) - memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def mult(quadr, i):
    res = memo.getValor(quadr.left_operand, None) * memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def div(quadr, i):
    res = memo.getValor(quadr.left_operand, None) / memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def assign(quadr, i):
    res = memo.getValor(quadr.left_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def gt(quadr, i):
    res = memo.getValor(quadr.left_operand, None) > memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def gte(quadr, i):
    res = memo.getValor(quadr.left_operand, None) >= memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def lt(quadr, i):
    res = memo.getValor(quadr.left_operand, None) < memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def lte(quadr, i):
    res = memo.getValor(quadr.left_operand, None) <= memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def equals(quadr, i):
    res = memo.getValor(quadr.left_operand, None) == memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def ne(quadr, i):
    res = memo.getValor(quadr.left_operand, None) != memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def andOp(quadr, i):
    res = memo.getValor(quadr.left_operand, None) and memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def orOp(quadr, i):
    res = memo.getValor(quadr.left_operand, None) or memo.getValor(quadr.right_operand, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def miInput(quadr, i):
    valor = input()
    tipo = str(get_type(valor))
    if tipo == "<class 'int'>":
        valor = int(valor)
        memo.updateLocalInMemory(valor, quadr.result)
    elif tipo == "<class 'float'>":
        valor = float(valor)
        memo.updateLocalInMemory(valor, quadr.result)
    elif tipo == "<class 'str'>":
        valor = str(valor)
        memo.updateLocalInMemory(valor, quadr.result)
    elif valor == 'true' or valor == 'false':
        memo.updateLocalInMemory(valor, quadr.result, 'bool')
    return i + 1


def miOutput(quadr, i):
    print(memo.getValor(quadr.result, None))
    return i + 1


# Switch para ejecutar una función dependiendo del operador del cuádruplo.
def switcher(quadr, i):
    switch = {
        'goto': goto,
        'gotof': gotof,

        'era': "era",
        'param': "param",
        'gosub': "gosub",
        'endproc': "endproc",

        '+': plus,
        '-': minus,
        '*': mult,
        '/': div,
        '=': assign,

        '>': gt,
        '>=': gte,
        '<': lt,
        '<=': lte,
        '==': equals,
        '<>': ne,

        'and': andOp,
        'or': orOp,

        'input': miInput,
        'output': miOutput
    }
    func = switch.get(quadr.operator)
    position = func(quadr, i)
    return position


def inicio():
    i = 0
    while Quad[i].operator != 'end':
        # print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
        i = switcher(Quad[i], i)


# def inicio():
#     while Quad[i].operator != 'end':
#         if Quad[i].operator == '*':
#             mult(Quad[i])
#         if Quad[i].operator == '/':
#             div(Quad[i])
#         if Quad[i].operator == '+':
#             plus(Quad[i])
#         if Quad[i].operator == '-':
#             minus(Quad[i])
#         if Quad[i].operator == '>':
#             gt(Quad[i])
#         if Quad[i].operator == '>=':
#             gte(Quad[i])
#         if Quad[i].operator == '<':
#             lt(Quad[i])
#         if Quad[i].operator == '<=':
#             lte(Quad[i])
#         if Quad[i].operator == '==':
#             equals(Quad[i])
#         if Quad[i].operator == '<>':
#             ne(Quad[i])
#         if Quad[i].operator == 'and':
#             andOp(Quad[i])
#         if Quad[i].operator == 'or':
#             orOp(Quad[i])
#         if Quad[i].operator == '=':
#             assign(Quad[i])
