import asyncio;

# 웹 소켓 모듈을 선언한다.
import websockets;
 


# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
  while True:
        data = await websocket.recv()
        print(f"Received: {data}")

        response_data = input("보낼 메세지: ")

        await websocket.send(response_data)

    
 
# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();