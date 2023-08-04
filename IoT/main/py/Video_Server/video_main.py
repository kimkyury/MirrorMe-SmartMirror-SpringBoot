from Recognition import find_user, gesture, get_user_face
from Message import audio_recoding, video_recoding

if __name__ == "__main__":
    print("start...")
    get_user_face.getUserFaceImage()

    print("find user")
    my_name = find_user.getUserName()
    print("user :", my_name)

    while True:
        # GESTURE
        do = gesture.getgesture()
        print(do)
        if do == 'Recording Audio':
            audio_recoding.recordingAudio(my_name, "1")
        if do == 'Yo':
            pass
        if do == 'Recording Video':
            video_recoding.recordingVideo(my_name, "1")
        if do == 'EXIT':
            exit(0)
