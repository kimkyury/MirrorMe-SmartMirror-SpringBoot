import cv2
import numpy as np
from tensorflow.keras import models

# 모델 로드 (이전에 학습한 모델 파일이 필요합니다.)
model = models.load_model('your_trained_model.h5')

# 입력 이미지 경로
image_path = 'TEST.png'

# 이미지 로드 및 전처리
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (128, 128))
    image_normalized = image_resized / 255.0  # 이미지를 0과 1 사이 값으로 정규화
    return np.expand_dims(image_normalized, axis=0)  # 모델 입력 형태로 차원 확장

# 입력 이미지 전처리
input_image = preprocess_image(image_path)

# 모델에 이미지 적용
predictions = model.predict(input_image)

# 결과 확인
# 예시: 0은 "happy", 1은 "neutral", 2는 "sad", 3은 "angry"로 매칭됩니다.
predicted_class = np.argmax(predictions[0])
emotion_classes = {
    0: "happy",
    1: "neutral",
    2: "sad",
    3: "angry"
}
print("예측된 감정 클래스:", emotion_classes[predicted_class])