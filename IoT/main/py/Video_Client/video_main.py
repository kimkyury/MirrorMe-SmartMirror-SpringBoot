from Recognition import find_user, gesture, get_user_face
from Message import audio_recoding, video_recoding
import threading
import websockets
import asyncio


#################################################################
#################################################################
# 웹소켓 연결하는 코루틴
async def connect():
    global recv, do, websocket
    # 웹 소켓에 접속을 합니다.
    try:
        async with websockets.connect("ws://localhost:9998") as ws:
            print("연결 성공")
            await ws.send("video")
            session_id = await ws.recv()
            websocket = ws
            while True:
                print("신호 대기")
                recv = await ws.recv()

                if recv == 'Recording Audio':
                    audio_recoding.recordingAudio(my_name, "1")
                    do = ''
                if recv == 'Yo':
                    pass
                if recv == 'Recording Video':
                    video_recoding.recordingVideo(my_name, "1")
                    do = ''
                if recv == 'EXIT':
                    exit(0)

    except websockets.exceptions.ConnectionClosed:
        print("error")
#################################################################
#################################################################


def get_gesture():
    loop = asyncio.new_event_loop()

    while True:
        global websocket, do
        # GESTURE
        do = gesture.getgesture()

        if do != None and websocket != None:
            loop.run_until_complete(websocket.send(do))
            print(do)


if __name__ == "__main__":
    print("start...")
    get_user_face.getUserFaceImage()

    print("find user")
    my_name = find_user.getUserName()
    print("user :", my_name)

    do = ''
    recv = ''
    websocket = None
    # Web socket connect

    ges = threading.Thread(target=get_gesture)
    ges.start()
    
    asyncio.run(connect())

    print('이상해')