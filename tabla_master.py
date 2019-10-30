# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
import vars_table as tabla
import pprint
# Tabla de simbolos
simbolos = {}

# Declaración de variables globales
miTipo = None
miID = None
miValor = None
miIdFunciones = None
esFuncion = False
esMain = False
esGlobal = False


# Funciones para modificar la tabla
def insert(id, type_data):
    temp = tabla.tabla_local(type_data, {})
    if len(simbolos) >= 1 and not itFoundGlobal(id):
        simbolos[id] = temp
    if not simbolos:
        simbolos[id] = temp


def update(id, value):
    if validate(value, id):
        simbolos[id].value = value


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


def itFound(id, id_funcion):
    aux = False
    if id in simbolos[id_funcion].value:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def insertFuncToMaster(id, type_data, id_funcion):
    if len(simbolos[id_funcion].value) >= 1 and not itFound(id, id_funcion):
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None)
    if len(simbolos[id_funcion].value) == 0:
        simbolos[id_funcion].value[id] = tabla.tabla_local(type_data, None)


def updateFuncToMaster(id, id_funcion, valor):
    if validate(valor, id, id_funcion):
        simbolos[id_funcion].value[id].value = valor


def show():
    for keys in simbolos:
        if keys == "judas":
            print("ID FUNCION: ", keys, " TYPE DATA: ", simbolos[keys].type_data)
            for id in simbolos[keys].value:
                print("ID: ", id)
                print("VALOR: ", simbolos[keys].value[id].value, " TYPE DATA: ", simbolos[keys].value[id].type_data)
            print("")
        elif keys == "simon":
            print("ID FUNCION: ", keys, " TYPE DATA: ", simbolos[keys].type_data)
            for id in simbolos[keys].value:
                print("ID: ", id)
                print("VALOR: ", simbolos[keys].value[id].value, " TYPE DATA: ", simbolos[keys].value[id].type_data)
            print("")
        elif keys == "oscar":
            print("ID FUNCION: ", keys, " TYPE DATA: ", simbolos[keys].type_data)
            for id in simbolos[keys].value:
                print("ID: ", id)
                print("VALOR: ", simbolos[keys].value[id].value, " TYPE DATA: ", simbolos[keys].value[id].type_data)
            print("")
        elif keys == "main":
            print("ID main: ", keys, " TYPE DATA: ", simbolos[keys].type_data)
            for id in simbolos[keys].value:
                print("ID: ", id)
                print("VALOR: ", simbolos[keys].value[id].value, " TYPE DATA: ", simbolos[keys].value[id].type_data)
            print("")
        else:
            print("ID: ", keys)
            for id in simbolos[keys].value:
                print("ID: ", id)
                print("VALOR: ", simbolos[keys].value[id].value, " TYPE DATA: ", simbolos[keys].value[id].type_data)
            print("")


def insertarMaster(id, objeto):
    for keys in simbolos:
        if keys == id:
            simbolos[keys].value = objeto


def itFoundGlobal(id):
    for Keys in simbolos:
        if id == Keys:
            return True
    return False
