import requests
import base64
import json
import io
from PIL import Image
import base64
from io import BytesIO

def decode_base64_image(base64_string):
    # base64 문자열을 디코딩하여 이미지 바이너리 데이터로 변환
    image_data = base64.b64decode(base64_string)
    # BytesIO를 사용하여 이미지 바이너리 데이터를 이미지 객체로 변환
    image = Image.open(BytesIO(image_data))
    return image

def save_image_as_png(image, output_filename):
    # 이미지를 PNG 확장자로 저장
    image.save(output_filename, format='png')

URL = "http://192.168.30.142:8080/api/iot/users"

# 서버팀에 보내고자 하는 것을 key - value 형식으로 작성. 작성한 것을 temp라는 변수에 대입
# 모두 소문자로 구성해줄 것
params = {
    "mirrorId": "1",
}

headers = {"Content-Type": "application/json"}

# 보내고자 하는 Data를 JSON 형식으로 변환 (GET에서는 변환 불 필요)
data = json.dumps(params)

# JSON 데이터를 포함하여 GET 요청을 보냄
response = requests.post(URL, headers=headers, data=data)

# 송신 결과 확인
rdata = response.json()

imgdata = rdata['body']['usersInSameHousehold'][-1]['profileImage']
img_out = decode_base64_image(imgdata)
save_image_as_png(img_out,'./face_and_gesture/photo/'+'8.png')
