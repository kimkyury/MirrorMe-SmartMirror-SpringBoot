

from serial import Serial

py_serial = Serial(port="/dev/ttyACM0", baudrate=9600,)


while True:
    if py_serial.readable():
        response = py_serial.readline()

        print(response.decode(), end="")
