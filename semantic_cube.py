# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

# Listas de operadores
operators = ['+', '-', '*', '/']
comparators = ['==', '>', '>=', '<', '<=', '<>']

# Verificar el tipo de resultado de una expresión
def semantic(left, right, operator):
    if(left == 'int'):
        if(right == 'int'):
            if(operator in operators or operator == '='):
                return 'int'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        elif(right == 'float'):
            if(operator in operators):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'

    elif(left == 'float'):
        if(right == 'float'):
            if(operator in operators or operator == '='):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        elif(right == 'int'):
            if(operator in operators):
                return 'float'
            elif(operator in comparators):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'

    elif(left == 'string'):
        if(right == 'string'):
            if(operator == '=' or operator == '+'):
                return 'string'
            elif(operator == '==' or operator == '<>'):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'

    elif(left == 'bool'):
        if(right == 'bool'):
            if(operator == '=' or operator == '==' or operator == '<>'):
                return 'bool'
            elif(operator == 'and' or operator == 'or'):
                return 'bool'
            else:
                return 'error'
        else:
            return 'error'

    else:
        return 'error'
