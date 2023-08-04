import cv2
import pyaudio
import wave
import time
from Message import merge_video

def recording(duration, output_path_video, output_path_audio):
    # Sound recording settings
    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []

    # Video recording settings
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 22.0
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_path_video, fourcc, fps, (frame_width, frame_height))

    # Recording start time
    start_time = time.time()

    print("start video recording...")

    while True:
        ret, frame = cap.read()
        out.write(frame)

        # Calculate the elapsed recording time by finding the difference between the current time and the start time
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > duration:
            break

        data = stream.read(CHUNK)
        frames.append(data)

    print("video recording finished!! ")

    # Release video and audio resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_file = wave.open(output_path_audio, 'wb')
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(audio.get_sample_size(FORMAT))
    wav_file.setframerate(RATE)
    wav_file.writeframes(b''.join(frames))
    wav_file.close()


def recordingVideo(sender_email, recipient_email):
    RECORDINGDURATION= 5  # Recording duration in seconds
    OUTPUTVIDEOFILE = "./Message/recorded_video.avi"  # File name to save the recorded video
    OUTPUTAUDIOFILE = "./Message/recorded_audio.wav"  # File name to save the recorded audio

    recording(RECORDINGDURATION, OUTPUTVIDEOFILE, OUTPUTAUDIOFILE)
    merge_video.mergeAudioAndVideo(sender_email, recipient_email)
