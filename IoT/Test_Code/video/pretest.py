import os
import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# 검출 모델 미리 로딩
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

def drawKeypoints(image, keypoints):
    image_with_keypoints = image.copy()
    for kp in keypoints:
        x, y = kp
        cv2.circle(image_with_keypoints, (x, y), 1, (255, 0, 0), -1)  # 원의 색상 변경 (파란색)
    return image_with_keypoints

def preprocess_image(image, target_size):
    # 이미지에서 얼굴 검출
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.detections is not None:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
            x, y, w, h = bbox

            # 얼굴 영역 추출 (얼굴만 잘라냄)
            face = image[y:y+h, x:x+w]

            # 이미지를 가로 길이와 세로 길이가 동일하도록 조절 (사각형 이미지로 만듦)
            if w > h:
                diff = w - h
                top = diff // 2
                face = face[top:top+h, :]
            else:
                diff = h - w
                left = diff // 2
                face = face[:, left:left+w]
            try:
                # 이미지 크기 조정 (리사이징) - 최적화를 위해 interpolation 방법 지정
                image_resized = cv2.resize(face, target_size, interpolation=cv2.INTER_LINEAR)

                # 흑백 이미지로 변환
                image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)

                # 얼굴 영역에서 특징점 검출
                results = face_mesh.process(image_resized)

                if results.multi_face_landmarks:
                    # 검출된 특징점 그리기
                    keypoints = []
                    for face_landmarks in results.multi_face_landmarks:
                        for landmark in face_landmarks.landmark:
                            x, y = int(landmark.x * image_resized.shape[1]), int(landmark.y * image_resized.shape[0])
                            keypoints.append((x, y))

                    # 특징점이 표시된 이미지를 반환 (이미지 리사이징 후 반환하도록 수정)
                    image_with_keypoints = drawKeypoints(image_resized, keypoints)
                    return image_with_keypoints, False
            except:
                return None, True

# 데이터 처리 시작
PATH = 'make_train'
data_folder = f"./{PATH}/"

emotion_classes = {
    1: "happy",
    2: "neutral",
    3: "sad",
    4: "angry"
}

target_size = (256, 256)  # 또는 다른 원하는 크기로 설정

data = []
labels = []

# 데이터 폴더 내의 각 폴더(클래스) 별로 이미지 처리
folder_dir = os.listdir(data_folder)

for folder in folder_dir:
    print(folder, '진행중...')
    emotion_class = int(folder[0])

    folder_path = data_folder + f'{folder}/'
    image_files = os.listdir(folder_path)

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5) as face_mesh:
        
        # cnt = 0
        for image_file in image_files:
            # if cnt >= 500:
            #     break
            try:
                print('\r'+folder_path + image_file, end="")
                image = cv2.imread(folder_path + image_file)

                # 작업 전에 BGR 이미지를 RGB로 변환합니다.
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # 얼굴 검출
                results = face_mesh.process(rgb_image)

                # 이미지에 얼굴 부분만을 추출하여 그립니다.
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
                if not results.multi_face_landmarks:
                    continue

                blank_image = np.zeros((height, width, 3), dtype=np.uint8)

                annotated_image = image.copy()
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

                face_only = cv2.resize(cv2.cvtColor(face_only, cv2.COLOR_BGR2GRAY), target_size, interpolation=cv2.INTER_LINEAR)
                
                # cv2.imshow('Resized Face with Keypoints', face_only)
                # cv2.waitKey(0)  # 키 입력을 기다림

                # 특징점을 그린 이미지를 data 리스트에 추가
                data.append(face_only)
                labels.append(emotion_class)
                # cnt += 1
            except:
                pass
            

# 데이터 전처리 완료 후 저장
data = np.array(data)
labels = np.array(labels)

np.save('preprocessed_data_test.npy', data)
np.save('labels_test.npy', labels)

print("Data shape:", data.shape)
print("Labels shape:", labels.shape)
