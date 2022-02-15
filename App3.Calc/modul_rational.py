import menu
b = menu.b
x = menu.x
y = menu.y

def init_operation(b):
    if b == '+':
        fraction_add(x, y)
    if b == '-':
        fraction_sub(x, y)
    if b == '*':
        fraction_mult(x, y)
    if b == '/':
        fraction_divid(x, y)


def fraction_add(a, b):
    res = a + b
    return res

def fraction_sub(a, b):
    res = a - b
    return res

def fraction_mult(a, b):
    res = a * b
    return res

def fraction_divid(a, b):
    res = a / b
    return res