import sensor

import matplotlib.pyplot as plt
import numpy as np

sensor.start()

xnew = np.arange(0.1, 1800, 0.1)

ynew = sensor.interp_func(xnew)   # use interpolation function returned by `interp1d`

plt.plot(sensor.ttable_stacked_unique[..., 0], sensor.ttable_stacked_unique[..., 1], 'o', xnew, ynew, '-')

plt.title("Curva de Resistência-Temperatura")

plt.show()


while True:
    reading = sensor.get_reading()
    print("tmp0: " + str(sensor.resistance_to_celsius(sensor.rawtmp_to_resistance(reading["tmp0"]))))
    print("tmp1: " + str(sensor.resistance_to_celsius(sensor.rawtmp_to_resistance(reading["tmp1"]))))
    print("hum: " + str(reading["hum"]))