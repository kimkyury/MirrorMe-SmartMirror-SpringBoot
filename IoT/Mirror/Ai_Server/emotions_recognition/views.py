from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tensorflow.keras import models
from rest_framework import status
import json
import os
import numpy as np
import requests
import cv2

from tensorflow.python.client import device_lib
import tensorflow as tf

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
print(device_lib.list_local_devices())
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


# 현재 스크립트 파일의 절대 경로를 얻습니다.
script_directory = os.path.dirname(os.path.abspath(__file__))
# 모델 파일의 경로를 절대 경로로 지정합니다.
model_path = os.path.join(script_directory, 'models', 'best_black_model.h5')
model = models.load_model(model_path)

# Create your views here.
@api_view(['POST'])
def findEmotion(request):
    data = json.loads(request.body)
    emotion_data = data['emotionList']
    emotion_list = [0,0,0,0,0]
    for input_image in emotion_data:
        try:
            input_batch = np.expand_dims(np.array(input_image), axis=0)
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
                emotion_list[predicted_class] += 1
        except:
            emotion_list[0] += 1
    print(emotion_list)

    data['emotionList'] = emotion_list

    headers = {"Content-Type": "application/json"}

    # 보내고자 하는 Data를 JSON 형식으로 변환
    data = json.dumps(data)

    # JSON 데이터를 포함하여 POST 요청을 보냄
    print(data)
    response = requests.post("http://i9e101.p.ssafy.io:8080/api/iot", headers=headers, data=data)
    print(response)
    return Response({"result": "success"}, status=status.HTTP_200_OK)