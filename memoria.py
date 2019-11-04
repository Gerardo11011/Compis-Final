import tabla_master as master
from estructuras import memoria_est

# Diccionario de memoria
memory_dir = {}

# Las direcciones de memoria actuales son:
# 3000 -> 3099
# 3100 -> 3199
# 3200 -> 3299



contador_i = 3000
contador_f = 3100
contador_s = 3200


def asginDir(type_data):
    global contador_i
    global contador_f
    global contador_s
    if type_data == 'int' and contador_i >= 3000 and contador_i < 3100:
        temp = contador_i
        memory_dir[temp] = None
        contador_i += 1
        return temp
    elif type_data == 'float' and contador_f >= 3100 and contador_f < 3200:
        temp = contador_f
        memory_dir[temp] = None
        contador_f += 1
        return temp
    elif type_data == 'string' and contador_s >= 3200 and contador_f < 3300:
        temp = contador_s
        memory_dir[temp] = None
        contador_s += 1
        return temp


def insertValue(direccion, value):
    memory_dir[direccion] = value


def getValue(direccion):
    print(memory_dir[direccion])
    return memory_dir[direccion]
