# Описываем в модуле 2 числа

x = 0
y = 0
# создадим метод, который будет отвечать за инициализацию(указание начальных значений числам)
def init(a, b):
    global x # глобальная переменная, объявленная внутри функции, будет доступна вне ее
    global y
    x = a
    y = b

# опишем метод, который будет складывать два числа
def do_it():
    return x + y

# получается некая модель простого калькулятора, в рамках которой есть:
# 2 числа, инициализация этих чисел и логика их складывания