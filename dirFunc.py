# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys

# Tabla de funciones
funciones = {}

# Declaración de variables globales
miTipo = None
miID = None
miValor = None


# Objeto tabla
class tabla_funciones(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None):
        self.type_data = str(type_data)
        self.value = value


# Funciones para modificar la tabla
def insert_funciones(id, type_data):
    temp = tabla_funciones(type_data)
    if len(funciones) >= 1 and not itFound_funciones(id):
        funciones[id] = temp
    if len(funciones) == 0:
        funciones[id] = temp


def update_funciones(id, value):
    if validate_funciones(value, id):
        funciones[id].value = value


def validate_funciones(dato, id):
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
        print("ERROR: Dato no válido.")
        sys.exit()


def itFound_funciones(id):
    aux = False
    if id in funciones:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def show_funciones():
    for keys in funciones:
        print("ID: ", keys)
        print("VALOR: ", funciones[keys].value, " TYPE DATA: ", funciones[keys].type_data)
        print("")
