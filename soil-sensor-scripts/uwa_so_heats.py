import sensor
import time
import datetime
import numpy as np
import signal

sensor.start()

label = input("manda label: ")

dont_stop_me_now = True

def stop_me_now(signum, frame):
    global dont_stop_me_now
    dont_stop_me_now = False

signal.signal(signal.SIGINT, stop_me_now)

timestamps = []
temps_s0 = []
temps_s1 = []

while dont_stop_me_now:
    try:
        rd = sensor.get_reading()
        timestamps.append(time.time())
        temps_s0.append(rd['tmp0'])
        temps_s1.append(rd['tmp1'])

        print("{} {}".format(str(rd['tmp0']), str(rd['tmp1'])))
    except Exception as e:
        print(e)
        print("Reading finalized due to a runtime exception")
        break

shit = np.vstack((timestamps, temps_s0, temps_s1))

np.savetxt('heat_readings_{}.csv'.format(label), shit, delimiter =', ') 
    

