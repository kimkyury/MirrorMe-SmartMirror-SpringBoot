import os
import cv2
import numpy as np
from tensorflow.keras import models
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# 검출 모델 미리 로딩
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# 모델 로드 (입력 이미지 크기에 맞게 수정)
model = models.load_model('best_val_model.h5')

target_size = (256, 256)

# 이미지 로드 및 전처리
def preprocess_image(image_file):
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5) as face_mesh:
    
        image = cv2.imread(file_path + image_file)

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

        blank_image = np.zeros((height, width, 3), dtype=np.uint8)

        annotated_image = image.copy()
        face_landmarks = results.multi_face_landmarks[0]

        face_landmarks = results.multi_face_landmarks[0]
        mp_drawing.draw_landmarks(
            image=blank_image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_tesselation_style())
        mp_drawing.draw_landmarks(
            image=blank_image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_contours_style())
        mp_drawing.draw_landmarks(
            image=blank_image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_iris_connections_style())

        # 얼굴 부분만 추출
        face_only = blank_image[y_min:y_max, x_min:x_max]

        face_only = cv2.cvtColor(face_only, cv2.COLOR_BGR2GRAY)
        face_only = cv2.resize(face_only, target_size, interpolation=cv2.INTER_LINEAR)
        face_only = np.expand_dims(face_only, axis=-1)  # 이미지에 채널 차원 추가 (1 채널)

        # cv2.imshow('img',face_only)
        # cv2.waitKey(0)

        return face_only


file_path = './test_image/'
file_list = os.listdir(file_path)

for i in file_list:
    # 입력 이미지 전처리
    input_image = preprocess_image(i)
    # 모델에 이미지 적용
    input_batch = np.expand_dims(input_image, axis=0)
    predictions = model.predict(input_batch)

    # 예측 결과에서의 최대 값과 해당 클래스 인덱스
    max_prediction = np.max(predictions)
    predicted_class = np.argmax(predictions[0])

    # 각 클래스의 임계값
    thresholds = {
        0: 0.7,  # happy
        1: 0.7,  # neutral
        2: 0.7,  # sad
        3: 0.7   # angry
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
    else:
        predicted_emotion = "nothing"

    print("예측된 감정:", predicted_emotion)