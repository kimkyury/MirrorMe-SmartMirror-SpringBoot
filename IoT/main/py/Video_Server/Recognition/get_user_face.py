import mediapipe as mp
import cv2
import os

def resizeFaceRegion(image, temp):
    # Calculate the coordinates and size of the face region.
    x_max = int(temp.xmin * image.shape[1] + temp.width * image.shape[1])
    y_max = int(temp.ymin * image.shape[0] + temp.height * image.shape[0])

    # Extract the image of the face region.
    return image[int(temp.ymin * image.shape[0]):y_max, int(temp.xmin * image.shape[1]):x_max]

def getUserFaceImage():
    PATH_DIR = './Recognition/'

    # Get the list of files in the directory.
    file_list = os.listdir(PATH_DIR + 'Image/')

    # If there are no files to process, exit the function.
    if not file_list:
        print("No Image Files In Folder")
        return

    # Load the face detection model.
    mp_face_detection = mp.solutions.face_detection

    # Process each file, perform face detection, and resize the faces.
    for i in file_list:
        image_path = PATH_DIR + 'Image/' + i
        image = cv2.imread(image_path)

        with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
            # Resize face of each face.
            if not results.detections:
                print("Face not found in image")
                continue
            else:
                print('Found {} faces.'.format(len(results.detections)))

                for detection in results.detections:
                    image = resizeFaceRegion(image, detection.location_data.relative_bounding_box)

                    face_filename = f'{PATH_DIR}Face_Image/{i}'
                    cv2.imwrite(face_filename, image)
    
    # After processing, delete the original images.
    for i in file_list:
        os.remove(PATH_DIR + 'Image/' + i)

# if __name__ == "__main__":
#     getUserFaceImage()
