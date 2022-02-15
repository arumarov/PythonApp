# Связывает menu.py и modul_complex и modul_rational
import menu
import modul_complex as complex
import modul_rational as rational

# создаем метод, создающий "кнопку", которую сможет "нажимать" пользователь
def button_click():
    value_a, value_b = menu.choise_number()
    model.init(value_a, value_b) # производим инициализацию начальных значений
    result = model.do_it()
    view.view_data(result, "result")