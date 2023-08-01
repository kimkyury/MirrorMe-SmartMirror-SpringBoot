import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
 
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def plt_imshow(title='image', img=None, figsize=(8 ,5)):
    plt.figure(figsize=figsize)
    if len(img.shape) < 3:
        rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(rgbImg)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.show()

def resize_face_region(image, temp):
    # 얼굴 영역의 좌표와 크기를 구합니다.
    xmax = int(temp.xmin * image.shape[1] + temp.width * image.shape[1])
    ymax = int(temp.ymin * image.shape[0] + temp.height * image.shape[0])

    # 얼굴 영역의 이미지를 추출합니다.
    face_region = image[int(temp.ymin * image.shape[0]):ymax, int(temp.xmin * image.shape[1]):xmax]

    return face_region

for i in range(1,7):
    image_path = './photo/' + str(i) + '.png'
    image = cv2.imread(image_path)

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Draw face detections of each face.
        if not results.detections:
            print("Face not found in image")
        else:
            print('Found {} faces.'.format(len(results.detections)))
            
            annotated_image = image.copy()
            
            # print(results.detections)
            for idx, detection in enumerate(results.detections):
                print(detection.location_data.relative_bounding_box)
                # mp_drawing.draw_detection(annotated_image, detection, bbox_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1))
                temp = resize_face_region(annotated_image, detection.location_data.relative_bounding_box)

                face_filename = f'./face_image/face_{i}_index_{idx}.png'
                cv2.imwrite(face_filename, temp)
            # plt_imshow("Find Faces", annotated_image, figsize=(16,10))