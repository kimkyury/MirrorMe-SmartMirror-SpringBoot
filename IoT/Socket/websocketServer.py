import asyncio;
import sys;

# 웹 소켓 모듈을 선언한다.
import websockets;

client = {"client" : ""}

async def handle_user_input():
    while True:
        user_input = await asyncio.get_event_loop().run_in_executor(None, input, "Enter something: ")
        # 유저의 입력 처리
        if client["client"] != "":
            await client["client"].send(user_input)
        print("User input:", user_input)

# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
  client["client"] = websocket
  await handle_user_input()

async def handle_client_input():
    while True:
        if client["client"] != "":
          client_input = await client["client"].recv()
          # 클라이언트의 입력 처리
          print("Client input:", client_input)
 
# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);

asyncio.get_event_loop().run_forever();

print("hello~~~")