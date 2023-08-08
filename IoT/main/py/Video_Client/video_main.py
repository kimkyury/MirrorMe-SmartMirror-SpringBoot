from Recognition import find_user, get_user_face
from Message import audio_recoding, video_recoding
from collections import deque
import cv2
import mediapipe as mp
import math
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


def dist(x1,y1,x2,y2):
        return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))


def getgesture():
    global stop_gesture
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    my_hands = mpHands.Hands()

    

    compareIndex = [[6,8],[10,12],[14,16],[18,20]]
    open = [True, False, False, False, (0,0)]
    gesture = [[True, True, True, True, (0,0), "5"],
            [True, True, False, False, (0,0), "V"],
            [True, False, False, True, (0,0), "A"],
            [False, False, False, False, (0,0), "EXIT"]]
    
    result = deque([None for _ in range(26)])
    distance = deque(['remain' for _ in range(3)])

    last_x = 0.5

    while not stop_gesture:
        result.popleft()

        success, img = cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = my_hands.process(imgRGB)
        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            
            if last_x - handLms.landmark[12].x > 0.02:
                distance.append("right")
                distance.popleft()
                last_x = handLms.landmark[12].x
            elif last_x - handLms.landmark[12].x < -0.02:
                distance.append("left")
                distance.popleft()
                last_x = handLms.landmark[12].x
            else:
                distance.append("remain")
                distance.popleft()
                last_x = handLms.landmark[12].x
            
            # print(last_x)

            for i in range(0,4):
                open[i] = (dist(handLms.landmark[0].x,handLms.landmark[0].y,
                        handLms.landmark[compareIndex[i][0]].x,handLms.landmark[compareIndex[i][0]].y) <
                        dist(handLms.landmark[0].x,handLms.landmark[0].y,
                        handLms.landmark[compareIndex[i][1]].x,handLms.landmark[compareIndex[i][1]].y))
            open[4] = (handLms.landmark[0].x,handLms.landmark[0].y)

            for i in range(0,len(gesture)):
                flag = True
                for j in range(0,4):
                    if(gesture[i][j] != open[j]):
                        flag = False
                
                if (flag == True):
                    result.append(gesture[i][5])
                    break
        

        if len(result) < 10:
            result.append(None)

        cv2.imshow("hand",img)
        cv2.waitKey(1)

        ret = max(set(result), key=result.count)

        if ret == "5":
            ret = max(set(distance), key=distance.count)
            if ret == "remain":
                continue
            return ret
        elif ret == None:
            pass
        else:
            return ret


def get_gesture():
    loop = asyncio.new_event_loop()

    while True:
        global websocket, do, stop_gesture
        # GESTURE
        if stop_gesture:continue
        do = getgesture()

        if do != None and websocket != None:
            loop.run_until_complete(websocket.send(do))
            print(do)


if __name__ == "__main__":
    print("start...")
    get_user_face.getUserFaceImage()

    print("find user")
    my_name = find_user.getUserName()
    print("user :", my_name)
    my_name = '1'
    do = ''
    recv = ''
    websocket = None
    stop_gesture = False
    # Web socket connect

    ges = threading.Thread(target=get_gesture)
    ges.start()
    
    asyncio.run(connect())

    print('이상해')