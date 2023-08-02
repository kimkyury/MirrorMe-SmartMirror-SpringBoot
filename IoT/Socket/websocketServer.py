import asyncio;
import uuid
# 웹 소켓 모듈을 선언한다.
import websockets;

client = {}

async def handle_user_input():
    while True:
        user_input = await asyncio.get_event_loop().run_in_executor(None, input, "Enter something: ")
        # 유저의 입력을 모든 클라이언트에 전송
        for websocket in client.values():
          await websocket.send(user_input)

        # end를 입력하면 모든 루프를 종료한다.
        if user_input == "end":
          asyncio.get_event_loop().stop()
          break
        print("User input:", user_input)

# 세션 아이디로 호출되어 해당 소켓의 데이터를 대기함
async def handle_client_input(session_id):
    try:
      while True:
        # 해당 세션 아이디의 데이터 대기
        client_input = await client[session_id].recv()
        # 클라이언트의 입력 처리
        print(f"\r{session_id} input:", client_input, end="\nEnter something: ")
        
    except websockets.exceptions.ConnectionClosedOK:
       print(f"{session_id} 클라이언트의 요청으로 연결 종료")
       del client[session_id]


# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
  session_id = uuid.uuid4()
  client[session_id] = websocket
  # asyncio.get_event_loop().run_until_complete(handle_client_input());
  await handle_client_input(session_id);
 


# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_until_complete(handle_user_input());
print("끝났지롱~~")
asyncio.get_event_loop().run_forever();
