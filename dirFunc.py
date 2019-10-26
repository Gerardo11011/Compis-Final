# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
import pprint
# import tabla_master as master
import vars_table as tabla
from tabla_master import simbolos

# Tabla de funciones
funciones = {}
temp_id = []
prueba = []

# Declaración de variables globales
miTipo_f = None
miID_f = None
miValor_f = None
miIdFunciones = None

# Funciones para modificar la tabla


def insert(id, type_data, id_funcion):
    temp = tabla.tabla_funciones(type_data, None, id_funcion)
    if len(funciones) >= 1 and not itFound(id):
        funciones[id] = temp
    if len(funciones) == 0:
        funciones[id] = temp


def updateIDFuncion(id, id_funcion):
    funciones[id].id_funcion = id_funcion


def update(id, value, id_funcion):
    if validate(value, id):
        funciones[id].value = value


def validate(dato, id):
    temp = str(type(dato))
    aux = None
    encontro = False
    if id in funciones:
        aux = funciones[id].type_data
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
        print("ERROR: Dato no válido funcion.")
        sys.exit()


def itFound(id):
    aux = False
    if id in funciones:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def show():
    print("AQUI EMPIEZAN LAS VARIABLES DE LAS FUNCIONES")
    for keys in funciones:
        print("ID: ", keys)
        print("VALOR: ", funciones[keys].value, " TYPE DATA: ", funciones[keys].type_data, " ID FUNCION: ", funciones[keys].id_funcion)
        print("")


def imp():
    print("NOMBRE DE LAS FUNCIONES: ")
    pprint.pprint(simbolos)


def insertarMaster():
    temp = next(iter(funciones))
    aux = funciones[temp].id_funcion
    for keys in funciones:
        if funciones[keys].id_funcion == aux:
            obj = tabla.tabla_local(funciones[keys].type_data, funciones[keys].value)
            temp_id.append(obj)
        else:
            prueba.append(temp_id)
            temp_id.clear()
            aux = funciones[keys].id_funcion
            obj = tabla.tabla_local(funciones[keys].type_data, funciones[keys].value)
            temp_id.append(obj)
    prueba.append(temp_id)
    pprint.pprint(prueba)
