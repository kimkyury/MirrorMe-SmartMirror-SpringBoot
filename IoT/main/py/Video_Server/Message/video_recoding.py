import cv2
import pyaudio
import wave
import time

def recording_video(duration, output_path_v, output_path_a):
    # 사운드
    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    #영상
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 22.0
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    print(frame_width,frame_height)
    out = cv2.VideoWriter(output_path_v, fourcc, fps, (frame_width, frame_height))

    start_time = time.time()
    print("녹화 시작")

    while True:
        ret, frame = cap.read()
        out.write(frame)

        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            break

        data = stream.read(CHUNK)
        frames.append(data)

    print("녹화 종료")

    # 영상
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # 사운드
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_path_a, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def recording():
    RECORDINGDURATION= 5  # 녹화 시간(초)
    OUTPUTVIDEOFILE = "./Video_Server/Message/recorded_video.avi"  # 저장할 비디오 파일 이름
    OUTPUTAUDIOFILE = "./Video_Server/Message/recorded_audio.wav"  # 저장할 오디오 파일 이름

    recording_video(RECORDINGDURATION, OUTPUTVIDEOFILE, OUTPUTAUDIOFILE)
    print("녹화 및 녹음이 완료되었습니다.")