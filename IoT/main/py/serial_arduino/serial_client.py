import serial
# from serial import Serial

from websocket import create_connection
# import asyncio

#################################################################
#################################################################
def serialArduino():
    py_serial = serial.Serial(port="/dev/ttyACM0", baudrate=9600,)
    print("아두이노 연결!")

    while True:
        if py_serial.readable():
            response = py_serial.readline()
            # print(type(response))
            # print(response)
            # print("========================")
            # response = response.decode()

            if response == b'1\n':
                send_message = "appear\n\r"

            elif response == b'0\n':
                send_message = "disappear\n\r"

            else:
                 send_message = ""
            

            try:
                ws = create_connection("ws://localhost:9998")
                ws.send("arduino")
                ws.send(send_message)
                ws.close()


            except Exception:
                print("error")

if __name__ == '__main__':
    serialArduino()