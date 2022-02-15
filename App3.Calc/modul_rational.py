import menu
b = menu.b
x = menu.x
y = menu.y

def init_operation(b):
    if b == '+':
        res = fraction_add(x, y)
    if b == '-':
        res = fraction_sub(x, y)
    if b == '*':
        res = fraction_mult(x, y)
    if b == '/':
        res = fraction_divid(x, y)
    return res


def fraction_add(x, y):
    res = x + y
    return res

def fraction_sub(x, y):
    res = x - y
    return res

def fraction_mult(x, y):
    res = x * y
    return res

def fraction_divid(x, y):
    res = x / y
    return res

print(init_operation(b))