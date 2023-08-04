from nlp import my_analyze as nla
from stt_streaming import *
import stt_streaming

import websockets
import asyncio

websocket = None
#################################################################
#################################################################
# 웹소켓 연결하는 코루틴
async def connect():
    # 웹 소켓에 접속을 합니다.
    try:
        async with websockets.connect("ws://localhost:9998") as ws:
            print("왜 안됨?")
            websocket = ws
            await ws.send("audio")
            session_id = await ws.recv()

            while True:
                recv = await ws.recv()


    except websockets.exceptions.ConnectionClosed:
        print("error")


#################################################################
#################################################################
# 마이크를 통해 오디오를 인식하는 코루틴
async def senMicrophone():
    # STT를 위한 세팅
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
        # 오디오 생성기
        audio_generator = stream.generator()
        # 오디오 입력을 구글 stt api에 맞게 바꿈
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
        for content in audio_generator) 

        # api요청
        responses = client.streaming_recognize(streaming_config, requests)
        #  결과를 main으로 보냄
        await sendMain(responses)


#################################################################
#################################################################
# 결과를 전달받아 자연어 처리후 main으로 보내는 함수
async def sendMain(responses):
    num_chars_printed = 0

    for response in responses:
        if not response.results:
            continue

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

        # transcript가 확정 되었다면
        # if result.is_final: 
        else:
            print(transcript + overwrite_chars)

            # 전역에 저장된 웹소켓으로 신호를 보낸다.
            global websocket
            if websocket is not None:
                await websocket.send(nla(transcript))

            num_chars_printed = 0


#################################################################
#################################################################

# 비동기로 서버에 접속한다.
asyncio.get_event_loop().run_until_complete(asyncio.gather(
    connect(),
    senMicrophone(),
))


