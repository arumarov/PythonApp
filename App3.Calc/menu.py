# menu.py - запрашиваем у пользователя, с какими числами он хочет выполнять операции (рациональные или комплексные), просим
# пользователя ввести данные, с которыми будут выполняться арифметические операции
# Инициализация введенных числовых значений для дальнейших расчетов

import modul_complex
import modul_rational

def choise_number_x(a):
    global x
    if a == 1:
        print('Введите первое вещественное число (для первого числа в выражении):')
        x1 = float(input())
        print('Введите второе вещественное число (для первого числа в выражении):')
        y1 = float(input())
        x = get_complex_number_x(x1, y1)
    elif a == 2:
        print('Введите числитель (для первого числа в выражении):')
        x3 = int(input())
        print('Введите знаменатель (для первого числа в выражении):')
        y3 = int(input())
        x = get_rational_number_x(x3, y3)
    else:
        x = print("Вы ввели неверное число")
    return x

def choise_number_y(a):
    global y
    if a == 1:
        print('Введите первое вещественное число (для второго числа в выражении):')
        x2 = float(input())
        print('Введите второе вещественное число (для второго числа в выражении):')
        y2 = float(input())
        y = get_complex_number_y(x2, y2)
    elif a == 2:
        print('Введите числитель (для второго числа в выражении):')
        x4 = int(input())
        print('Введите знаменатель (для второго числа в выражении):')
        y4 = int(input())
        y = get_rational_number_y(x4, y4)
    else:
        y = print("Пожалуйста перезапустите программу")
    return y

# Генерация комплексных чисел
def get_complex_number_x(x, y):
    res = complex(x, y)
    return res

def get_complex_number_y(x, y):
    res = complex(x, y)
    return res

# Генерация рациональных чисел
def get_rational_number_x(x, y):
    from fractions import Fraction
    res = Fraction(x, y)
    return res

def get_rational_number_y(x, y):
    from fractions import Fraction
    res = Fraction(x, y)
    return res

def pull_result(a):
    if a == 1:
        res = modul_complex.init_operation(x, y)
    elif a == 2:
        res = modul_rational.init_operation(x, y)
    return res