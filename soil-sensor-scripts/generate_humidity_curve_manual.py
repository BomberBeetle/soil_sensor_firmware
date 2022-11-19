import sensor
from matplotlib import pyplot as plt
import numpy as np
import csv
import datetime

hums = []
volumes = []

sensor.start()

label = input('Etiqueta da amostra: ')
base_vol = float(input('Insira o volume base da terra: '))

while True:
    hum = sensor.get_reading()['hum']
    print(hum)
    str_in = input('({}) Volume de agua (ml): (nao digite um numero para pular e t para terminar):'.format( str(hum)))
    if str_in == 't':
        print('Terminado.')
        break
    else:
        try:
            volumes.append(float(str_in))
            hums.append(hum)
        except:
            print('Pulado.')

np.savetxt('humidity_relation_{}_BASE{}.csv'.format(label, str(base_vol)), np.vstack((volumes, hums)), delimiter =', ') 


