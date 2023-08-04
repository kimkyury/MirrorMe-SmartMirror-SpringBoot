import cv2
import mediapipe as mp
import math
from collections import deque

def getgesture():
    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    my_hands = mpHands.Hands()

    def dist(x1,y1,x2,y2):
        return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))

    compareIndex = [[6,8],[10,12],[14,16],[18,20]]
    open = [True, False, False, False, (0,0)]
    gesture = [[True, True, True, True, (0,0), "Recording Audio"],
            [True, True, False, False, (0,0), "Recording Video"],
            [True, False, False, True, (0,0), "Yo"],
            [False, False, False, False, (0,0), "EXIT"]]
    
    result = deque([None for _ in range(11)])
    distance = deque([(0, 0) for _ in range(11)])
    while True:
        result.popleft()
        distance.popleft()

        success, img = cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = my_hands.process(imgRGB)
        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            distance.append((handLms.landmark[0].x, handLms.landmark[0].y))

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
            distance.append((0,0))

        cv2.imshow("hand",img)
        cv2.waitKey(1)

        print(result)
        print(distance)