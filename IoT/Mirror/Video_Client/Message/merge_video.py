import os
import json
import string
import random
from moviepy.editor import VideoFileClip, AudioFileClip

def mergeAudioAndVideo(sender_email, recipient_email):
    # Paths to the video and audio files
    PATH_VIDEO = "./Message/recorded_video.mp4"
    PATH_AUDIO = "./Message/recorded_audio.wav"

    # Load the video and audio clips
    video_clip = VideoFileClip(PATH_VIDEO)
    audio_clip = AudioFileClip(PATH_AUDIO)

    # Merge the video and audio
    final_clip = video_clip.set_audio(audio_clip)

    # Generate a random file name
    chars = string.ascii_letters + string.digits
    file_name = "".join(random.choice(chars) for _ in range(10))

    # Save the merged video
    final_output_path = "./Message/To_Be_Sent/" + file_name + ".mp4"
    final_clip.write_videofile(final_output_path, codec="libx264")  # Changed codec to libx264

    # Save information about the video as JSON
    info_dict = dict()
    info_dict["userId"] = sender_email
    info_dict["sendUserId"] = recipient_email
    info_dict["fileName"] = file_name + ".mp4"
    info_dict["type"] = "v"

    # Create a JSON file
    info_json = json.dumps(info_dict)
    with open("./Message/To_Be_Sent/" + file_name + ".json", "w") as f:
        f.write(info_json)

    # Delete the video and audio files
    os.remove(PATH_VIDEO)
    os.remove(PATH_AUDIO)

    print("video saved")
