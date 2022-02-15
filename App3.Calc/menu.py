# meny.py - запрашиваем у пользователя, с какими числами он хочет выполнять операции (рациональные или комплексные), просим
# пользователя ввести данные, с которыми будут выполняться арифметические операции

# Инициализация введенных числовых значений для дальнейших расчетов
def choise_number(a): 
    if a == 1:
        print('Введите первое вещественное число (для первого числа в выражении):')
        x1 = float(input())
        print('Введите второе вещественное число (для первого числа в выражении):')
        y1 = float(input())
        print('Введите первое вещественное число (для второго числа в выражении):')
        x2 = float(input())
        print('Введите второе вещественное число (для второго числа в выражении):')
        y2 = float(input())
        res1 = get_complex_number_x(x1, y1)
        res2 = get_complex_number_y(x2, y2)
    elif a == 2:
        print('Введите числитель (для первого числа в выражении):')
        x3 = int(input())
        print('Введите знаменатель (для первого числа в выражении):')
        y3 = int(input())
        print('Введите числитель (для второго числа в выражении):')
        x4 = int(input())
        print('Введите знаменатель (для второго числа в выражении):')
        y4 = int(input())
        res1 = get_rational_number_x(x3, y3)
        res2 = get_rational_number_y(x4, y4)
    else:
        res1 = print("Вы ввели неверное число")
        res2 = print("Перезапустите программу")
    return res1, res2

# Генерация комплексных чисел
def get_complex_number_x(a, b):
    res = complex(a, b)
    return res

def get_complex_number_y(a, b):
    res = complex(a, b)
    return res

# Генерация рациональных чисел
def get_rational_number_x(a, b):
    from fractions import Fraction
    res = Fraction(a, b)
    print(res)
    return res

def get_rational_number_y(a, b):
    from fractions import Fraction
    res = Fraction(a, b)
    print(res)
    return res

# Запуск программы, выбор вида чисел
print("Добро пожаловать в КАЛЬКУЛЯТОР v.1.0")
print()
print("С какими числами вы хотите работать? \nЕсли с комплексными - нажмите 1 \nЕсли с рациональными - нажмите 2")
a = int(input())
choise_number(a)