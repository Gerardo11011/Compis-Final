# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
import sys

# Tabla de simbolos_master
# simbolos = {}

# Objeto tabla
class tabla_local(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None):
        self.type_data = str(type_data)
        self.value = value


class tabla_funciones(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None, id_funcion=None, id_variable=None):
        self.type_data = str(type_data)
        self.value = value
        self.id_funcion = id_funcion
        self.id_variable = id_variable


class tabla_temporal(object):
    """docstring for tabla."""

    def __init__(self, id, type_data=None, value=None):
        self.type_data = str(type_data)
        self.value = value
        self.id = id
