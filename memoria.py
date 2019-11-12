import tabla_master as master
import estructuras
from pprint import pprint
# Diccionario de memoria
memory_dir = None
memoria_global = estructuras.memoria()
memoria_local = estructuras.memoria()
memoria_cte = estructuras.memoria()

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


# para insertar los valores a cualquier direccion local es a traves del metodo updateLocalInMemory
# por lo que se tiene que pasar a la funcion la direccion indicada

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

def reiniciarDireccionesFunc():
    global memoFuncInt
    global memoFuncFloat
    global memoFuncString
    global memoFuncBool
    global memoCteInt
    global memoCteFloat
    global memoCteString
    global memoCteBool
    memoFuncInt = 9000
    memoFuncFloat = 9100
    memoFuncString = 9200
    memoFuncBool = 9300
    memoCteInt = 20000
    memoCteFloat = 21000
    memoCteString = 22000
    memoCteBool = 23000


# Funcion que obtiene el tipo de un cte
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


def getValor(direccion, tipo):
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


# Funcion que asigna las primeras direcciones Globales
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


def getVirtualCte(miTipo):
    global memoCteInt
    global memoCteFloat
    global memoCteString
    global memoFuncBool
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
        temp = memoFuncBool
        memoFuncBool += 1
    return temp


def insertGlobalInToMemory(tipo, memoria):
    if tipo == "int":
        memoria_global.integers[memoria] = None
    if tipo == "float":
        memoria_global.float[memoria] = None
    if tipo == "string":
        memoria_global.string[memoria] = None
    if tipo == "bool":
        memoria_global.booleanos[memoria] = None


def updateGlobalInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_global.integers[direccion] = valor
    if tipo == "float":
        memoria_global.float[direccion] = valor
    if tipo == "string":
        memoria_global.string[direccion] = valor
    if tipo == "bool":
        memoria_global.booleanos[direccion] = valor


def insertLocalInMemory(tipo, memoria):
    if tipo == "int":
        memoria_local.integers[memoria] = None
    if tipo == "float":
        memoria_local.float[memoria] = None
    if tipo == "string":
        memoria_local.string[memoria] = None
    if tipo == "bool":
        memoria_local.booleanos[memoria] = None


def updateLocalInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor


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


def limpiarDireUsadas():
    global memoIntUsada
    global memoFloatUsada
    global memoStringUsada
    global memoBoolUsada
    for i in range(len(memoIntUsada)):
        del memoria_local.integers[memoIntUsada[i]]
    for i in range(len(memoFloatUsada)):
        del memoria_local.float[memoFloatUsada[i]]
    for i in range(len(memoStringUsada)):
        del memoria_local.string[memoStringUsada[i]]
    for i in range(len(memoBoolUsada)):
        del memoria_local.booleanos[memoBoolUsada[i]]
    memoIntUsada.clear()
    memoFloatUsada.clear()
    memoStringUsada.clear()
    memoBoolUsada.clear()


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


################FUNCIONES ANTIGUAS################

def show():
    print("INTEGERS GLOBALS")
    pprint(memoria_global.integers, width=1)
    print("FLOAT GLOBALS")
    pprint(memoria_global.float, width=1)
    print("STRING GLOBALS")
    pprint(memoria_global.string, width=50)
    print("BOOL GLOBALS")
    pprint(memoria_global.booleanos, width=1)

    print("INTEGERS LOCAL")
    pprint(memoria_local.integers, width=1)
    print("FLOAT LOCAL")
    pprint(memoria_local.float, width=1)
    print("STRING LOCAL")
    pprint(memoria_local.string, width=50)
    print("BOOL LOCAL")
    pprint(memoria_local.booleanos, width=1)


# def insertToLocalFunc(id_funcion):
#     for id in master.simbolos[id_funcion].value:
#         tipo = master.simbolos[id_funcion].value[id].type_data
#         value = master.simbolos[id_funcion].value[id].value
#         dir = insertLocal(tipo, True)
#         # show()
#         # print("TIPO:", tipo, "VALOR:", value, "DIR:", dir)
#         master.simbolos[id_funcion].value[id].direccion = dir
#         updateLocalInMemory(value, dir, tipo, True)




def insertLocalTemp(tipo):
    global localTempINT
    global localTempFLOAT
    global localTempSTRING
    global localTempBOOL
    if tipo == "int":
        memoria_cte.integers[localTempINT] = None
        temp = localTempINT
        localTempINT += 1
        return temp
    if tipo == "float":
        memoria_cte.float[localTempFLOAT] = None
        temp = localTempFLOAT
        localTempFLOAT += 1
        return temp
    if tipo == "string":
        memoria_cte.string[localTempSTRING] = None
        temp = localTempSTRING
        localTempSTRING += 1
        return temp
    if tipo == "bool":
        memoria_cte.booleanos[localTempBOOL] = None
        temp = localTempBOOL
        localTempBOOL += 1
        print("INTRODUJO BOOL")
        return temp

def showCteMemo(id):
    print("ID:", id)
    for i in range(len(memoIntUsada)):
        print("Direccion CTE:",memoIntUsada[i], "Valor:", getValor(memoIntUsada[i], "int"))
    for i in range(len(memoFloatUsada)):
        print("Direccion CTE:", memoFloatUsada[i], "Valor:", getValor(memoFloatUsada[i], 'float'))
    for i in range(len(memoStringUsada)):
        print("Direccion CTE:", memoStringUsada[i], "Valor:", getValor(memoStringUsada[i], 'string'))
    for i in range(len(memoBoolUsada)):
        print("Direccion CTE:", memoBoolUsada[i], "Valor:", getValor(memoBoolUsada[i], 'bool'))
    print("")
