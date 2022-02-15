import menu
b = menu.b
x = menu.x
y = menu.y

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
    res = a + b
    return res

def complex_sub(a, b):
    res = a - b
    return res

def complex_mult(a, b):
    res = a * b
    return res

def complex_divid(a, b):
    res = a / b
    return res