import cv2
import pyaudio
import wave
import time
import threading

# 영상 녹화 함수
def record_video(duration, output_path):
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30.0
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    start_time = time.time()

    print("녹화 시작")

    while True:
        ret, frame = cap.read()

        if ret:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > duration:
                break
            out.write(frame)
        else:
            break
    
    print("녹화 종료")
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# 음성 녹음 함수
def record_audio(duration, output_path):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    start_time = time.time()

    print("녹음 시작...")

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            break

    print("녹음 종료...")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


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
    recording_duration = 15  # 녹화 시간(초)
    output_video_file = "recorded_video.avi"  # 저장할 비디오 파일 이름
    output_audio_file = "recorded_audio.wav"  # 저장할 오디오 파일 이름

    recording_video(recording_duration, output_video_file, output_audio_file)
    print("동시 녹화 및 녹음이 완료되었습니다.")

    # audio_thread = threading.Thread(target=record_audio, args=(recording_duration, output_audio_file))
    # video_thread = threading.Thread(target=record_video, args=(recording_duration, output_video_file))
    
    # # 영상 녹화와 음성 녹음을 병렬로 실행
    # audio_thread.start()
    # video_thread.start()

    # # 두 작업이 완료될 때까지 기다립니다.
    # video_thread.join()
    # audio_thread.join()