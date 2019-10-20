# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import pprint
import sys

# Tabla de variables
simbolos = []
variables = {}

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
    if len(variables) >= 1 and not itFound(id):
        variables[id] = temp
    if len(variables) == 0:
        variables[id] = temp

def update(id, value):
    if validate(value, id):
        variables[id].value = value

def validate(dato, id):
    temp = str(type(dato))
    longitud = len(variables)
    aux = None
    encontro = False
    if id in variables:
        aux = variables[id].type_data
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
    if id in variables:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux

def show():
    for keys in variables:
        print("ID: ", keys)
        print("VALOR: ", variables[keys].value, " TYPE DATA: ", variables[keys].type_data)
        print("")
