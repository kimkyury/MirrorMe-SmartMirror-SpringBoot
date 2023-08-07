# 파이썬 버전 3.8.10

# 비동기 처리 모듈
import asyncio
# 세션 발급용 모듈
import uuid
# 웹 소켓 모듈을 선언한다.
import websockets

from main/py/AISpeaker_Client import tts
import random

###############################################################################################
###############################################################################################
# 접속된 클라이언트를 저장하는 딕셔너리
client = {}
# 역할에 따른 세션 번호를 구분하는 딕셔너리
client_role = {}

# 클라이언트 접속이 되면 호출되고 종료되면 연결이 끊어진다.
async def accept(websocket, path):
    # 클라이언트 연결 시 2초 이내로 신호를 보내야됨
    try:
        role = await asyncio.wait_for(websocket.recv(), timeout = 3)

    # 시간초과시 연결 끊기
    except TimeoutError:
        await websocket.send("연결시간 초과")
        await websocket.close()
        return

    # 우리가 지정한 코드가 아니면 연결 끊어버림
    # 현재는 react, audio, video
    if connect_check.get(role) is None:
        await websocket.send("인증 코드 실패")
        await websocket.close()
        return

    # 조건 충족시 세션코드 발급 후 소켓 저장
    session_id = str(uuid.uuid4())
    client[session_id] = websocket

    # 연결 되었음을 알리고 역할에 따른 세션아이디 저장
    connect_check[role].set()
    client_role[role] = session_id
    # 세션 코드 발급
    await websocket.send(session_id)

    # 따로 서버가 끊길때 까지 대기
    await websocket.wait_closed()
    del client[session_id]
    
###############################################################################################
###############################################################################################

WAITTING = 0
CALL_MIRROR = 100
YOUTUBE = 101
MESSAGE_CAP = 102
MESSAGE_SHOW = 103

STATUS = 0


# 명령이 쌓이게 되는 큐
order = asyncio.Queue()
connect_check = {"audio" : asyncio.Event(), "video" : asyncio.Event()}

# 음성인식 혹은 제스쳐 명령을 받아와서 큐에 저장
async def hearOrder(audio_or_video):
    print(f"{audio_or_video} 연결 대기")
    # 클라이언트가 접속할때까지 대기 후
    # 이벤트 꺼줌
    await connect_check[audio_or_video].wait()
    print(f"{audio_or_video} 연결 성공")
    connect_check[audio_or_video].clear()
    
    while True:
        try:
            catch_order = await client[client_role[audio_or_video]].recv()
            # print(catch_order)
            await order.put(catch_order)
    
        # 연결이 끊겼을 때 새로 연결되어 호출 될때까지 대기
        except websockets.exceptions.ConnectionClosedOK:
            print(f"{audio_or_video}요청으로 연결 끊김")
            await connect_check[audio_or_video].wait()
            print(f"{audio_or_video} 연결 성공")
            connect_check[audio_or_video].clear()

        except websockets.exceptions.ConnectionClosedError:
            print(f"{audio_or_video}가 예상치 못하게 연결 끊김")
            await connect_check[audio_or_video].wait()
            print(f"{audio_or_video} 연결 성공")
            connect_check[audio_or_video].clear()


# 큐에 쌓인 명령을 가져와 하나씩 수행
async def doOrder():
    while True:
        # 명령을 받아 옴
        received_event = await order.get()
        print(received_event)

# 거울을 호출 했을때 실행되는 코루틴
async def call():
    if STATUS != WAITTING:
        return

    answer = ["네", "네, 무엇을 도와드릴까요?", "부르셨나요?"]
    # 대답 후 상태 변경
    tts.text_to_speech(random.choice(answer))

    




async def main():
    await asyncio.gather(
        hearOrder("audio"),
        hearOrder("video"),
        doOrder()
    )

###############################################################################################
###############################################################################################

# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_until_complete(main());
asyncio.get_event_loop().run_forever();


