# 파이썬 버전 3.8.10

# 비동기 처리 모듈
import asyncio
# 세션 발급용 모듈
import uuid
# 웹 소켓 모듈을 선언한다.
import websockets
# 파일 경로 설정용 sys
import sys
sys.path.append("./AISpeaker_Client/")
from tts import text_to_speech as tts

sys.path.append("./Video_Client/")
from Recognition import find_user, get_user_face

# import serial
import random
import json

import requests


###############################################################################################
###############################################################################################
# 서버에서 유저 데이터 받아오기

from get_user_info import encryption, decryption, decode_base64_image, save_image_as_png
# 장치 고유 시리얼 넘버
DEVICE_SERIAL_CODE = '6rBZ68bBiJ46ntHGBfJP'
URL_USER_DATA = "http://i9e101.p.ssafy.io:8080/api/iot/users"
RSA_N = 20453
RSA_E = 20053


# 서버팀에 보내고자 하는 것을 key - value 형식으로 작성. 작성한 것을 temp라는 변수에 대입
# 모두 소문자로 구성해줄 것

print("서버에 유저 데이터 요청")
temp = encryption("6rBZ68bBiJ46ntHGBfJP",RSA_N,RSA_E)
params = {
    "mirrorId": temp,
}
headers = {"Content-Type": "application/json"}

# 보내고자 하는 Data를 JSON 형식으로 변환
data = json.dumps(params)

# JSON 데이터를 포함하여 POST 요청을 보냄
response = requests.post(URL_USER_DATA, headers=headers, data=data)

# 송신 결과 확인
rdata = response.json()
user_info_list = rdata['response']

for user in user_info_list:
    if user["profileImage"] != None:
        img_out = decode_base64_image(user["profileImage"])
        save_image_as_png(img_out, f'/home/ssafy/바탕화면/S09P12E101/IoT/main/py/Video_Client/Recognition/Image/{user["userName"]}.png')
        # save_image_as_png(img_out, f'./Video_client/Recognition/Image/{user["userName"]}.png')

    user.pop("profileImage",None)

get_user_face.getUserFaceImage()

# Create a JSON file
info_json = json.dumps(user_info_list)
with open("./" + "user_data" + ".json", "w") as f:
    f.write(info_json)
print("데이터 수신 완료")

###############################################################################################
###############################################################################################
# 접속된 클라이언트를 저장하는 딕셔너리
client = {}
# 역할에 따른 세션 번호를 구분하는 딕셔너리
client_role = {}

# 클라이언트 접속이 되면 호출되고 종료되면 연결이 끊어진다.
async def accept(websocket, path):
    # 클라이언트 연결 시 2초 이내로 신호를 보내야됨
    try:
        role = await asyncio.wait_for(websocket.recv(), timeout = 3)

    # 시간초과시 연결 끊기
    except asyncio.exceptions.TimeoutError:
    # except TimeoutError:
        print("연결시간 초과")
        await websocket.send("연결시간 초과")
        await websocket.close()
        return

    if role == "arduino":
        print("아두이노 연결됨")
        person_is_sen = await websocket.recv()
        await order.put(person_is_sen)
        await websocket.wait_closed()
        return

    # 우리가 지정한 코드가 아니면 연결 끊어버림
    # 현재는 react, audio, video
    if connect_check.get(role) is None:
        await websocket.send("인증 코드 실패")
        await websocket.close()
        return

    # 이미 연결된 장치면 리턴
    if client.get(role):
        await websocket.close()
        return


    # 조건 충족시 세션코드 발급 후 소켓 저장
    # session_id = str(uuid.uuid4())
    client[role] = websocket

    # 연결 되었음을 알리고 역할에 따른 세션아이디 저장
    connect_check[role].set()
    client_role[role] = role
    # 세션 코드 발급
    # 리엑트 안 보내줌

    # 따로 서버가 끊길때 까지 대기
    await websocket.wait_closed()
    del client[session_id]
    
###############################################################################################
###############################################################################################

