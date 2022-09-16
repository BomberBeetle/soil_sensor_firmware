import serial
import csv
import numpy as np
from scipy import interpolate

conn = serial.Serial()
conn.baudrate = 9600

samples = 100
resistor_val = 22000

thermistor_data = []
with open('../thermistor_data_format/thermistor_data_formatted.csv') as file:
    data = csv.reader(file)
    for row in data:
        thermistor_data.append(row)

thermistor_table = np.array(thermistor_data, dtype='float64')

mintable = np.delete(thermistor_table, 1, 1)
mintable = np.delete(mintable, 1, 1)

avgtable = np.delete(thermistor_table, 1, 1)
avgtable = np.delete(avgtable, 2, 1)

maxtable = np.delete(thermistor_table, 2, 1)
maxtable = np.delete(maxtable, 2, 1)

ttable_stacked = np.vstack((mintable, avgtable, maxtable))

ttable_stacked_unique = np.unique(ttable_stacked[..., 1], return_index=True)

ttable_stacked_unique = np.stack(ttable_stacked_unique, axis=1)

ttable_stacked_unique = np.array([[v[0], ttable_stacked[int(v[1]), 0]] for v in ttable_stacked_unique])

interp_func = interpolate.interp1d(ttable_stacked_unique[..., 0], ttable_stacked_unique[..., 1], kind='linear')


def start(port='/dev/ttyUSB0'):
    conn.setPort(port)
    if not conn.is_open: conn.open()

def stop():
    if conn.is_open: conn.close()

def get_reading():
    conn.write(b'a')
    hum = int.from_bytes(conn.read(2), "little", signed=True)
    tmp0 = int.from_bytes(conn.read(4), "little", signed=True)
    tmp1 = int.from_bytes(conn.read(4), "little", signed=True)

    return {"hum":hum, "tmp0":tmp0, "tmp1":tmp1}

def rawtmp_to_resistance(tmp):
    act = tmp/samples
    return (resistor_val*act)/float((1023-act))

def resistance_to_celsius(res):
    res_adj = res/1000
    """closestmax = np.abs(thermistor_table[..., 1] - res_adj).argmin()
    closestavg = np.abs(thermistor_table[..., 2] - res_adj).argmin()
    closestmin = np.abs(thermistor_table[..., 3] - res_adj).argmin()"""
    """spline_y = np.array((thermistor_table[closestmin, 0], thermistor_table[closestavg, 0], thermistor_table[closestmax, 0]))
    spline_x = np.array((thermistor_table[closestmin, 3], thermistor_table[closestavg, 2], thermistor_table[closestmax, 1]))
    print(spline_x)"""
    
    try:
        return interp_func([res_adj])[0]
    except:
        return None
