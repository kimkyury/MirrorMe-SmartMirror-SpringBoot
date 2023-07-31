from nlp import sample_analyze_syntax as nla
from stt_streaming import MicrophoneStream
from tts import text_to_speech


def listen_print_loop(responses):
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
            print(transcript + overwrite_chars)

            # 문장중에 '명령끝'이라는 단어가 있다면 종료한다.
            if re.search(r'\b(명령 끝)\b', transcript, re.I):
                print('Exiting..')
                break

            num_chars_printed = 0

RATE = 16000
CHUNK = int(RATE / 10)  


WAITING = 100
LISTEN_ORDER = 200

STATE = 100


while True:
    