user_email = ""
user_name = ""
user_id = ""

SCREEN_OFF = 0
WAITTING = 1
CALL_MIRROR = 100
YOUTUBE = 101
MESSAGE_CAP = 102
MESSAGE_SHOW = 103

STATUS = SCREEN_OFF


# 명령이 쌓이게 되는 큐
order = asyncio.Queue()
connect_check = {"audio" : asyncio.Event(), "video" : asyncio.Event(), "react" : asyncio.Event()}

# 음성인식 혹은 제스쳐 명령을 받아와서 큐에 저장
async def hearOrder(audio_or_video):
    print(f"{audio_or_video} 연결 대기")
    # 클라이언트가 접속할때까지 대기 후 이벤트 꺼줌
    await connect_check[audio_or_video].wait()
    print(f"{audio_or_video} 연결 성공")
    connect_check[audio_or_video].clear()
    
    while True:
        try:
            catch_order = await client[client_role[audio_or_video]].recv()
            # print(catch_order)
            await order.put(catch_order)
    
        # 연결이 끊겼을 때 새로 연결되어 호출 될때까지 대기
        except websockets.exceptions.ConnectionClosedOK:
            print(f"{audio_or_video}요청으로 연결 끊김")
            await connect_check[audio_or_video].wait()
            print(f"{audio_or_video} 연결 성공")
            connect_check[audio_or_video].clear()

        except websockets.exceptions.ConnectionClosedError:
            print(f"{audio_or_video}가 예상치 못하게 연결 끊김")
            await connect_check[audio_or_video].wait()
            print(f"{audio_or_video} 연결 성공")
            connect_check[audio_or_video].clear()


# 큐에 쌓인 명령을 가져와 하나씩 비동기로 수행
async def doOrder():
    while True:
        # 명령을 받아 옴
        received_event = await order.get()
        commend, *arg = received_event.split("\n\r")
        print(commend)
        # if commend == "disappear!" and STATUS == SCREEN_OFF:
        #     continue
        # if commend == "appear!" and STATUS != SCREEN_OFF:
        #     continue

        if order_fun.get(commend, False):
            # print("여긴오나?")
            asyncio.create_task(order_fun[commend](*arg))

        
# 음성 처리 결과를 처리하는 코루틴 함수들
# 거울을 호출 했을때 실행
# 없어질 수도 있음
async def call(*arg):
    global STATUS
    if STATUS != WAITTING:
        print(f"현재 상태 : {STATUS}")
        return

    answer = ["네", "네, 무엇을 도와드릴까요?", "부르셨나요?"]
    # 대답 후 상태 변경
    tts(random.choice(answer))
    STATUS = CALL_MIRROR
# arg로 메세지 보내기
async def messageSend(*arg):
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return
    
    STATUS = MESSAGE_CAP
    # 보내는 대상은  target에 저장되어 있음
    target = arg[0]
    print(target)

    send_data = {
        "order" : "MESSAGESENDSTART",
        "query" : {
            "receiver" : target
        }
    }
    print("리엑트에 전송")
    # 리엑트가 접속 했을 때만 전송
    await websocketSend('react', json.dumps(send_data))
    print("리엑트에 전송완료")
    
    with open("./user_data.json", "r") as f:
        user_data = json.load(f)
        global user_email
        for user in user_data:
            check = False
            if user["userEmail"] == user_email:
                for friend in user["aliases"]:
                    if friend["connectUserAlias"] == target:
                        target = friend["connectUserEmail"]
                        check = True
                        break
            
            if check:
                break

        del user_data

    # audio와 video측에 알려서 연결을 끊고 녹화를 시작하도록함
    await websocketSend('audio', 'audio_end')

    tts(f"{target}님께 보낼 영상메세지 촬영을 시작합니다.") 
    send_data = {
        "order" : "video_start",
        "query" : {
            "target_user" : target
        }
    }
    await websocketSend('video', json.dumps(send_data))

