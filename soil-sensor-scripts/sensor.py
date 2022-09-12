import serial

conn = serial.Serial()
conn.baudrate = 9600


def start(port='/dev/ttyUSB0'):
    conn.setPort(port)
    if not conn.is_open: conn.open()

def stop():
    if conn.is_open: conn.close()

def get_reading():
    conn.write(ord('a'))
    hum = conn.readline()
    tmp0 = conn.readline()
    tmp1 = conn.readline()

    return {"hum":hum, "tmp0":tmp0, "tmp1":tmp1}