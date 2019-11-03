# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
import estructuras as tabla

# Tabla de simbolos y arreglo con id de funciones
simbolos = {}
funciones = []

# Declaración de variables globales
miTipo = None
miID = None
miValor = None
miIdFunciones = None
esFuncion = False
esMain = False


# Funcion que inicializa la tabla con funciones, global, y main
def insert(id, type_data):
    temp = tabla.tabla_local(type_data, {})
    if len(simbolos) >= 1 and not itFoundIdFunc(id):
        simbolos[id] = temp
    if not simbolos:
        simbolos[id] = temp


# Funcion que revisa que no haya dos funciones con el mismo nombre
def itFoundIdFunc(id):
    for Keys in simbolos:
        if id == Keys:
            print("Id de funcion declarado previamente:", id)
            sys.exit()
            return True
    return False


# Funcion que valida si no hay una variable global con el mismo id ya definido
def itFoundGlobalVar(id):
    for keys in simbolos["global"].value:
        if id == keys:
            print("Variable global con el mismo ID:", id)
            sys.exit()
            return True
    return False


# Funcion que comprueba que no se puedan volver a declarar dos variables con el mismo ID
def itFoundLocal(id, id_funcion):
    aux = False
    if id in simbolos[id_funcion].value:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


# Funcion que valida que el valor ingresado y el tipo de la variable sean iguales
def validate(dato, id, id_funcion):
    temp = str(type(dato))
    aux = None
    encontro = False
    if id in simbolos[id_funcion].value:
        aux = simbolos[id_funcion].value[id].type_data
        encontro = True
    if not encontro:
        print('ERROR: ID no declarado:', id)
        sys.exit()
    if temp == "<class 'float'>" and aux == 'float':
        return True
    if temp == "<class 'int'>" and aux == 'int':
        return True
    if temp == "<class 'str'>" and aux == 'string':
        return True
    else:
        print("ERROR: Dato no válido.")
        sys.exit()


# Funcion que inserta las variables en su respectiva tabla local
def insertIdToFunc(id, type_data, id_funcion):
    if len(simbolos[id_funcion].value) >= 1 and not itFoundGlobalVar(id) and not itFoundLocal(id, id_funcion):
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None)
    if len(simbolos[id_funcion].value) == 0 and not itFoundGlobalVar(id):
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None)


# Funcion que actualiza el valor de una variable
def updateIdInFunc(id, id_funcion, valor):
    if validate(valor, id, id_funcion):
        simbolos[id_funcion].value[id].value = valor


# Funcion que imprime la tabla master
def show():
    for keys in simbolos:
        print("ID FUNCION:", keys, " TYPE DATA:", simbolos[keys].type_data)
        for id in simbolos[keys].value:
            print("ID:", id)
            print("VALOR:", simbolos[keys].value[id].value, " TYPE DATA:", simbolos[keys].value[id].type_data)
        print("")
