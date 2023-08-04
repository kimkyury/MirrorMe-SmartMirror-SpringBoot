import cv2
import os
import mediapipe as mp
import face_recognition
import numpy as np

def calculateEmbedding(image, known):
    # Calculate and compare face embeddings.
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]
        # Perform face comparison and output using the existing code.
        face_min = 1
        for name, face_compare in known.items():
            face_distance = np.linalg.norm(face_compare - face_encoding)
            if face_distance < face_min: 
                result = name
                face_min = face_distance

        return result

def getUserName():
    # Load the mediapipe face detection model.
    mp_face_detection = mp.solutions.face_detection

    # Load files from the folder.
    path_dir = './Recognition/Face_Image/'
    file_list = os.listdir(path_dir)

    # Store known face embeddings.
    known = dict()

    for photo in file_list:
        image_path = os.path.join(path_dir, photo)
        image = face_recognition.load_image_file(image_path)

        # Calculate face embeddings from the image file.
        face_encodings = face_recognition.face_encodings(image)

        # If a face is detected and an embedding is obtained, store it in the dictionary.
        if len(face_encodings) > 0:
            known[photo[:-4]] = face_encodings[0]
        else:
            print("Could not find a face in the image.")

    maybe = []

    # Use webcam (or video file) for face recognition.
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Could not find a webcam.")
                continue
            # Flip the image horizontally for better view, and convert BGR to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            # Detect faces and calculate distance to recognize the name.
            name = calculateEmbedding(image, known)
            if name is not None:
                maybe.append(name)
                if len(maybe) >= 5:
                    return max(set(maybe), key=maybe.count)
    cap.release()
