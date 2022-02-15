def init_operation(x, y):
    print("Какое действие вы хотите совершить? Введите один из знаков: +, -, *, /")
    b = str(input())
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
