import pyaudio
import wave
import time
import string
import random
import json

def recordingAudio(sender_email, recipient_email):
    # Generate a random file name
    chars = string.ascii_letters + string.digits
    file_name = "".join(random.choice(chars) for _ in range(10))

    DURATION = 5
    OUTPUT_PATH = "./Message/To_Be_Sent/"
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    # Open an audio recording stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    # Record start time
    start_time = time.time()

    print("start audio recording...")

    while True:
        # Read audio frames and append them to the list
        data = stream.read(CHUNK)
        frames.append(data)

        # Calculate the elapsed recording time by finding the difference between the current time and the start time
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > DURATION:
            break

    print("audio recording finished!!")

    # Close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wav_file = wave.open(OUTPUT_PATH + file_name + ".wav", "wb")
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(audio.get_sample_size(FORMAT))
    wav_file.setframerate(RATE)
    wav_file.writeframes(b"".join(frames))
    wav_file.close()

    # Save information about the file as JSON
    info_dict = dict()
    info_dict["userEmail"] = recipient_email
    info_dict["sendUserEmail"] = sender_email
    info_dict["file_name"] = file_name + ".wav"
    info_dict["type"] = "a"

    # Create a JSON file
    info_json = json.dumps(info_dict)
    with open(OUTPUT_PATH + file_name + ".json", "w") as f:
        f.write(info_json)
    
    print("audio saved")
