# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import tabla_master as master
import estructuras
from pprint import pprint
# Diccionario de memoria
memory_dir = None
memoria_local = estructuras.memoria()
memoria_temp = estructuras.memoria()

# contadores de direcciones de memoria
memoIntUsada = []
memoFloatUsada = []
memoStringUsada = []
memoBoolUsada = []

# direccion de memorias globales
globalINT = 5000
globalFLOAT = 5100
globalSTRING = 5200
globalBOOL = 5300

# direccion de memorias temporales
memoTempInt = 43000
memoTempFloat = 43100
memoTempString = 43200
memoTempBool = 43300

# direccion de memorias de las constantes
memoCteInt = 20000
memoCteFloat = 21000
memoCteString = 22000
memoCteBool = 23000

# Direccion de memoria de las funciones
memoFuncInt = 9000
memoFuncFloat = 9100
memoFuncString = 9200
memoFuncBool = 9300

# Direccion de memoria del main
memoMainInt = 8000
memoMainFloat = 8100
memoMainString = 8200
memoMainBool = 8300

# Direccion temporal del main
tempMainInt = 85000
tempMainFloat = 86000
tempMainString = 87000
tempMainBool = 88000

# Direccion del return
memoReturn = 150000


def getDirecVectorMain(tipo, salto):
    global memoMainInt
    global memoMainFloat
    global memoMainString
    global memoMainBool
    if tipo == 'int':
        temp = memoMainInt
        memoMainInt += salto
    elif tipo == 'float':
        temp = memoMainFloat
        memoMainFloat += salto
    elif tipo == 'string':
        temp = memoMainString
        memoMainString += salto
    elif tipo == 'bool':
        temp = memoMainBool
        memoMainBool += salto
    return temp


def getDirecVectorFunc(miTipo, salto):
    global memoFuncInt
    global memoFuncFloat
    global memoFuncString
    global memoFuncBool
    if miTipo == 'int':
        temp = memoFuncInt
        memoFuncInt += salto
    elif miTipo == 'float':
        temp = memoFuncFloat
        memoFuncFloat += salto
    elif miTipo == 'string':
        temp = memoFuncString
        memoFuncString += salto
    elif miTipo == 'bool':
        temp = memoFuncBool
        memoFuncBool += salto
    return temp


def getDirecVecorGlobal(miTipo, salto):
    global globalINT
    global globalFLOAT
    global globalSTRING
    global globalBOOL
    if miTipo == 'int':
        temp = globalINT
        globalINT += salto
    elif miTipo == 'float':
        temp = globalFLOAT
        globalFLOAT += salto
    elif miTipo == 'string':
        temp = globalSTRING
        globalSTRING += salto
    elif miTipo == 'bool':
        temp = globalBOOL
        globalBOOL += salto
    return temp


def inicInMemory(id, Tipo, id_funcion, direccion=None):
    if Tipo == 'int':
        master.updateIdInFunc(id, id_funcion, 0)
        memoria_local.integers[direccion] = 0
    elif Tipo == 'float':
        master.updateIdInFunc(id, id_funcion, 0.0)
        memoria_local.float[direccion] = 0.0
    elif Tipo == 'string':
        master.updateIdInFunc(id, id_funcion, "")
        memoria_local.string[direccion] = ""
    elif Tipo == 'bool':
        master.updateIdInFunc(id, id_funcion, 'false')
        memoria_local.booleanos[direccion] = False


def copyVectorToExe(direccion, dimesion, tipo):
    if tipo == "int":
        for i in range(dimesion):
            memoria_local.integers[direccion + i] = 0
    if tipo == "float":
        for i in range(dimesion):
            memoria_local.float[direccion + i] = 0.0
    if tipo == "string":
        for i in range(dimesion):
            memoria_local.string[direccion + i] = ""
    if tipo == "bool":
        for i in range(dimesion):
            memoria_local.booleanos[direccion + i] = False


def getVirtualTemp(tipo):
    global memoTempInt
    global memoTempFloat
    global memoTempString
    global memoTempBool
    if tipo == 'int':
        temp = memoTempInt
        memoTempInt += 1
    elif tipo == 'float':
        temp = memoTempFloat
        memoTempFloat += 1
    elif tipo == 'string':
        temp = memoTempString
        memoTempString += 1
    elif tipo == 'bool':
        temp = memoTempBool
        memoTempBool += 1
    return temp


def getVirtualMainTemp(tipo):
    global tempMainInt
    global tempMainFloat
    global tempMainString
    global tempMainBool
    if tipo == 'int':
        temp = tempMainInt
        tempMainInt += 1
    elif tipo == 'float':
        temp = tempMainFloat
        tempMainFloat += 1
    elif tipo == 'string':
        temp = tempMainString
        tempMainString += 1
    elif tipo == 'bool':
        temp = tempMainBool
        tempMainBool += 1
    return temp


def reiniciarTemporales():
    global memoTempInt
    global memoTempFloat
    global memoTempString
    global memoTempBool
    memoTempInt = 43000
    memoTempFloat = 43100
    memoTempString = 43200
    memoTempBool = 43300
    memoria_temp.reiniciar()


