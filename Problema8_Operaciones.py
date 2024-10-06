def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "¡Error! El tipo de dato no es válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "¡Error! El tipo de dato no es válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "¡Error! El tipo de dato no es válido."

def division(a, b):
    try:
        if b == 0:
            return "¡Error! No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "¡Error! El tipo de dato no es válido."
    