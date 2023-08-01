from nlp import my_analyze as nla
from stt_streaming import *
import stt_streaming
from tts import text_to_speech


WAITING = 100
LISTEN_ORDER = 200

STATE = 100

def listen_print_loop(responses):
    global STATE, WAITING, LISTEN_ORDER
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        # 최종적인 결과값은 언제나 results[0]에 반영되므로 result[0]만 고려.
        result = response.results[0]
        if not result.alternatives:
            continue

        # 확실성 가장 높은 alternative의 해석
        transcript = result.alternatives[0].transcript

        # 완성된 문장이 intrim 문장보다 짧다면, 나머지 부분은 ' '으로 overwrite해 가려준다.
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))   

        if not result.is_final: # 확정된 transcript가 아니라면,
            sys.stdout.write(transcript + overwrite_chars + '\r')   # '\r'로 줄바꿈은 하지 않고 맨 앞으로 돌아가 이전 문장위에 덧쓰도록 한다.
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:   # 확정된 transcript라면

            if re.search(r'\b(여기까지)\b', transcript, re.I):
                text_to_speech("대화를 종료합니다.")
                break

            # 거울아 단어에 반응해서 대답한다
            elif STATE == WAITING and re.search(r'\b(거울아)\b', transcript, re.I):
                print("##################################")
                text_to_speech("네")
                STATE = LISTEN_ORDER
                continue

            elif STATE == LISTEN_ORDER:
                temp, order = nla(transcript)
                text_to_speech()
                if temp != -1:
                    STATE = WAITING
                print("##################################")
                continue



            # else:
                # print(transcript + overwrite_chars)
                
            
            num_chars_printed = 0


RATE = 16000
CHUNK = int(RATE / 10) 


language_code = 'ko-KR'  # a BCP-47 language tag

client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding='LINEAR16',
    sample_rate_hertz=RATE,
    max_alternatives=1, 
    language_code=language_code)
streaming_config = speech.StreamingRecognitionConfig(
    config=config,
    interim_results=True)

with MicrophoneStream(RATE, CHUNK) as stream:
    audio_generator = stream.generator()
    requests = (speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator) 

    responses = client.streaming_recognize(streaming_config, requests)
    listen_print_loop(responses) 

    

