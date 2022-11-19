import serial

conn = serial.Serial()


def start(baud=9600, port='/dev/ttyUSB1'):
    conn.baudrate = baud
    conn.setPort(port)
    conn.parity = serial.PARITY_NONE
    conn.bytesize = 8
    conn.stopbits = 1
    if not conn.is_open:
        conn.open()

def stop():
    conn.close()

def read(raw=False):
    conn.write(b'\nW\r')
    print(conn.in_waiting)
    res = conn.read(1+1+1+1+1+10+3+1)
    if raw:
        return res
    else:
        return {
            "s": res[1],
            "r": res[2],
            "n": res[3],
            "m": res[4],
            "f": res[5],
            "value": res[6:16],
            "unit": res[17:20]
        }

def read_hidef(raw=False):
    conn.write(b'\nH\r')
    res = conn.read(1+1+1+1+1+10+3+1)
    if raw:
        return res
    else:
        return {
            "s": res[1],
            "r": res[2],
            "n": res[3],
            "m": res[4],
            "f": res[5],
            "value": res[6:16],
            "unit": res[17:20]
        }


