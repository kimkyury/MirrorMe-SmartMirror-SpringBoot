import pyaudio
import wave
import time

def record_audio(duration, output_path):
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

if __name__ == "__main__":
    recording_duration = 5  # 녹음 시간(초)
    output_file = "recorded_audio.wav"  # 저장할 오디오 파일 이름
    record_audio(recording_duration, output_file)
