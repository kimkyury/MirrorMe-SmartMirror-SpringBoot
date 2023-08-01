import os
import json
import string
import random
from moviepy.editor import VideoFileClip, AudioFileClip


def merge(From, To):
    # 영상 파일과 음성 파일 경로
    video_path = './message/recorded_video.avi'
    audio_path = './message/recorded_audio.wav'

    # 동영상과 음성 파일 불러오기
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # 영상과 음성 합치기
    final_clip = video_clip.set_audio(audio_clip)

    # 파일 이름 난수 생성
    chars = string.ascii_letters + string.digits
    fileName = ''.join(random.choice(chars) for _ in range(10))


    # 합쳐진 동영상 저장
    final_output_path = './message/temp/' + fileName + '.mp4'
    final_clip.write_videofile(final_output_path, codec='mpeg4')

    temp = dict()
    temp['userId'] = From
    temp['sendUserId'] = To
    temp['fileName'] = fileName + '.mp4'
    temp['type'] = 'video'

    json_data = json.dumps(temp)
    with open('./message/temp/' + fileName + '.json', 'w') as f:
        f.write(json_data)

    # 영상 및 음성 파일 삭제
    os.remove(video_path)
    os.remove(audio_path)

