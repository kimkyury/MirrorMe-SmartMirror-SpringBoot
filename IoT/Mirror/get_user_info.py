import requests
import base64
import json
from PIL import Image
import base64
from io import BytesIO

def encryption(Sentence : str, n : int, e : int) -> str:
    return "".join([chr(pow(i,e,n)) for i in base64.b64encode(Sentence.encode('utf-8'))])

def decryption(Sentence : str, n: int, d: int) -> str:
    return base64.b64decode("".join([chr(pow(j,d,n)) for j in [ord(i) for i in Sentence]])).decode('utf-8')

def decode_base64_image(base64_string):
    # base64 문자열을 디코딩하여 이미지 바이너리 데이터로 변환
    image_data = base64.b64decode(base64_string)
    # BytesIO를 사용하여 이미지 바이너리 데이터를 이미지 객체로 변환
    image = Image.open(BytesIO(image_data))
    return image

def save_image_as_png(image, output_filename):
    # 이미지를 PNG 확장자로 저장
    image.save(output_filename, format='png')


# 테스트용 코드
if __name__ == '__main__':
    URL = "http://i9e101.p.ssafy.io:8080/api/iot/users"
    RSA_N = 20453
    RSA_E = 20053

    # 서버팀에 보내고자 하는 것을 key - value 형식으로 작성. 작성한 것을 temp라는 변수에 대입
    # 모두 소문자로 구성해줄 것
    temp = encryption("6rBZ68bBiJ46ntHGBfJP",RSA_N,RSA_E)
    params = {
        "mirrorId": temp,
    }
    print(params)
    headers = {"Content-Type": "application/json"}

    # 보내고자 하는 Data를 JSON 형식으로 변환 (GET에서는 변환 불 필요)
    data = json.dumps(params)

    # JSON 데이터를 포함하여 GET 요청을 보냄
    response = requests.post(URL, headers=headers, data=data)

    # 송신 결과 확인
    rdata = response.json()
    user_info_list = rdata['response']

    for user in user_info_list:
        if user["profileImage"] != None:
            img_out = decode_base64_image(user["profileImage"])
            save_image_as_png(img_out,f'./Video_client/Recognition/Image/{user["userName"]}.png')
        user.pop("profileImage",None)

    # Create a JSON file
    info_json = json.dumps(user_info_list)
    with open("./" + "user_data" + ".json", "w") as f:
        f.write(info_json)