import os
import json
import string
import random
from moviepy.editor import VideoFileClip, AudioFileClip


def merge(From, To):
    # 영상 파일과 음성 파일 경로
    PATH_VIDEO = './Video_Server/Message/recorded_video.avi'
    PATH_AUDIO = './Video_Server/Message/recorded_audio.wav'

    # 동영상과 음성 파일 불러오기
    video_clip = VideoFileClip(PATH_VIDEO)
    audio_clip = AudioFileClip(PATH_AUDIO)

    # 영상과 음성 합치기
    final_clip = video_clip.set_audio(audio_clip)

    # 파일 이름 난수 생성
    chars = string.ascii_letters + string.digits
    file_name = ''.join(random.choice(chars) for _ in range(10))


    # 합쳐진 동영상 저장
    final_output_path = './Video_Server/Message/To_Be_Sent/' + file_name + '.mp4'
    final_clip.write_videofile(final_output_path, codec='mpeg4')

    temp = dict()
    temp['userId'] = From
    temp['sendUserId'] = To
    temp['fileName'] = file_name + '.mp4'
    temp['type'] = 'video'

    json_data = json.dumps(temp)
    with open('./message/temp/' + file_name + '.json', 'w') as f:
        f.write(json_data)

    # 영상 및 음성 파일 삭제
    os.remove(PATH_VIDEO)
    os.remove(PATH_AUDIO)

