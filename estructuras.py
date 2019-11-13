# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
# Tabla de simbolos_master
# simbolos = {}


# Objeto tabla
class tabla_local(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None, direccion=None, param=False):
        self.type_data = str(type_data)
        self.value = value
        self.direccion = direccion
        self.param = param


# Estructura de memoria
class memoria(object):
    """docstring for memoria_est."""

    def __init__(self):
        self.integers = {}
        self.float = {}
        self.string = {}
        self.booleanos = {}

    def reiniciar(self):
        self.integers.clear()
        self.float.clear()
        self.string.clear()
        self.booleanos.clear()

# VARIABLES GLOBALES SERAN DEL 0-99 EN CADA DICCIONARIO
# INTEGERS VAN A SER DE 3000-3099
# FLOAT VAN A SER DE 3100-3199
# STRING VAN A SER DE 3200-3299
