# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934
# Tabla de simbolos_master
# simbolos = {}


# Objeto tabla
class tabla_local(object):
    """docstring for tabla."""

    def __init__(self, type_data, value=None):
        self.type_data = str(type_data)
        self.value = value


# Estructura de memoria
class memoria_est(object):
    """docstring for memoria_est."""

    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
