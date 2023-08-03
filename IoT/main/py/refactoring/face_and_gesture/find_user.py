import cv2
import os
import mediapipe as mp
import face_recognition
import numpy as np


def resize_face_region(image, temp, known):
    # 얼굴 영역의 좌표와 크기를 구합니다.
    xmax = int(temp.xmin * image.shape[1] + temp.width * image.shape[1])
    ymax = int(temp.ymin * image.shape[0] + temp.height * image.shape[0])

    # 얼굴 영역의 이미지를 추출합니다.
    face_region = image[int(temp.ymin * image.shape[0]):ymax, int(temp.xmin * image.shape[1]):xmax]

    # 임베딩을 계산하고 비교한다.
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]
        # 기존의 코드로 얼굴 비교 및 출력 수행
        face_min = 1
        for name, face_compare in known.items():
            face_distance = np.linalg.norm(face_compare - face_encoding)
            if face_distance < face_min: 
                result = name
                face_min = face_distance

        # 얼굴 위에 이름 텍스트를 그립니다.
        # cv2.putText(image, result, (int(temp.xmin * image.shape[1]), int(temp.ymin * image.shape[0]) - 10),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # 이름을 return
        return result


def get_name():
    # 모델
    mp_face_detection = mp.solutions.face_detection
    # mp_drawing = mp.solutions.drawing_utils

    # 폴더 내 파일들 불러오기
    PATH_DIR = './face_and_gesture/face_image'
    file_list = os.listdir(PATH_DIR)

    # 알고있는 얼굴 임베딩 저장
    known = dict()

    for photo in file_list:
        image_path = os.path.join(PATH_DIR, photo)
        image = face_recognition.load_image_file(image_path)

        # 이미지 파일로부터 임베딩 계산
        face_encodings = face_recognition.face_encodings(image)

        # 얼굴이 인식되어 임베딩이 있을 경우, 출력
        if len(face_encodings) > 0:
            # 임베딩을 리스트에 추가하여 알고 있는 얼굴로 저장
            known[photo[:-4]] = face_encodings[0]
        else:
            print("얼굴을 찾지 못했습니다.")

    maybe = []

    # 웹캠, 영상 파일의 경우 이것을 사용하세요.:
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("웹캠을 찾을 수 없습니다.")
                # 비디오 파일의 경우 'continue'를 사용하시고, 웹캠에 경우에는 'break'를 사용하세요.
                continue
            # 보기 편하기 위해 이미지를 좌우를 반전하고, BGR 이미지를 RGB로 변환합니다.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # 성능을 향상시키려면 이미지를 작성 여부를 False으로 설정하세요.
            image.flags.writeable = False
            results = face_detection.process(image)

            # 영상에 얼굴 감지 주석 그리기 기본값 : True.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.detections:
                for detection in results.detections:
                    # 얼굴을 감지하면 ditance를 계산하여 이름을 표시/반환
                    name =  resize_face_region(image, detection.location_data.relative_bounding_box, known)
                    if name != None:
                        maybe.append(name)
                        if len(maybe) >= 5:
                            # print(maybe)
                            return max(set(maybe), key = maybe.count)

            # 확인용
            # cv2.imshow('MediaPipe Face Detection', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()