async def messageEnd(*arg):
    global STATUS
    if STATUS != MESSAGE_CAP:
        return
    print("메세지 녹화 종료")
    await websocketSend('audio', "audio_restart")

    # 메세지 녹화 종료를 리엑트로 알림
    send_data = {
        "order" : "MESSAGESENDEND",
        "query" :None
    }

    await websocketSend('react', json.dumps(send_data))

    STATUS = WAITTING

# 메세지 확인하기
async def messageShow(*arg):
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return
    
    send_data = {
        "order" : "MESSAGESHOW",
        "query" : None
    }

    await websocketSend('react', json.dumps(send_data))

    STATUS = MESSAGE_SHOW
    tts("메세지를 내역입니다.")

    # 메세지 보기 처리

    # 리엑트 측으로 부터 영상이 종료되었음을 수신
    # if client_role.get("react", False):
    #     await client[client_role["react"]].recv()

    STATUS = WAITTING
# arg로 유튜브 검색하기
async def youtube(*arg):
    ########################################
    # 거울의 상태에 따라  전송 여부를 결정
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return
    
    #########################################
    # 유튜브 영상 출력 관련 처리
    # 유튜브 영상 검색 후 최상단 영상의 키
    youtube_key = arg[0]

    send_data = {
        "order" : "YOUTUBE",
        "query" : {
            "key" : youtube_key
            }
    }

    # 리엑트 접속시 링크 보내주기
    await websocketSend('react', json.dumps(send_data))



    STATUS = YOUTUBE
    tts(f"{youtube_key}관련 유튜브 영상을 재생해 드릴게요")
    #########################################
    # 유튜브 종료 대기
    # 리엑트 측에서 유튜브 영상이 끝났음을 수신
    # if client_role.get("react", False):
    #     await client[client_role["react"]].recv()

    STATUS = WAITTING
    return 
# 날씨 확인하기
async def weather(*arg):
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return

    send_data = {
        "order" : "WEATHER",
        "query" : None
    }
    await websocketSend('react', json.dumps(send_data))


    tts("오늘의 날씨 입니다.")

    # 날씨관련 받아서
    # 음성으로 출력하기

    STATUS = WAITTING
# 뉴스 확인하기
# 현재 처리 하지 않음
# nlp에서 NEWS로 넘어오는 신호가 없어서 실행되지 않음
async def news(*arg):
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return

    tts("뉴스를 확인합니다.")

    STATUS = WAITTING

    # react로 보냄
# 모르겠는건 모른다고 답하기
async def chatgpt(*arg):
    global STATUS
    if STATUS != CALL_MIRROR:
        print(f"현재 상태 : {STATUS}")
        return

    tts("무슨 말씀이신지 이해하지 못했어요")

    STATUS = WAITTING

###############################################################################################
###############################################################################################
# 아두이노 연결 처리 함수들

