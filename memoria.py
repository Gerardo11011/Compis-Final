import tabla_master as master
import estructuras
from pprint import pprint
# Diccionario de memoria
memory_dir = None
memoria_global = estructuras.memoria()
memoria_local = estructuras.memoria()
memoria_cte = estructuras.memoria()
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


# Para insertar los valores a cualquier direccion local es a traves del metodo
# updateLocalInMemor por lo que se tiene que pasar a la funcion la direccion indicada
def insertarFuncInMemoryExe(id_funcion):
    for id in master.simbolos[id_funcion].value:
        if id != "PARAMCANTI":
            tipo = master.simbolos[id_funcion].value[id].type_data
            direccion = master.simbolos[id_funcion].value[id].direccion
            insertLocalInMemory(tipo, direccion)
            valor = master.simbolos[id_funcion].value[id].value
            updateLocalInMemory(valor, direccion, tipo)


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
        # del memoria_local.integers[memoIntUsada[i]]
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
def getValor(direccion, tipo):
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


# Busca el valor de una direccion asociada a un CTE
def getValorCte(tipo, direccion):
    temp = None
    if tipo == 'int':
        temp = memoria_cte.integers.get(direccion)
    elif tipo == 'float':
        temp = memoria_cte.float.get(direccion)
    elif tipo == 'string':
        temp = memoria_cte.string.get(direccion)
    elif tipo == 'bool':
        temp = memoria_cte.booleanos.get(direccion)
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


# Funcion que inserta la direccion global en la memoria
def insertGlobalInToMemory(tipo, memoria):
    if tipo == "int":
        memoria_global.integers[memoria] = None
    if tipo == "float":
        memoria_global.float[memoria] = None
    if tipo == "string":
        memoria_global.string[memoria] = None
    if tipo == "bool":
        memoria_global.booleanos[memoria] = None


# Funcion que actualiza el valor de una direccion global
def updateGlobalInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_global.integers[direccion] = valor
    if tipo == "float":
        memoria_global.float[direccion] = valor
    if tipo == "string":
        memoria_global.string[direccion] = valor
    if tipo == "bool":
        memoria_global.booleanos[direccion] = valor


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
        memoria_global.integers[direccion] = valor
    if tipo == "float":
        memoria_global.float[direccion] = valor
    if tipo == "string":
        memoria_global.string[direccion] = valor
    if tipo == "bool":
        memoria_global.booleanos[direccion] = valor

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
def updateLocalInMemory(valor, direccion, tipo):
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor


# Funcion que actualiza el valor con una CTE de una direccion de memoria CTE
def updateCteInMemory(valor, direccion, tipo):
    # print("valor:", valor, "direccion:", direccion, "tipo:", tipo)
    if tipo == "int":
        memoria_cte.integers[direccion] = valor
    if tipo == "float":
        memoria_cte.float[direccion] = valor
    if tipo == "string":
        memoria_cte.string[direccion] = valor
    if tipo == "bool":
        memoria_cte.booleanos[direccion] = valor


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


# Funcion que verifica si el CTE ya se encuentra en la memoria
def verificarValorCte(cte):
    tipo = getTipo(cte)
    if tipo == 'int':
        if cte in memoria_cte.integers.values():
            return True
    elif tipo == 'float':
        if cte in memoria_cte.float.values():
            return True
    elif tipo == 'string':
        if cte in memoria_cte.string.values():
            return True
    elif tipo == 'bool':
        if cte in memoria_cte.booleanos.values():
            return True


# Funcion que obtiene la direccion de un CTE dado
def getDireCte(cte):
    tipo = getTipo(cte)
    if tipo == 'int':
        for key, value in memoria_cte.integers.items():
            if cte == value:
                return key
    elif tipo == 'float':
        for key, value in memoria_cte.float.items():
            if cte == value:
                return key
    elif tipo == 'string':
        for key, value in memoria_cte.string.items():
            if cte == value:
                return key
    elif tipo == 'bool':
        for key, value in memoria_cte.booleanos.items():
            if cte == value:
                return key
    return "DIRECCION INVALIDA"

################FUNCIONES ANTIGUAS################


# Funcion que imprime las memorias
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


# Funcion que inserta y obtiene una direccion de memoria de los temporales
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


# Funcion que imprime las CTE en la memoria
def showCteMemo():
    print("CTE INTEGERS")
    pprint(memoria_cte.integers, width=1)
    print("CTE FLOAT")
    pprint(memoria_cte.float)
    print("CTE STRING")
    pprint(memoria_cte.string)
    print("CTE BOOL")
    pprint(memoria_cte.booleanos)
