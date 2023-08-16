import serial
# from serial import Serial

import websockets
import asyncio

#################################################################
#################################################################
async def serialArduino():
    py_serial = serial.Serial(port="/dev/ttyACM0", baudrate=9600,)
    print("아두이노 연결!")

    while True:
        if py_serial.readable():
            response = py_serial.readline()
            response = response.decode()
            print(response + "test")
            

            try:
                async with websockets.connect("ws://localhost:9998") as ws:
                    await ws.send("arduino")
                    await ws.send(f"{response}")
                    await ws.close()


            except websockets.exceptions.ConnectionClosed:
                print("error")

if __name__ == '__main__':
    asyncio.run(serialArduino())