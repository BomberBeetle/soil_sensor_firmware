import sensor
import scale
import time
import numpy as np
import signal

sensor.start()
scale.start()

timestamps = []
readings = []
scale_readings = []

label = input("manda label paizão: ")

dont_stop_me_now = True

def stop_me_now(signum, frame):
    global dont_stop_me_now
    dont_stop_me_now = False

signal.signal(signal.SIGINT, stop_me_now)

while dont_stop_me_now:
    try:
        time.sleep(0.005)
    #comment this line to fuckin. fart out readings like
    #there's no tomorrow.
        data.append((time.time(), sensor.get_reading(), scale.read_hidef()))
        timestamps.append(time.time())
        readings.append(sensor.get_reading())
        scale_readings.append(scale.read_hidef())
    except Exception as e:
        print("reading stopped due to exception (dumping readings): ")
        print(e)

stuff = np.vstack((timestamps, readings, scale_readings))

np.savetxt('hum_curve_{}.csv'.format(label), stuff, delimiter=", ")