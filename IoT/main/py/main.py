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


###############################################################################################
###############################################################################################
# 서버에서 유저 데이터 받아오기

from get_user_info import encryption, decryption, decode_base64_image, save_image_as_png
import requests
# 장치 고유 시리얼 넘버
DEVICE_SERIAL_CODE = '6rBZ68bBiJ46ntHGBfJP'
URL_USER_DATA = "http://i9e101.p.ssafy.io:8080/api/iot/users"
RSA_N = 119
RSA_E = 43


# 서버팀에 보내고자 하는 것을 key - value 형식으로 작성. 작성한 것을 temp라는 변수에 대입
# 모두 소문자로 구성해줄 것

print("서버에 유저 데이터 요청")
temp = encryption("6rBZ68bBiJ46ntHGBfJP",RSA_N,RSA_E)
params = {
    "mirrorId": "SxdePkscFV4HJzRLE18eXF5mJ2w=",
}
headers = {"Content-Type": "application/json"}

# 보내고자 하는 Data를 JSON 형식으로 변환
data = json.dumps(params)

# JSON 데이터를 포함하여 POST 요청을 보냄
response = requests.post(URL_USER_DATA, headers=headers, data=data)

# 송신 결과 확인
rdata = response.json()
user_info_list = rdata['body']['usersInSameHousehold']

for user in user_info_list:
    if user["profileImage"] != None:
        img_out = decode_base64_image(user["profileImage"])
        save_image_as_png(img_out,f'./Video_client/Recognition/Image/{user["userName"]}.png')
    user.pop("profileImage",None)

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
    except TimeoutError:
        await websocket.send("연결시간 초과")
        await websocket.close()
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
    session_id = str(uuid.uuid4())
    client[session_id] = websocket

    # 연결 되었음을 알리고 역할에 따른 세션아이디 저장
    connect_check[role].set()
    client_role[role] = session_id
    # 세션 코드 발급
    await websocket.send(session_id)

    # 따로 서버가 끊길때 까지 대기
    await websocket.wait_closed()
    del client[session_id]
    
###############################################################################################
###############################################################################################

SCREEN_OFF = 0
WAITTING = 1
CALL_MIRROR = 100
YOUTUBE = 101
MESSAGE_CAP = 102
MESSAGE_SHOW = 103

STATUS = WAITTING


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

        if order_fun.get(commend, False):
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
    
    # 보내는 대상은  target에 저장되어 있음
    target = arg[0]

    send_data = {
        "order" : "MESSAGESENDSTART",
        "query" : {
            "target" : target
        }
    }
    # 리엑트가 접속 했을 때만 전송
    if client_role.get("react", False):
        await client[client_role["react"]].send(json.dumps(send_data))

    tts(f"{target}님께 보낼 영상메세지 촬영을 시작합니다.")
    STATUS = MESSAGE_CAP
    # 메세지 녹화 동기로 실행
    # audio와 video측에 알려서 연결을 끊고 녹화를 시작하도록함
    # 그 다음 종료시 다시 audio와 video측에서 다시 연결

    # 메세지 녹화 종료를 리엑트로 알림
    send_data = {
        "order" : "MESSAGESENDEND",
        "query" :None
    }

    if client_role.get("react", False):
        await client[client_role["react"]].send(json.dumps(send_data))


    # 이후 저장된 영상데이터를 백엔드 측으로 보내 줘야 됨
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

    if client_role.get("react", False):
        await client[client_role["react"]].send(json.dumps(send_data))

    STATUS = MESSAGE_SHOW
    tts("메세지를 보여드릴게요")

    # 메세지 보기 처리

    # 리엑트 측으로 부터 영상이 종료되었음을 수신
    if client_role.get("react", False):
        await client[client_role["react"]].recv()

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
    if client_role.get("react", False):
        await client[client_role["react"]].send(json.dumps(send_data))


    STATUS = YOUTUBE
    tts(f"{youtube_key}관련 유튜브 영상을 재생해 드릴게요")
    #########################################
    # 유튜브 종료 대기
    # 리엑트 측에서 유튜브 영상이 끝났음을 수신
    if client_role.get("react", False):
        await client[client_role["react"]].recv()

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
    if client_role.get("react", False):
        await client[client_role["react"]].send(json.dumps(send_data))

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
    global STATUS
    STATUS = WAITTING

    # 얼굴 인식 처리
    # 처리 후 정보를 react로 보내야 됨

    pass
# 없어지면 
async def disappear(*arg):
    global STATUS
    if STATUS == WAITTING:
        # 이건 리눅스에서만 기능한다.
        # os.system("xset dpms force off")
        # 스피커와 카메라로 사용 종료 보내기

        STATUS = SCREEN_OFF

async def left(*arg):
    pass

async def right(*arg):
    pass


order_fun = {"CALL" : call,
            "MESSAGESEND" : messageSend,
            "MESSAGESHOW" : messageShow,
            "WEATHER" : weather,
            "NEWS" : news,
            "YOUTUBE" : youtube,
            "CANTUNDERSTAND" : chatgpt,
            "LEFT": left,
            "RIGHT": right}


# async def serialArduino():
#     py_serial = serial.Serial(port="COM4", baudrate=9600,)

#     while True:
#         if py_serial.readable():
#             response = py_serial.readline()
#             order.put(response.decode())



async def main():
    await asyncio.gather(
        hearOrder("audio"),
        hearOrder("video"),
        doOrder(),
        # serialArduino(),
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
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()


