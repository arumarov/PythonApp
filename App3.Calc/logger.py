from datetime import datetime as dt
from time import time

def data_logger(x, y, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; result: {}\n'
                     .format(time, x, y, res))


# def temperature_view(sensor):
#     data = prov.get_temperature(sensor)
#     log.temperature_logger(data)
#     return data