def reiniciarDireccionesFunc():
    global memoFuncInt
    global memoFuncFloat
    global memoFuncString
    global memoFuncBool
    memoFuncInt = 9000
    memoFuncFloat = 9100
    memoFuncString = 9200
    memoFuncBool = 9300


# Funcion que elimina las direcciones asociadas
def limpiarDireUsadas():
    global memoIntUsada
    global memoFloatUsada
    global memoStringUsada
    global memoBoolUsada
    for i in range(len(memoIntUsada)):
        memoria_local.integers.pop(memoIntUsada[i], None)
    for i in range(len(memoFloatUsada)):
        memoria_local.float.pop(memoFloatUsada[i], None)
    for i in range(len(memoStringUsada)):
        memoria_local.string.pop(memoStringUsada[i], None)
    for i in range(len(memoBoolUsada)):
        memoria_local.booleanos.pop(memoBoolUsada[i], None)
    memoIntUsada.clear()
    memoFloatUsada.clear()
    memoStringUsada.clear()
    memoBoolUsada.clear()


# Funcion que obtiene elipo de un cte
def getTipo(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        temp = 'bool'
        return temp
    if tipo == "<class 'float'>":
        temp = 'float'
        return temp
    if tipo == "<class 'int'>":
        temp = 'int'
        return temp
    if tipo == "<class 'str'>":
        temp = 'string'
        return temp


# Busca el valor de una direccion asociada
def getValor(direccion, tipo=None):
    temp = None
    if direccion == 15000:
        temp = memoria_local.returns
        return temp
    if tipo is None:
        tipo = getTipoViaDireccion(direccion)
    if tipo == 'int':
        temp = memoria_local.integers[direccion]
    elif tipo == 'float':
        temp = memoria_local.float[direccion]
    elif tipo == 'string':
        temp = memoria_local.string[direccion]
    elif tipo == 'bool':
        temp = memoria_local.booleanos[direccion]
    return temp


# Busca el valor de una direccion asociada a un CTE
def getValorCte(tipo, direccion):
    temp = None
    if tipo == 'int':
        temp = memoria_local.integers.get(direccion)
    elif tipo == 'float':
        temp = memoria_local.float.get(direccion)
    elif tipo == 'string':
        temp = memoria_local.string.get(direccion)
    elif tipo == 'bool':
        temp = memoria_local.booleanos.get(direccion)
    return temp


# Funcion que asigna las primeras direcciones Locales
def getVirtualDicLocal(miTipo):
    global memoFuncInt
    global memoFuncFloat
    global memoFuncString
    global memoFuncBool
    if miTipo == 'int':
        temp = memoFuncInt
        memoFuncInt += 1
    elif miTipo == 'float':
        temp = memoFuncFloat
        memoFuncFloat += 1
    elif miTipo == 'string':
        temp = memoFuncString
        memoFuncString += 1
    elif miTipo == 'bool':
        temp = memoFuncBool
        memoFuncBool += 1
    return temp


# Funcion que asigna las direcciones Globales
def getVirtualDicGlobal(miTipo):
    global globalINT
    global globalFLOAT
    global globalSTRING
    global globalBOOL
    if miTipo == 'int':
        temp = globalINT
        globalINT += 1
    elif miTipo == 'float':
        temp = globalFLOAT
        globalFLOAT += 1
    elif miTipo == 'string':
        temp = globalSTRING
        globalSTRING += 1
    elif miTipo == 'bool':
        temp = globalBOOL
        globalBOOL += 1
    return temp


# Funcion que asigna las direcciones CTE
def getVirtualCte(miTipo):
    global memoCteInt
    global memoCteFloat
    global memoCteString
    global memoCteBool
    if miTipo == 'int':
        temp = memoCteInt
        memoCteInt += 1
    elif miTipo == 'float':
        temp = memoCteFloat
        memoCteFloat += 1
    elif miTipo == 'string':
        temp = memoCteString
        memoCteString += 1
    elif miTipo == 'bool':
        temp = memoCteBool
        memoCteBool += 1
    return temp


# Funcion que asigna las direcciones en el main
def getVirtualDicMain(miTipo):
    global memoMainInt
    global memoMainFloat
    global memoMainString
    global memoMainBool
    if miTipo == 'int':
        temp = memoMainInt
        memoMainInt += 1
    elif miTipo == 'float':
        temp = memoMainFloat
        memoMainFloat += 1
    elif miTipo == 'string':
        temp = memoMainString
        memoMainString += 1
    elif miTipo == 'bool':
        temp = memoMainBool
        memoMainBool += 1
    return temp


# Funcion que actualiza el valor de una direccion temporal
def updateTempInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_temp.integers[direccion] = valor
    if tipo == "float":
        memoria_temp.float[direccion] = valor
    if tipo == "string":
        memoria_temp.string[direccion] = valor
    if tipo == "bool":
        memoria_temp.booleanos[direccion] = valor


# Funcion que actualiza el valor de una direccion temporal del main
def updateMainTempInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor


# Funcion que inserta una direccion de memoria local en la memoria
def insertLocalInMemory(tipo, memoria):
    if tipo == "int":
        memoria_local.integers[memoria] = None
    if tipo == "float":
        memoria_local.float[memoria] = None
    if tipo == "string":
        memoria_local.string[memoria] = None
    if tipo == "bool":
        memoria_local.booleanos[memoria] = None


# Funcion que actualiza el valor de una direccion de memoria local
def updateLocalInMemory(valor, direccion, tipo=None):
    if tipo is None:
        tipo = getTipo(valor)
    if valor is True:
        memoria_local.booleanos[direccion] = 'true'
        return
    if valor is False:
        memoria_local.booleanos[direccion] = 'false'
        return
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor


# Funcion que actualiza el valor con una CTE de una direccion de memoria CTE
def updateCteInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor


# Funcion que guarda lass direcciones usadas por las CTE
def guardarDireUsada(cte, direccion):
    global memoIntUsada
    global memoFloatUsada
    global memoStringUsada
    global memoBoolUsada
    tipo = getTipo(cte)
    if tipo == "int":
        memoIntUsada.append(direccion)
    if tipo == "float":
        memoFloatUsada.append(direccion)
    if tipo == "string":
        memoStringUsada.append(direccion)
    if tipo == "bool":
        memoBoolUsada.append(direccion)


# Funcion que verifica si el CTE ya se encuentra en la memoria
def verificarValorCte(cte):
    tipo = getTipo(cte)
    if tipo == "int" and cte in memoria_local.integers.values():
        return True
    elif tipo == "float" and cte in memoria_local.float.values():
        return True
    elif tipo == "string" and cte in memoria_local.string.values():
        return True
    elif tipo == "bool" and cte in memoria_local.booleanos.values():
        return True
    else:
        return False


# Funcion que obtiene la direccion de un CTE dado
def getDireCte(cte):
    tipo = getTipo(cte)
    if tipo == 'int':
        for key, value in memoria_local.integers.items():
            if cte == value:
                return key
    elif tipo == 'float':
        for key, value in memoria_local.float.items():
            if cte == value:
                return key
    elif tipo == 'string':
        for key, value in memoria_local.string.items():
            if cte == value:
                return key
    elif tipo == 'bool':
        for key, value in memoria_local.booleanos.items():
            if cte == value:
                return key
    return "DIRECCION INVALIDA"

# ###############FUNCIONES ANTIGUAS################


# Funcion que imprime las memorias
def show():
    print("INTEGERS LOCAL")
    pprint(memoria_local.integers, width=1)
    print("FLOAT LOCAL")
    pprint(memoria_local.float, width=1)
    print("STRING LOCAL")
    pprint(memoria_local.string, width=50)
    print("BOOL LOCAL")
    pprint(memoria_local.booleanos, width=1)


def showTemps():
    print("TEMPORALES FUNCIONES")
    print("integers")
    pprint(memoria_temp.integers, width=1)
    print("float")
    pprint(memoria_temp.float, width=1)
    print("string")
    pprint(memoria_temp.string)
    print("booleanos")
    pprint(memoria_temp.booleanos)


def getTipoViaDireccion(direccion):
    if (direccion >= 20000 and direccion < 21000) or (direccion >= 9000 and direccion < 9100) or (direccion >= 20000 and direccion < 21000) or (direccion >= 5000 and direccion < 5100) or (direccion >= 85000 and direccion < 86000) or (direccion >= 43000 and direccion < 43100) or (direccion >= 8000 and direccion < 8100):
        tipo = "int"
        return tipo
    elif (direccion >= 21000 and direccion < 22000) or (direccion >= 9100 and direccion < 9200) or (direccion >= 21000 and direccion < 22000) or (direccion >= 5100 and direccion < 5200) or (direccion >= 86000 and direccion < 87000) or (direccion >= 43100 and direccion < 43200) or (direccion >= 8100 and direccion < 8200):
        tipo = "float"
        return tipo
    elif (direccion >= 22000 and direccion < 23000) or (direccion >= 9200 and direccion < 9300) or (direccion >= 22000 and direccion < 23000) or (direccion >= 5200 and direccion < 5300) or (direccion >= 87000 and direccion < 88000) or (direccion >= 43200 and direccion < 43300) or (direccion >= 8200 and direccion < 8300):
        tipo = "string"
        return tipo
    else:
        tipo = "bool"
        return tipo


def insertReturn(valor):
    global memoReturn
    memoria_local.booleanos[memoReturn] = valor


def getReturn():
    global memoReturn
    memoria_local.booleanos[memoReturn]


# Funcion que elimina todas las direcciones de un vector en memoria de ejecucion
def deleteVectoInExe(direccion, salto, tipo):
    if tipo == "int":
        for i in range(salto):
            memoria_local.integers.pop(direccion + i)
    if tipo == "float":
        for i in range(salto):
            memoria_local.float.pop(direccion + i)
    if tipo == "string":
        for i in range(salto):
            memoria_local.string.pop(direccion + i)
    if tipo == "bool":
        for i in range(salto):
            memoria_local.booleanos.pop(direccion + i)
