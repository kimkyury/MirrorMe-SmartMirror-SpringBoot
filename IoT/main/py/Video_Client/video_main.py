from Recognition import find_user, gesture, get_user_face
from Message import audio_recoding, video_recoding
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


async def get_gesture():
    while True:
        global websocket
        # GESTURE
        do = gesture.getgesture()
        print(do)
        if do != None and websocket != None:
            await websocket.send(do)
        

async def task():
    await asyncio.gather(connect(),get_gesture())

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

    asyncio.run(task())

    print('이상해')