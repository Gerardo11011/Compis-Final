# Oscar Guevara     A01825177
# Gerardo Ponce     A00818934

from quadruples import Quad


switch = {
    'goto' : "goto",
    'gotof' : "gotof",

    'era' : "era",
    'param' : "param",
    'gosub' : "gosub",
    'endproc' : "endproc",

    '+' : "+",
    '-' : "-",
    '*' : "*",
    '/' : "/",
    '=' : "=",

    '>' : ">",
    '>=' : ">=",
    '<' : "<",
    '<=' : "<=",
    '==' : "==",
    '<>' : "<>",

    'and' : "and",
    'or' : "or",

    'input' : "input",
    'output' : "output"
}


def inicio():
    for i in range(Quad[0].result, len(Quad)):
        switch.get(Quad[i].operator)
