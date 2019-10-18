# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

import sys

# Directorio de funciones
funciones = []

# Declaración de variables globales
miID = None

# Clase funcion
class funcion(object):
    def __init__(self, id, varsTable):
        self.id = str(id)
        self.varsTable = varsTable

# Funciones para modificar el Directorio
def insert(id, varsTable):
    temp = funcion(id, varsTable)
    if len(funciones) >= 1 and not itFound(id):
        funciones.append(temp)
    if len(funciones) == 0:
        funciones.append(temp)

def itFound(id):
    aux = False
    for i in range(0, len(funciones)):
        if funciones[i].id == id:
            aux = True
            print("ERROR: ID ya definido: ", id)
            sys.exit()
    return aux

def show():
    longitud = len(funciones)
    i = 0
    for i in range(0, longitud):
        print(funciones[i].id, sep=', ')
