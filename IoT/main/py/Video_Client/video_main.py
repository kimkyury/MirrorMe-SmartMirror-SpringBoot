from Utils.datasets import get_labels
from Utils.inference import detect_faces
from Utils.inference import draw_text
from Utils.inference import draw_bounding_box
from Utils.inference import apply_offsets
from Utils.inference import load_detection_model
from Utils.preprocessor import preprocess_input
from keras.models import load_model
from statistics import mode
import numpy as np

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


def getgesture():
    global stop_gesture
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    my_hands = mpHands.Hands()

    # loading face models
    face_cascade = cv2.CascadeClassifier('./Models/haarcascade_frontalface_default.xml')
    emotion_classifier = load_model('./models/emotion_model.hdf5')
    emotion_offsets = (20, 40)

    # starting lists for calculating modes
    emotion_window = []
    frame_window = 10

    # getting input model shapes for inference
    emotion_target_size = emotion_classifier.input_shape[1:3]

    compareIndex = [[6,8],[10,12],[14,16],[18,20]]
    open = [True, False, False, False, (0,0)]
    gesture = [[True, True, True, True, (0,0), "5"],
            [True, True, False, False, (0,0), "V"]]
            # [True, False, False, True, (0,0), "A"],
            # [False, False, False, False, (0,0), "EXIT"]]
    
    result = deque([None for _ in range(26)])
    distance = deque(['remain' for _ in range(3)])

    last_x = 0.5

    while not stop_gesture:
        result.popleft()

        success, img = cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        # emotion recognition
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        emotion_labels = get_labels('fer2013')

        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
		                                      minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for face_coordinates in faces:
            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue

            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            emotion_window.append(emotion_text)

            if len(emotion_window) > frame_window:
                emotion_window.pop(0)
            try:
                emotion_mode = mode(emotion_window)
            except:
                continue

            if emotion_text == 'angry':
                color = emotion_probability * np.asarray((255, 0, 0))
            elif emotion_text == 'sad':
                color = emotion_probability * np.asarray((0, 0, 255))
            elif emotion_text == 'happy':
                color = emotion_probability * np.asarray((255, 255, 0))
            elif emotion_text == 'surprise':
                color = emotion_probability * np.asarray((0, 255, 255))
            else:
                color = emotion_probability * np.asarray((0, 255, 0))
            print(emotion_text)
            color = color.astype(int)
            color = color.tolist()

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
    print("start...")
    try:
        get_user_face.getUserFaceImage()
        print("make face image finished")
    except:
        pass
    
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