import sensor
from matplotlib import pyplot as plt
import numpy as np

points = []

sensor.start()

sample_name = input('Etiqueta da amostra: ')
base_weight = float(input('Insira o peso base da terra: '))

points = [None]*1024




while True:
    hum = sensor.get_reading()['hum']
    print(hum)
    if points[hum] == None:
        str_in = input('({}) Peso Atual (nao digite um numero para pular e t para terminar):'.format( str(hum)))
        if str_in == 't':
            print('Terminado.')
            break
        elif not str_in.isdecimal():
            print('Pulado.')
        else:
            points.insert(hum, (float(str_in)-base_weight)/base_weight)
            print('Razão para ({}): '.format(str(hum)))
    if range(0, 1024) in points:
        print('Curva completa.')
        break

plt.plot(points)
plt.show()

