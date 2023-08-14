from tensorflow.keras import models
from statistics import mode
from Message import audio_recoding, video_recoding
from collections import deque
import numpy as np
import cv2
import mediapipe as mp
import math
import threading
import websockets
import asyncio
import os
import json
import requests
from datetime import datetime

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# 검출 모델 미리 로딩
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# 모델 로드 (입력 이미지 크기에 맞게 수정)
model = models.load_model('./Models/best_black_model.h5')

my_name = '1'
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

                if recv == 'Recording Audio':
                    audio_recoding.recordingAudio(my_name, "1")
                    do = ''
                if recv == 'Yo':
                    pass
                if recv == 'V':
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

            # 이미지에 출력하고 그 위에 얼굴 그물망 경계점을 그립니다.
            # if not results.multi_face_landmarks:
            #     return 0

            # blank_image = np.zeros((height, width, 3), dtype=np.uint8)

            # annotated_image = image.copy()
            # face_landmarks = results.multi_face_landmarks[0]

            # face_landmarks = results.multi_face_landmarks[0]
            # mp_drawing.draw_landmarks(
            #     image=blank_image,
            #     landmark_list=face_landmarks,
            #     connections=mp_face_mesh.FACEMESH_TESSELATION,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles
            #     .get_default_face_mesh_tesselation_style())
            # mp_drawing.draw_landmarks(
            #     image=blank_image,
            #     landmark_list=face_landmarks,
            #     connections=mp_face_mesh.FACEMESH_CONTOURS,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles
            #     .get_default_face_mesh_contours_style())
            # mp_drawing.draw_landmarks(
            #     image=blank_image,
            #     landmark_list=face_landmarks,
            #     connections=mp_face_mesh.FACEMESH_IRISES,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles
            #     .get_default_face_mesh_iris_connections_style())
            # # 얼굴 부분만 추출
            # face_only = blank_image[y_min:y_max, x_min:x_max]

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
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    my_hands = mpHands.Hands()

    compareIndex = [[6,8],[10,12],[14,16],[18,20]]
    open = [True, False, False, False, (0,0)]
    gesture = [[True, True, True, True, (0,0), "5"],
            [True, True, False, False, (0,0), "Video"],
            # [True, False, False, True, (0,0), "A"],
            [False, False, False, False, (0,0), "exit"]]
    
    result = deque([None for _ in range(26)])
    distance = deque(['remain' for _ in range(3)])

    last_x = 0.5
    count = 0

    emotion_list = [0,0,0,0,0]

    while not stop_gesture:
        result.popleft()

        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        sf, input_image = preprocess_image(imgRGB)
        if sf:
            # 모델에 이미지 적용
            input_batch = np.expand_dims(input_image, axis=0)
            predictions = model.predict(input_batch)

            # 예측 결과에서의 최대 값과 해당 클래스 인덱스
            max_prediction = np.max(predictions)
            predicted_class = np.argmax(predictions[0])

            # 각 클래스의 임계값
            thresholds = {
                1: 0.8,  # happy
                2: 0.8,  # neutral
                3: 0.8,  # sad
                4: 0.55   # angry
            }

            # 최대 값이 해당 클래스의 임계값보다 크거나 같으면 해당 감정으로 예측
            if max_prediction >= thresholds[predicted_class]:
                emotion_classes = {
                    1: "happy",
                    2: "neutral",
                    3: "sad",
                    4: "angry"
                }
                predicted_emotion = emotion_classes[predicted_class]
                emotion_list[predicted_class] += 1
            else:
                predicted_emotion = "nothing"

            print("예측된 감정:", predicted_emotion)

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



        cv2.imshow("camera",img)
        cv2.waitKey(1)
        
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
    
    try:
        now = datetime.now()
        formatted_date_time = now.strftime('%Y-%m-%d-%H-%M-%S')

        params = {
            "emotionDate": str(formatted_date_time),
            "userId": my_name,
            "emotionList" : emotion_list
        }
        headers = {"Content-Type": "application/json"}

        # 보내고자 하는 Data를 JSON 형식으로 변환
        data = json.dumps(params)

        # JSON 데이터를 포함하여 POST 요청을 보냄
        response = requests.post("http://i9e101.p.ssafy.io:8080/api/iot", headers=headers, data=data)
    except:
        print('error')
    

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

            if do == 'V':
                video_recoding.recordingVideo(my_name, "1")

if __name__ == "__main__":
    # Web socket connect

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
