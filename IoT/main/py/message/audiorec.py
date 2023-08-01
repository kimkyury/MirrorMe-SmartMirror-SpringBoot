import pyaudio
import wave
import time
import string
import random
import json

def record_audio(From, To):
    # 파일 이름 난수 생성
    chars = string.ascii_letters + string.digits
    fileName = ''.join(random.choice(chars) for _ in range(10))

    duration = 5
    output_path = './message/temp/' + fileName + '.wav'

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    # 오디오 녹음 스트림 열기
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    # 녹음 시작 시간
    start_time = time.time()

    print("녹음 시작...")

    while True:
        # 오디오 프레임을 읽어서 리스트에 추가
        data = stream.read(CHUNK)
        frames.append(data)

        # 현재 시간과 시작 시간의 차이를 구해서 녹음 시간을 체크합니다.
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            break

    print("녹음 종료...")

    # 오디오 스트림 닫기
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 녹음된 음성을 WAV 파일로 저장
    wf = wave.open(output_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    temp = dict()
    temp['userId'] = From
    temp['sendUserId'] = To
    temp['fileName'] = fileName + '.wav'
    temp['type'] = 'audio'

    json_data = json.dumps(temp)
    with open('./message/temp/' + fileName + '.json', 'w') as f:
        f.write(json_data)
