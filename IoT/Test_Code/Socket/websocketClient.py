import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
 
async def connect():
    # 웹 소켓에 접속을 합니다.

  try:
    async with websockets.connect("ws://localhost:9998") as websocket:
      await websocket.send("react")
      session_id = await websocket.recv()
      print("============================================")
      print(session_id)
      print("============================================")
      
      while True:
        recv = await websocket.recv()
        print(recv)

      # for i in range(5):
      #   await websocket.send("명령어")
      #   print("보냈다")
      #   await asyncio.sleep(1)
      #   print("에러났냐?")
      # await websocket.close()

  except websockets.exceptions.ConnectionClosed:
    print("error")


# 비동기로 서버에 접속한다.
asyncio.get_event_loop().run_until_complete(connect())