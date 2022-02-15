import menu

def button_click_a():
     global a
     print("Добро пожаловать в КАЛЬКУЛЯТОР v.1.0")
     print()
     print("С какими числами вы хотите работать? \nЕсли с комплексными - нажмите 1 \nЕсли с рациональными - нажмите 2")
     a = int(input())
     return a

a = button_click_a()

x = menu.choise_number_x(a)
y = menu.choise_number_y(a)
print(menu.pull_result(a))
exit(0)