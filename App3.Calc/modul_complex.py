import menu

menu.choise_number(a)

def init_operation(b):
    if b == '+':
        complex_add(x, y)
    if b == '-':
        complex_sub(x, y)
    if b == '*':
        complex_mult(x, y)
    if b == '/':
        complex_divid(x, y)


def complex_add(a, b):
    return a + b

def complex_sub(a, b):
    return a - b

def complex_mult(a, b):
    return a * b

def complex_divid(a, b):
    return a / b