# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

from yacc import varsTable as varsTable

numID = len(varsTable.simbolos)
variables = varsTable.simbolos

# Declaración de pilas
POper = []
PilaO = []
PTypes = []
Quad = []
AVAIL = []

def pushID(id):
    for i in range(0, numID):
        if id == variables[i].id:
            PilaO.append(id)
            PTypes.append(variables[i].type_data)
            AVAIL.append(variables[i].value)

def pushPoper(operator):
    POper.append(operator)

def popTerm():
    if POper[len(POper-1)] == '+' or POper[len(POper-1)] == '-':
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()
        result_type = None
        if(result_type != 'error'):
            result