async def appear(*arg):
    # 둘중에 어느게 화면 켜는건지 모르겠다. 일단 해보고 처리
    # os.system("xset dpms force standby")
    # os.system("xset dpms force suspend")
    # print("appear로 잘 들어옴!")
    # return

    global STATUS
    if STATUS != SCREEN_OFF:
        return
    
    # 얼굴 인식
    # 유저이름 인코딩 중요!
    print("start...")
    try:
        get_user_face.getUserFaceImage()
        print("make face image finished")
    except:
        pass
    
    print("find user")
    global user_email, user_name, user_id
    user_name = find_user.getUserName()
    print("user :", user_name)
    user_name = "신성환"

    with open("./user_data.json", "r") as f:
        user_data = json.load(f)
        for user in user_data:
            if user["userName"] == user_name:
                user_id = user["userId"]
                user_email = user["userEmail"]
                break

        del user_data

    print(user_email)
    # 인식된 사람에게 해줄 말을 정보 비동기로 받아오기
    task = asyncio.create_task(callSpeech(user_email))

    ## 리엑트로 유저정보 보내기
    send_data = {
        "order" : "USERINFO",
        "query" : {
            "email" : user_email
        }
    }

    await websocketSend('audio', 'audio_restart')
    await websocketSend('react', json.dumps(send_data))

    # 비디오로 유저정보 보내기
    send_data = {
        "order" : "userInfo",
        "query" : {
            "userId" : user_id,
            "userEmail" : user_email
        }
    }
    
    await websocketSend('video', json.dumps(send_data))


    # 사람에게 해줄말을 받아올 때까지 대기
    speech = await task

    # 해줄말이 있다면 내용 리엑트로 전달하고, tts시키기
    if speech:
        send_data = {
            "order" : "TTS",
            "query" : speech
        }
        await websocketSend('react', json.dumps(send_data))
        tts(speech["content"])
        send_data = {
                        "order" : "TTS_end",
                        "query" : None
                    }
        await websocketSend('react', json.dumps(send_data))

    # 해줄말이 없다면 그냥 인사만
    else :
        send_data = {
            "order" : "TTS",
            "query" : {
                "content" : "TTS",
                "query" : {
                    "content" : f"{user_name}님 안녕하세요",
                    "type" : "hello"
                }

            }
        }
        await websocketSend('react', json.dumps(send_data))

        tts(f"{user_name}님 안녕하세요")

        send_data = {
                "order" : "TTS_end",
                "query" : None
            }
        await websocketSend('react', json.dumps(send_data))

    # 드디어 대기모드
    STATUS = WAITTING

async def callSpeech(user_email):
    print("서버에 유저 데이터 요청")

    URL_MENT = "http://i9e101.p.ssafy.io:8080/api/iot/text/first?userEmail="

    response = requests.get(URL_MENT + user_email)
    response = response.json()

    print(response)

    if response.get('success'):
        if response["response"] != None:
            text_code = response["response"]["textCode"]
            text_content = response["response"]["textContent"]

            return {
                "content" : text_content,
                "type" : text_code
            }
    
    return False


async def disappear(*arg):
    global STATUS
    if STATUS == WAITTING:
        # 이건 리눅스에서만 기능한다.
        # os.system("xset dpms force off")
        print("screen_off")
        # 스피커와 카메라로 사용 종료 보내기
        await websocketSend('audio', 'audio_end')
        send_data = {
            "order" : "logout",
            "query" : None
        }
        await websocketSend('video', json.dumps(send_data))


        STATUS = SCREEN_OFF

async def left(*arg):
    send_data = {
        "order" : "LEFT",
        "query" : None
    }

    await websocketSend('react', json.dumps(send_data))

async def right(*arg):
    send_data = {
        "order" : "RIGHT",
        "query" : None
    }

    await websocketSend('react', json.dumps(send_data))

async def mainUI(*arg):
    global STATUS
    STATUS = WAITTING
    send_data = {
        "order" : "EXIT",
        "query" : None
    }

    await websocketSend('react', json.dumps(send_data))

async def websocketSend(target, data):
    if client_role.get(target):
        await client[client_role[target]].send(data)

order_fun = {"CALL" : call,
            "MESSAGESEND" : messageSend,
            "MESSAGESHOW" : messageShow,
            "WEATHER" : weather,
            "NEWS" : news,
            "YOUTUBE" : youtube,
            "CANTUNDERSTAND" : chatgpt,
            "left": left,
            "right": right,
            "recoding_end": messageEnd,
            "appear": appear,
            "disappear": disappear,
            "exit" : mainUI
            }




async def main():
    await asyncio.gather(
        hearOrder("audio"),
        hearOrder("video"),
        doOrder(),
    )

###############################################################################################
###############################################################################################

# try:
#     get_user_face.getUserFaceImage()
#     print("make face image finished")
# except:
#     print("error")

# print("find user")
# my_name = find_user.getUserName()
# print("user :", my_name)

###############################################################################################
###############################################################################################


# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998)
# 비동기로 서버를 대기한다.
# threading.Thread(target = serialArduino).start()
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()


