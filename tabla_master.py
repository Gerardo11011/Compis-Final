# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
import estructuras as tabla
import memoria as memo

# Tabla de símbolos y arreglos con id de funciones.
simbolos = {}
funciones = []
arrParam = []

# Declaración de variables globales.
miTipo = None
miTipoAux = None
miID = None
miValor = None
miIdFunciones = None
esFuncion = False
esMain = False
esGlobal = False
prueba = None
returnValor = None
miParamFunc = None
esParam = False
miFuncType = None
contadorParam = 0
contadorDatosPasados = 0
esVector = None
tamaVec = 0
esVoid = False


# Función que inicializa la tabla con funciones, global, y main.
def insert(id, type_data):
    temp = tabla.tabla_local(type_data, {})
    if len(simbolos) >= 1 and not itFoundIdFunc(id):
        simbolos[id] = temp
    if not simbolos:
        simbolos[id] = temp


# Función que revisa que no haya dos funciones con el mismo nombre.
def itFoundIdFunc(id):
    for Keys in simbolos:
        if id == Keys:
            print("Id de funcion declarado previamente:", id)
            sys.exit()
            return True
    return False


# Función que valida si no hay una variable global con el mismo id ya definido.
def itFoundGlobalVar(id):
    if "global" in simbolos.keys():
        for keys in simbolos["global"].value:
            if id == keys:
                print("Variable global con el mismo ID:", id)
                sys.exit()
                return True
        return False


# Función que comprueba que no se puedan volver a declarar dos variables
# con el mismo ID.
def itFoundLocal(id, id_funcion):
    aux = False
    if id in simbolos[id_funcion].value:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def volverFloat(dato, id, id_funcion):
    temp = str(type(dato))
    if simbolos[id_funcion].value[id].type_data == 'float' and temp == "<class 'int'>":
        temp = "<class 'float'>"
    return temp


# Función que valida que el valor ingresado y el tipo de la variable
# sean iguales.
def validate(dato, id, id_funcion):
    temp = volverFloat(dato, id, id_funcion)
    aux = None
    encontroLocal = False
    encontroGlobal = False
    if id in simbolos[id_funcion].value:
        aux = simbolos[id_funcion].value[id].type_data
        encontroLocal = True
    if "global" in simbolos.keys():
        if id in simbolos["global"].value:
            aux = simbolos["global"].value[id].type_data
            encontroGlobal = True
    if not encontroLocal and not encontroGlobal:
        print('ERROR: ID no declarado:', id)
        sys.exit()

    if dato == 'true' or dato == 'false':
        temp = "<class 'bool'>"
    if temp == "<class 'float'>" and aux == 'float':
        return True
    if temp == "<class 'int'>" and aux == 'int':
        return True
    if temp == "<class 'str'>" and aux == 'string':
        return True
    if temp == "<class 'bool'>" and aux == 'bool':
        return True
    if temp == None:
        print(id, "No tiene valor asignado")
        sys.exit()
    else:
        print("ERROR: Dato no válido. validate", dato, id, id_funcion)
        sys.exit()


# Función que inserta las variables en su respectiva tabla local.
def insertIdToFunc(id, type_data, id_funcion, direccion, param=None, dimensionada=0):
    if len(simbolos[id_funcion].value) >= 1 and not itFoundGlobalVar(id) and not itFoundLocal(id, id_funcion):
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None, direccion, param, dimensionada)
    if len(simbolos[id_funcion].value) == 0 and not itFoundGlobalVar(id):
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None, direccion, param, dimensionada)


# Función que actualiza el valor de una variable.
def updateIdInFunc(id, id_funcion, valor):
    if validate(valor, id, id_funcion):
        temp = str(type(valor))
        if temp == "<class 'str'>":
            # valor = valor.replace('"', '')
            simbolos[id_funcion].value[id].value = valor
        else:
            simbolos[id_funcion].value[id].value = valor


# Función que actualiza el valor de una variable.
def getDireccion(id, id_funcion):
    dir = simbolos[id_funcion].value[id].direccion
    return dir

# Función que obtiene el tipo de una variable dentro de una función.
def getType(id, id_funcion):
    type = simbolos[id_funcion].value[id].type_data
    return type


# Función que obtiene el valor de una variable dentro de una función.
def getValor(id, id_funcion):
    valor = simbolos[id_funcion].value[id].value
    return valor


# Función que retorna una lista con las variables que son parámetros
# dentro de la función.
def getidParam(id_funcion):
    temp = []
    for id in simbolos[id_funcion].value:
        if simbolos[id_funcion].value[id].param:
            temp.append(id)
    return temp


# Función que imprime la tabla master.
def show():
    for keys in simbolos:
        print("ID FUNCION:", keys, " TYPE DATA:", simbolos[keys].type_data)
        for id in simbolos[keys].value:
            print("id:", id)
            print("valor:", simbolos[keys].value[id].value, " type data:", simbolos[keys].value[id].type_data, " MEMORIA:", simbolos[keys].value[id].direccion, "TAMA VECT", simbolos[keys].value[id].dimensionada)
        print("")


# Función que retorna el valor de una variable si esta se encuentra declara,
# en caso contrario regresa el id.
def returnValue(id, id_funcion):
    if id in simbolos[id_funcion].value.keys():
        temp = simbolos[id_funcion].value[id].value
        return temp
    else:
        return id


# Función que verifica si la variable ya ha sido previamente declarada
# como global.
def isVarGlobal(id):
    if "global" in simbolos:
        if id in simbolos["global"].value:
            return True
        else:
            return False
    else:
        return False
