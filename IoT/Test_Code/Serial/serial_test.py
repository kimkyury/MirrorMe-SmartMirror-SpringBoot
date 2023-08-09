import serial

py_serial = serial.Serial(port="COM4", baudrate=9600,)


while True:
    if py_serial.readable():
        response = py_serial.readline()

        print(response.decode(), end="")
