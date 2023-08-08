"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

from playsound import playsound
from google.cloud import texttospeech


def text_to_speech(tts_text):

	# Instantiates a client
	client = texttospeech.TextToSpeechClient()

	# Set the text input to be synthesized
	# tts_text = "안녕하세요, 무엇을 도와 드릴까요"
	synthesis_input = texttospeech.SynthesisInput(text=tts_text)

	# Build the voice request, select the language code ("en-US") and the ssml
	# voice gender ("neutral")
	voice = texttospeech.VoiceSelectionParams(
	    language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
	)

	# Select the type of audio file you want returned
	audio_config = texttospeech.AudioConfig(
	    audio_encoding=texttospeech.AudioEncoding.MP3
	)

	# Perform the text-to-speech request on the text input with the selected
	# voice parameters and audio file type
	response = client.synthesize_speech(
	    input=synthesis_input, voice=voice, audio_config=audio_config
	)

	# The response's audio_content is binary.
	with open("output.mp3", "wb") as out:
	    # Write the response to the output file.
	    out.write(response.audio_content)
	    # print('Audio content written to file "output.mp3"')
	print(tts_text)
	playsound("output.mp3")
	
	
if __name__ == '__main__':    
	text_to_speech("안녕하세요, 무엇을 도와 드릴까요")
	