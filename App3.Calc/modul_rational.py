def init_operation(x, y):
    print("Какое действие вы хотите совершить? Введите один из знаков: +, -, *, /")
    b = str(input())
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
