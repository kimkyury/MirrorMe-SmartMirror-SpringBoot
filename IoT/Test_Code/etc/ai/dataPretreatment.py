import os
import cv2
import numpy as np

def Pretreatment(path : str):
    # 데이터 폴더 경로 설정
    data_folder = f"./{path}/"

    # 감정 클래스 레이블과 해당 클래스명 매칭
    emotion_classes = {
        1: "happy",
        2: "neutral",
        3: "sad",
        4: "angry"
    }

    # 이미지 크기 설정
    target_size = (128, 128)  # 또는 다른 원하는 크기로 설정

    # 데이터와 라벨을 저장할 리스트 생성
    data = []
    labels = []

    # 폴더별로 이미지 처리
    for emotion_class, class_name in emotion_classes.items():
        folder_path = os.path.join(data_folder, str(class_name))
        image_files = os.listdir(folder_path)

        for image_file in image_files:
            # 이미지 로드
            image_path = os.path.join(folder_path, image_file)
            image = cv2.imread(image_path)

            # 이미지 크기 조정 (리사이징)
            image_resized = cv2.resize(image, target_size)

            # 이미지 데이터를 리스트에 추가
            data.append(image_resized)

            # 라벨 데이터를 리스트에 추가 (각각의 이미지에 해당하는 클래스)
            labels.append(emotion_class)

    # 데이터와 라벨을 numpy 배열로 변환
    data = np.array(data)
    labels = np.array(labels)
    return data, labels
# np.save('preprocessed_data.npy', data)
# np.save('labels.npy', labels)

# 데이터 확인 (옵션)
# print("Data shape:", data.shape)
# print("Labels shape:", labels.shape)

# Data shape: (6, 128, 128, 3)는 전처리된 이미지 데이터의 형태(shape)를 나타냅니다.
# 6: 이미지의 개수입니다. 전처리된 데이터에는 총 6개의 이미지가 포함되어 있습니다.
# 128: 이미지의 높이(Height)입니다. 전처리 후 이미지는 128픽셀의 높이를 가집니다.
# 128: 이미지의 너비(Width)입니다. 전처리 후 이미지는 128픽셀의 너비를 가집니다.
# 3: 이미지의 채널(Channel)입니다. 전처리된 이미지는 컬러 이미지이므로 RGB 채널을 가집니다. RGB 채널은 각각 Red(빨강), Green(녹색), Blue(파랑)의 정보를 나타냅니다. 따라서 각 이미지는 128x128 크기의 컬러 이미지로 구성되어 있습니다.
# Labels shape: (6,)는 라벨(감정 클래스) 데이터의 형태(shape)를 나타냅니다. 각 파라미터의 의미는 다음과 같습니다:
# 6: 라벨(감정 클래스) 데이터의 개수입니다. 전처리된 라벨 데이터에는 총 6개의 라벨이 포함되어 있습니다. 이는 이미지 데이터와 개수가 동일하며, 각 이미지에 해당하는 감정 클래스를 나타냅니다.