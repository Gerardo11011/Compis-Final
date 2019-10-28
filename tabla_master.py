# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys
import vars_table as tabla

# Tabla de simbolos
simbolos = {}

# Declaración de variables globales
miTipo = None
miID = None
miValor = None


# Funciones para modificar la tabla
def insert(id, type_data):
    temp = tabla.tabla_local(type_data)
    if len(simbolos) >= 1 and not itFound(id):
        simbolos[id] = temp
    if len(simbolos) == 0:
        simbolos[id] = temp


def update(id, value):
    if validate(value, id):
        simbolos[id].value = value


def validate(dato, id):
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


def itFound(id):
    aux = False
    if id in simbolos:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


def show():
    for keys, obj in simbolos.items():
        '''if keys == "judas":
            print("ID: ", keys)
            print("id variable: ", obj.id[0], " Valor: ", obj.value[0], " Tipo de dato: ", obj.type_data[0])
            print("id variable: ", obj.id[1], " Valor: ", obj.value[1], " Tipo de dato: ", obj.type_data[1])
            # print(obj.value[0].value)

        else:'''
        print("ID: ", keys)
        print("VALOR: ", simbolos[keys].value, " TYPE DATA: ", simbolos[keys].type_data)
        print("")


def insertarMaster(id, objeto):
    for keys in simbolos:
        if keys == id:
            simbolos[keys].value = objeto
