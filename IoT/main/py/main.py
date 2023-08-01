from face_and_gesture import find_user, gesture
from message import videorec, mergeimage, audiorec
import threading

from socket import *

if __name__ == "__main__":
    print("start...")

    print("find user")
    my_name = find_user.get_name()
    print("user :", my_name)

    while True:
        # STT, NLP

        # GESTURE
        do = gesture.getgesture()
        if do == None: continue
        print(do)
        if do == 'Hi':
            videorec.recording()
            mergeimage.merge(my_name, "1")
        if do == 'Yo':
            audiorec.record_audio(my_name, "1")
        if do == 'V':
            exit(0)

