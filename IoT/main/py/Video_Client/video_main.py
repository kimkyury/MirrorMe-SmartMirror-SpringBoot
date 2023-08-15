from Message import audio_recoding, video_recoding
from collections import deque
import numpy as np
import cv2
import mediapipe as mp
import math
import threading
import websockets
import asyncio
import json
import requests
from datetime import datetime
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# 검출 모델 미리 로딩
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

my_name = 11
my_email = 'ssafy@ssafy.com'
do = ''
recv = ''
websocket = None
stop_gesture = False

target_size = (256, 256)

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

                if recv == 'audio_message_start':
                    audio_recoding.recordingAudio(my_name, "1")
                    do = None
                if recv == 'video_message_start':
                    stop_gesture = 0
                    video_recoding.recordingVideo(my_name, "1")
                    stop_gesture = 1
                    do = None
                if recv == 'EXIT':
                    do = None

    except websockets.exceptions.ConnectionClosed:
        print("error")
#################################################################
#################################################################


def dist(x1,y1,x2,y2):
        return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))


# 이미지 로드 및 전처리
def preprocess_image(image):
    try:
        drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        with mp_face_mesh.FaceMesh(
                static_image_mode=True,
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5) as face_mesh:

            # 작업 전에 BGR 이미지를 RGB로 변환합니다.
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # 얼굴 검출
            results = face_mesh.process(rgb_image)

            if results.multi_face_landmarks:
                face_landmarks = results.multi_face_landmarks[0]  # 첫 번째 얼굴 사용
                height, width, _ = image.shape
                x_min, y_min, x_max, y_max = width, height, 0, 0

                for landmark in face_landmarks.landmark:
                    x, y = int(landmark.x * width), int(landmark.y * height)
                    x_min = min(x_min, x)
                    y_min = min(y_min, y)
                    x_max = max(x_max, x)
                    y_max = max(y_max, y)

            face_only = cv2.cvtColor(rgb_image[y_min:y_max, x_min:x_max], cv2.COLOR_BGR2GRAY)
            # face_only = cv2.cvtColor(face_only, cv2.COLOR_BGR2GRAY)
            
            face_only = cv2.resize(face_only, target_size, interpolation=cv2.INTER_LINEAR)
            face_only = np.expand_dims(face_only, axis=-1)  # 이미지에 채널 차원 추가 (1 채널)

            # cv2.imshow('img',face_only)
            # cv2.waitKey(0)

            return True, face_only
    except :
        return False, None


def getgesture():
    global stop_gesture
    if stop_gesture:
        time.sleep(15.5)
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    my_hands = mpHands.Hands()

    compareIndex = [[6,8],[10,12],[14,16],[18,20]]
    open = [True, False, False, False, (0,0)]
    gesture = [[True, True, True, True, (0,0), "5"],
            [True, True, False, False, (0,0), "video_message_start"],
            # [True, False, False, True, (0,0), "A"],
            [False, False, False, False, (0,0), "exit"]]
    
    result = deque([None for _ in range(26)])
    distance = deque(['remain' for _ in range(3)])

    last_x = 0.5
    count = 0

    emotion_list = []
    
    while not stop_gesture:
        result.popleft()

        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        sf, input_image = preprocess_image(imgRGB)

        if sf:
            emotion_list.append(input_image.tolist())
            if len(emotion_list) > 29:break
           
        # gesture recognition
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
    
    cap.release()

    # try:
    now = datetime.now()
    formatted_date_time = now.strftime('%Y%m%d')

    params = {
        "emotionDate": str(formatted_date_time),
        "userId": my_name,
        "emotionList" : emotion_list
    }
    headers = {"Content-Type": "application/json"}

    # 보내고자 하는 Data를 JSON 형식으로 변환
    data = json.dumps(params)

    # JSON 데이터를 포함하여 POST 요청을 보냄
    response = requests.post("http://127.0.0.1:8000/emotion/findemotion/", headers=headers, data=data)
    # except:
    #     print('error')
    

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

            if do == 'video_message_start':
                video_recoding.recordingVideo(my_name, "1")
            
            do = None

if __name__ == "__main__":
    # Web socket connect

    video_recoding.recordingVideo(my_name, "1")

    ges = threading.Thread(target=get_gesture)
    ges.start()
    
    asyncio.run(connect())

    print('끝')

    # print("start...")
    # try:
    #     get_user_face.getUserFaceImage()
    #     print("make face image finished")
    # except:
    #     pass
    
    # print("find user")
    # my_name = find_user.getUserName()
    # print("user :", my_name)
