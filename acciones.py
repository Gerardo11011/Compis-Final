# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

from quadruples import Quad
from ast import literal_eval
import memoria as memo
import tabla_master as master

dir_param = []
tipo_param = []
quadNo = None
dirReturn = None
funcNo = []
esPrimera = False
primerQuadNo = None
miFunc = None
esArreglo = False
contVer = 0


# Función para obtener el tipo de un valor ingresado por el usuario.
def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


# Función para saber si un operando guarda una dirección.
def tieneDireccion(operand):
    operand = str(operand)
    if operand[0] == '(':
        newOp = operand[1:len(operand)-1]
        newOp = int(newOp)
        dir = memo.getValor(newOp, None)
        return dir
    else:
        return int(operand)


# Funciones de ejecución.
def goto(quadr, i):
    return quadr.result


def gotof(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    value = memo.getValor(left_op, None)
    if value == 'false' or value is False:
        return quadr.result
    else:
        return i + 1


def era(quadr, i):
    global dir_param
    global tipo_param
    global dirReturn
    global funcNo
    global esPrimera
    global miFunc
    miFunc = quadr.result
    funcNo.append(quadr.result)
    if funcNo.count(quadr.result) == 1:
        esPrimera = True
    for id in master.simbolos[quadr.result].value:
        if id != "PARAMCANTI" and id != 'Cuadruplos':
            tipo = master.simbolos[quadr.result].value[id].type_data
            direccion = master.simbolos[quadr.result].value[id].direccion
            if master.simbolos[quadr.result].value[id].param:
                dir_param.append(direccion)
                tipo_param.append(tipo)
            if id == 'return':
                dirReturn = direccion
            if not master.simbolos[quadr.result].value[id].param:
                valor = master.simbolos[quadr.result].value[id].value
                memo.insertLocalInMemory(tipo, direccion)
                memo.updateLocalInMemory(valor, direccion, tipo)
    return i + 1


def param(quadr, i):
    global dir_param
    global tipo_param
    left_op = tieneDireccion(quadr.left_operand)
    valor = memo.getValor(left_op, None)
    memo.insertLocalInMemory(tipo_param[-1], dir_param[-1])
    memo.updateLocalInMemory(valor, dir_param[-1])
    dir_param.pop()
    tipo_param.pop()
    return i + 1


def gosub(quadr, i):
    global quadNo
    global esPrimera
    global primerQuadNo
    if esPrimera:
        primerQuadNo = i
    else:
        quadNo = i
    esPrimera = False
    return quadr.result


def miReturn(quadr, i):
    global funcNo
    global miFunc
    regresa = tieneDireccion(quadr.left_operand)
    valor = memo.getValor(regresa, None)
    memo.insertReturn(valor)
    funcNo.remove(miFunc)
    if funcNo.count(miFunc) <= 0:
        for id in master.simbolos[miFunc].value:
            if id != "PARAMCANTI" and id != "Cuadruplos":
                direccion = master.simbolos[miFunc].value[id].direccion
                tipo = memo.getTipoViaDireccion(direccion)
                if tipo == "int":
                    memo.memoria_local.integers.pop(direccion)
                if tipo == "float":
                    memo.memoria_local.float.pop(direccion)
                if tipo == "string":
                    memo.memoria_local.string.pop(direccion)
                if tipo == "bool":
                    memo.memoria_local.booleanos.pop(direccion)
        return primerQuadNo + 1
    return quadNo + 1


def endproc(quadr, i):
    global funcNo
    id_funcion = quadr.result
    funcNo.remove(id_funcion)
    if funcNo.count(id_funcion) <= 0:
        for id in master.simbolos[id_funcion].value:
            if id != "PARAMCANTI" and id != "Cuadruplos":
                direccion = master.simbolos[id_funcion].value[id].direccion
                tipo = memo.getTipoViaDireccion(direccion)
                if tipo == "int":
                    memo.memoria_local.integers.pop(direccion)
                if tipo == "float":
                    memo.memoria_local.float.pop(direccion)
                if tipo == "string":
                    memo.memoria_local.string.pop(direccion)
                if tipo == "bool":
                    memo.memoria_local.booleanos.pop(direccion)
        return primerQuadNo + 1
    return quadNo + 1


def plus(quadr, i):
    global esArreglo
    global contVer
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    if esArreglo:
        contVer += 1
        res = memo.getValor(quadr.left_operand, None) + quadr.right_operand
    else:
        res = memo.getValor(left_op, None) + memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    if contVer >= 2:
        esArreglo = False
    return i + 1


def minus(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) - memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def mult(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) * memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def div(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) / memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def assign(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    resDir = tieneDireccion(quadr.result)
    res = memo.getValor(left_op, None)
    memo.updateLocalInMemory(res, resDir)
    return i + 1


def gt(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) > memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def gte(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) >= memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def lt(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) < memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def lte(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) <= memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def equals(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) == memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def ne(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) != memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def andOp(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) and memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def orOp(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) or memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


def miInput(quadr, i):
    resDir = tieneDireccion(quadr.result)
    valor = input()
    tipo = str(get_type(valor))
    if tipo == "<class 'int'>":
        valor = int(valor)
        memo.updateLocalInMemory(valor, resDir)
    elif tipo == "<class 'float'>":
        valor = float(valor)
        memo.updateLocalInMemory(valor, resDir)
    elif tipo == "<class 'str'>":
        valor = str(valor)
        memo.updateLocalInMemory(valor, resDir)
    elif valor == 'true' or valor == 'false':
        memo.updateLocalInMemory(valor, resDir, 'bool')
    return i + 1


def miOutput(quadr, i):
    resDir = tieneDireccion(quadr.result)
    if str(type(memo.getValor(resDir, None))) == "<class 'str'>":
        valor = memo.getValor(resDir, None).replace('"', ' ')
        print(valor)
    else:
        print(memo.getValor(resDir, None))
    return i + 1


def ver(quadr, i):
    global esArreglo
    global contVer
    esArreglo = True
    contVer = 0
    return i + 1


# Switch para ejecutar una función dependiendo del operador del cuádruplo.
def switcher(quadr, i):
    switch = {
        'goto': goto,
        'gotof': gotof,

        'era': era,
        'param': param,
        'endproc': endproc,
        'gosub': gosub,
        'return': miReturn,

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
        'output': miOutput,

        'ver': ver
    }
    func = switch.get(quadr.operator, 'nel')
    if func != 'nel':
        position = func(quadr, i)
        return position
    return i + 1


def inicio():
    i = 0
    while Quad[i].operator != 'end':
        # print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
        i = switcher(Quad[i], i)
    # memo.show()
