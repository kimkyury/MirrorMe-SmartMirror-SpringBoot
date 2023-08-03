import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
 
async def connect():
    # 웹 소켓에 접속을 합니다.
  try:
    async with websockets.connect("ws://localhost:9998") as websocket:
      print("connent")
      while True:
        response = await websocket.recv()
        print(response)

  except websockets.exceptions.ConnectionClosed:
    print("error")





    # for i in range(1,10,1):
    #   # 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력합니다.
    #   data = await websocket.recv();
    #   print(data);
# 비동기로 서버에 접속한다.
asyncio.get_event_loop().run_until_complete(connect())