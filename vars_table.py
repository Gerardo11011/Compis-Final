# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import sys

# Tabla de variables
simbolos = []

# Declaración de variables globales
miTipo = None
miID = None
miValor = None

# Objeto variable
class variable(object):
    """docstring for variable."""
    def __init__(self, id, type_data, value=None):
        self.id = str(id)
        self.type_data = str(type_data)
        self.value = value

# Funciones para modificar la tabla
def insert(id, type_data):
    temp = variable(id, type_data)
    if len(simbolos) >= 1 and not itFound(id):
        simbolos.append(temp)
    if len(simbolos) == 0:
        simbolos.append(temp)

def update(id, value):
    if validate(value, id):
        for i in range(0, len(simbolos)):
            if simbolos[i].id == id:
                simbolos[i].value = value

def validate(dato, id):
    temp = str(type(dato))
    longitud = len(simbolos)
    aux = None
    encontro = False
    for i in range(0, longitud):
        if simbolos[i].id == id:
            aux = simbolos[i].type_data
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
    for i in range(0, len(simbolos)):
        if simbolos[i].id == id:
            aux = True
            print("ERROR: ID ya definido: ", id)
            sys.exit()
    return aux

def show():
    longitud = len(simbolos)
    i = 0
    for i in range(0, longitud):
        print(simbolos[i].id, simbolos[i].type_data, simbolos[i].value, sep=', ')
