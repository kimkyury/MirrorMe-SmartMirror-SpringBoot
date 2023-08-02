from face_and_gesture import find_user, gesture, getuserface
from message import videorec, mergeimage, audiorec
import threading

from socket import *

if __name__ == "__main__":
    print("start...")
    getuserface.get_user_face_image()

    print("find user")
    my_name = find_user.get_name()
    print("user :", my_name)

    # if len(result) >= 20:
    #     print(result)
    #     return max(set(result), key = result.count)

    while True:
        # GESTURE
        do=(gesture.getgesture())
        print(do)
        if do == 'Hi':
            videorec.recording()
            mergeimage.merge(my_name, "1")
        if do == 'Yo':
            audiorec.record_audio(my_name, "1")
        if do == 'V':
            pass
        if do == 'EXIT':
            exit(0)
