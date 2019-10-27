# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys

# Tabla de simbolos
simbolos = {}

# Declaración de variables globales
miTipo = None
miID = None
miValor = None


# Objeto tabla
class tabla_local(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None):
        self.type_data = str(type_data)
        self.value = value


# Funciones para modificar la tabla
def insert_local(id, type_data):
    temp = tabla_local(type_data)
    if len(simbolos) >= 1 and not itFound_local(id):
        simbolos[id] = temp
    if len(simbolos) == 0:
        simbolos[id] = temp


def update_local(id, value):
    if validate_local(value, id):
        simbolos[id].value = value


def validate_local(dato, id):
    temp = str(type(dato))
    aux = None
    encontro = False
    if id in simbolos:
        aux = simbolos[id].type_data
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


def itFound_local(id):
    aux = False
    if id in simbolos:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def show_local():
    for keys in simbolos:
        print("ID: ", keys)
        print("VALOR: ", simbolos[keys].value, " TYPE DATA: ", simbolos[keys].type_data)
        print("")
