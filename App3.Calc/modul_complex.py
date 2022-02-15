import menu
b = menu.b
x = menu.x
y = menu.y

def init_operation(b):
    if b == '+':
        res = complex_add(x, y)
    if b == '-':
        res = complex_sub(x, y)
    if b == '*':
        res = complex_mult(x, y)
    if b == '/':
        res = complex_divid(x, y)
    return res

def complex_add(x, y):
    res = x + y
    return res

def complex_sub(x, y):
    res = x - y
    return res

def complex_mult(x, y):
    res = x * y
    return res

def complex_divid(x, y):
    res = x / y
    return res

print(init_operation(b))