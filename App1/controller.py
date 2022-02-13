# Связывает model.py и view.py
import model # импортируем model
import view # импортируем view

# создаем метод, создающий "кнопку", которую сможет "нажимать" пользователь
def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init() # производим инициализацию начальных значений