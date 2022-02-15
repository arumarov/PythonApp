# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в нее систему логирования

# meny.py - запрашиваем у пользователя, с какими числами он хочет выполнять операции (рациональные или комплексные), просим
# пользователя ввести данные, с которыми будут выполняться арифметические операции

# modul_complex.py - выполняет арифметические операции с комплексными числами



####################
# Комплексные числа:

a = 2 +2j
b = 3 + 4j

print(a + b)


####################
# Рациональные числа:
from fractions import Fraction

a = Fraction(5, 9)
b = Fraction(2, 6)

print(a + b)