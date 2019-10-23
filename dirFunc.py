# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
# import tabla_master as master
import vars_table as tabla

# Tabla de funciones
funciones = {}

# Declaración de variables globales
miTipo_f = None
miID_f = None
miValor_f = None


# Funciones para modificar la tabla
def insert(id, type_data):
    temp = tabla.tabla_local(type_data)
    if len(funciones) >= 1 and not itFound(id):
        funciones[id] = temp
    if len(funciones) == 0:
        funciones[id] = temp


def update(id, value):
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
        print("VALOR: ", funciones[keys].value, " TYPE DATA: ", funciones[keys].type_data)
        print("")
