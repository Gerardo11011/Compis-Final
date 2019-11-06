import tabla_master as master
import estructuras
from pprint import pprint
# Diccionario de memoria
memory_dir = None
memoria_global = estructuras.memoria()
memoria_local = estructuras.memoria()
# Las direcciones de memoria actuales son:
# 3000 -> 3099 -> INT
# 3100 -> 3199 -> FLOAT
# 3200 -> 3299 -> STRING

MEMORY_SIZE = 100

globalINT = 0
globalFLOAT = 0
globalSTRING = 0
globalBOOL = 0

localINT = 0
localFLOAT = 0
localSTRING = 0
localBOOL = 0

types = ["int", "float", "string", "bool"]


def insertGlobal(tipo):
    global globalINT
    global globalFLOAT
    global globalSTRING
    global globalBOOL
    if tipo == "int":
        memoria_global.integers = {globalINT: None}
        temp = globalINT
        globalINT += 1
        return temp
    if tipo == "float":
        memoria_global.float = {globalFLOAT: None}
        temp = globalFLOAT
        globalFLOAT += 1
        return temp
    if tipo == "string":
        memoria_global.string = {globalSTRING: None}
        temp = globalSTRING
        globalSTRING += 1
        return temp
    if tipo == "bool":
        memoria_global.booleanos = {globalBOOL: None}
        temp = globalBOOL
        globalBOOL += 1
        return temp


def updateGlobal(valor, direccion, tipo):
    if tipo == "int":
        memoria_global.integers[direccion] = valor
    if tipo == "float":
        memoria_global.float[direccion] = valor
    if tipo == "string":
        memoria_global.string[direccion] = valor
    if tipo == "bool":
        memoria_global.booleanos[direccion] = valor


def insertLocal(tipo):
    global localINT
    global localFLOAT
    global localSTRING
    global localBOOL
    if tipo == "int":
        memoria_local.integers = {localINT: None}
        temp = localINT
        localINT += 1
        return temp
    if tipo == "float":
        memoria_local.float = {localFLOAT: None}
        temp = localFLOAT
        localFLOAT += 1
        return temp
    if tipo == "string":
        memoria_local.string = {localSTRING: None}
        temp = localSTRING
        localSTRING += 1
        return temp
    if tipo == "bool":
        memoria_local.booleanos = {localBOOL: None}
        temp = localBOOL
        localBOOL += 1
        return temp


def updateLocal(valor, direccion, tipo):
    if tipo == "int":
        memoria_local.integers[direccion] = valor
    if tipo == "float":
        memoria_local.float[direccion] = valor
    if tipo == "string":
        memoria_local.string[direccion] = valor
    if tipo == "bool":
        memoria_local.booleanos[direccion] = valor


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
