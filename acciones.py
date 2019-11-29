# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

from quadruples import Quad
from ast import literal_eval
import memoria as memo
import tabla_master as master
import sys

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


# Función que recibe un valor ingresado por el usuario y
# regresa el tipo de este.
# Es utilizado por miInput para realizar asignación de valores de acuerdo a su tipo.
def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


# Función que recibe un operando y regresa la dirección de que este guarda,
# si es que guarda una.
# Es utilizado por todas las funciones de ejecución de memoria en caso de que
# haya un arreglo dentro de las operaciones
def tieneDireccion(operand):
    operand = str(operand)
    if operand[0] == '(':
        newOp = operand[1:len(operand)-1]
        newOp = int(newOp)
        dir = memo.getValor(newOp, None)
        return dir
    else:
        return int(operand)


# ########################## FUNCIONES DE EJECUCIÓN ##########################

# Función que recibe un cuádruplo y regresa el número de cuádruplo al que
# deberá saltar.
def goto(quadr, i):
    return quadr.result


# Función que recibe un cuádruplo, actualiza el valor obtenido en la dirección
# y regresa el número de cuádruplo al que deberá saltar, en caso de hacerlo.
def gotof(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    value = memo.getValor(left_op, None)
    if value == 'false' or value is False:
        return quadr.result
    else:
        return i + 1


# Función que recibe un cuádruplo, crea la tabla de variables de la función
# llamada y regresa el siguiente número de cuádruplo.
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
            dimension = master.simbolos[quadr.result].value[id].dimensionada
            tipo = master.simbolos[quadr.result].value[id].type_data
            direccion = master.simbolos[quadr.result].value[id].direccion
            matriz = master.simbolos[quadr.result].value[id].matriz
            if master.simbolos[quadr.result].value[id].param:
                dir_param.append(direccion)
                tipo_param.append(tipo)
            if id == 'return':
                dirReturn = direccion
            if not master.simbolos[quadr.result].value[id].param:
                if dimension > 0 and matriz == 0:
                    memo.copyVectorToExe(direccion, dimension, tipo)
                elif dimension > 0 and matriz > 0:
                    tam = matriz * dimension
                    memo.copyVectorToExe(direccion, tam, tipo)
                else:
                    valor = master.simbolos[quadr.result].value[id].value
                    memo.insertLocalInMemory(tipo, direccion)
                    memo.updateLocalInMemory(valor, direccion, tipo)
    return i + 1


# Función que recibe un cuádruplo, actualiza los parámetros de la funcióno
# llamada y regresa el siguiente número de cuádruplo.
def param(quadr, i):
    global dir_param
    global tipo_param
    valor = memo.getValor(quadr.left_operand, None)
    memo.insertLocalInMemory(tipo_param[-1], dir_param[-1])
    memo.updateLocalInMemory(valor, dir_param[-1])
    dir_param.pop()
    tipo_param.pop()
    return i + 1


# Función que recibe un cuádruplo y regresa el número de cuádruplo al que
# deberá saltar, dependiendo de si es recursiva o no.
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


# Función que recibe un cuádruplo, actualiza el valor del return, borra
# el bloque de memoria y regresa el siguiente número de cuádruplo.
def miReturn(quadr, i):
    global funcNo
    global miFunc
    regresa = tieneDireccion(quadr.result)
    valor = memo.getValor(regresa, None)
    memo.insertReturn(valor)
    funcNo.remove(miFunc)
    if funcNo.count(miFunc) <= 0:
        for id in master.simbolos[miFunc].value:
            if id != "PARAMCANTI" and id != "Cuadruplos":
                direccion = master.simbolos[miFunc].value[id].direccion
                matriz = master.simbolos[miFunc].value[id].matriz
                dimension = master.simbolos[miFunc].value[id].dimesion
                tipo = memo.getTipoViaDireccion(direccion)
                if dimension > 0 and matriz == 0:
                    memo.deleteVectoInExe(direccion, dimension, tipo)
                elif dimension > 0 and matriz > 0:
                    tam = dimension * matriz
                    memo.deleteVectoInExe(direccion, tam, tipo)
                else:
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


# Función que recibe un cuádruplo, elimina el bloque de memoria utilizado
# por esa función y regresa el siguiente número de cuádruplo.
def endproc(quadr, i):
    global funcNo
    id_funcion = quadr.result
    funcNo.remove(id_funcion)
    if funcNo.count(id_funcion) <= 0:
        for id in master.simbolos[id_funcion].value:
            if id != "PARAMCANTI" and id != "Cuadruplos":
                dimension = master.simbolos[quadr.result].value[id].dimensionada
                direccion = master.simbolos[id_funcion].value[id].direccion
                matriz = master.simbolos[id_funcion].value[id].matriz
                tipo = memo.getTipoViaDireccion(direccion)
                if dimension > 0 and matriz == 0:
                    memo.deleteVectoInExe(direccion, dimension, tipo)
                elif dimension > 0 and matriz > 0:
                    tam = dimension * matriz
                    memo.deleteVectoInExe(direccion, tam, tipo)
                else:
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


# Función que recibe un cuádruplo, realiza la operación de suma entre
# operandos, actualiza el valor y regresa el siguiente número de cuádruplo.
def plus(quadr, i):
    global esArreglo
    global contVer
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    if right_op == 0:
        esArreglo = True
    if esArreglo:
        res = memo.getValor(left_op, None) + quadr.right_operand
        contVer += 1
    else:
        res = memo.getValor(left_op, None) + memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    if contVer >= 2:
        esArreglo = False
    return i + 1


# Función que recibe un cuádruplo, realiza la operación de resta entre
# operandos, actualiza el valor y regresa el siguiente número de cuádruplo.
def minus(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) - memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


# Función que recibe un cuádruplo, realiza la operación de multiplicación entre
# operandos, actualiza el valor y regresa el siguiente número de cuádruplo.
def mult(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    if right_op < 5000:
        res = memo.getValor(left_op, None) * right_op
    else:
        res = memo.getValor(left_op, None) * memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


# Función que recibe un cuádruplo, realiza la operación de división entre
# operandos, actualiza el valor y regresa el siguiente número de cuádruplo.
def div(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    right_op = tieneDireccion(quadr.right_operand)
    res = memo.getValor(left_op, None) / memo.getValor(right_op, None)
    memo.updateLocalInMemory(res, quadr.result)
    return i + 1


# Función que recibe un cuádruplo, realiza la operación de asignación entre
# operandos, actualiza el valor y regresa el siguiente número de cuádruplo.
def assign(quadr, i):
    left_op = tieneDireccion(quadr.left_operand)
    resDir = tieneDireccion(quadr.result)
    res = memo.getValor(left_op, None)
    memo.updateLocalInMemory(res, resDir)
    return i + 1


# Funciones que reciben un cuádruplo, realizan la operación de comparación
# entre operandos, actualizan el valor y regresan el siguiente número de
# cuádruplo.
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


# Funciones que reciben un cuádruplo, realizan la operación lógica entre
# operandos, actualizan el valor y regresan el siguiente número de cuádruplo.
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


# Función que recibe un cuádruplo, pide un valor al usuario, obtiene su tipo,
# actualiza el valor en memoria y regresa el siguiente número de cuádruplo.
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


# Función que recibe un cuádruplo, muestra el resultado en pantalla y regresa
# el siguiente número de cuádruplo.
def miOutput(quadr, i):
    resDir = tieneDireccion(quadr.result)
    if str(type(memo.getValor(resDir, None))) == "<class 'str'>":
        valor = memo.getValor(resDir, None).replace('"', '')
        print(valor)
    else:
        print(memo.getValor(resDir, None))
    return i + 1


# Función que recibe un cuádruplo, verifica que el operando izquierdo esté
# dentro de los límites del arreglo y regresa el siguiente número de cuádruplo.
def ver(quadr, i):
    global esArreglo
    global contVer
    left_op = tieneDireccion(quadr.left_operand)
    verifica = memo.getValor(left_op, None)
    if verifica >= 0 and verifica <= quadr.result:
        contVer = 0
        return i + 1
    else:
        print("ERROR: Índice fuera de rango.")
        sys.exit()


# Función que recibe un cuádruplo, manda ejecutar una función dependiendo del
# operador y regresa el númro de cuádruplo que recibe de la función.
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


# Función que itera sobre la pila de cuádruplos y manda llamar al switcher para
# ejecutar la máquina virtual.
def inicio():
    i = 0
    while Quad[i].operator != 'end':
        # print(Quad[i].num, Quad[i].operator, Quad[i].left_operand, Quad[i].right_operand, Quad[i].result, sep = '\t')
        i = switcher(Quad[i], i)
    # memo.show()
