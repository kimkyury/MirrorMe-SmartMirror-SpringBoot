import os
from moviepy.editor import VideoFileClip, AudioFileClip
from videorec import recording

recording()

# 영상 파일과 음성 파일 경로
video_path = './recorded_video.avi'
audio_path = './recorded_audio.wav'

# 동영상과 음성 파일 불러오기
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# 영상과 음성 합치기
final_clip = video_clip.set_audio(audio_clip)

# 파일 이름 난수 생성


# 합쳐진 동영상 저장
final_output_path = './temp/' + 'final_output.mp4'
final_clip.write_videofile(final_output_path, codec='mpeg4')

# 영상 및 음성 파일 삭제
os.remove(video_path)
os.remove(audio_path)

