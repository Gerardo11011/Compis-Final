# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys

# Tabla de simbolos_master
simbolos_master = {}

# Declaración de variables globales
miTipo = None
miID = None
miValor = None


# Objeto tabla
class tabla(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None):
        self.type_data = str(type_data)
        self.value = value


# Funciones para modificar la tabla
def insert(id, type_data):
    temp = tabla(type_data)
    if len(simbolos_master) >= 1 and not itFound(id):
        simbolos_master[id] = temp
    if len(simbolos_master) == 0:
        simbolos_master[id] = temp


def update(id, value):
    if validate(value, id):
        simbolos_master[id].value = value


def validate(dato, id):
    temp = str(type(dato))
    aux = None
    encontro = False
    if id in simbolos_master:
        aux = simbolos_master[id].type_data
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


def itFound(id):
    aux = False
    if id in simbolos_master:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def show():
    for keys in simbolos_master:
        print("ID: ", keys)
        print("VALOR: ", simbolos_master[keys].value, " TYPE DATA: ", simbolos_master[keys].type_data)
        print("")
