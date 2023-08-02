import requests
import json
import pprint

URL = "https://jsonplaceholder.typicode.com/users"

# 서버팀에 보내고자 하는 것을 key - value 형식으로 작성. 작성한 것을 temp라는 변수에 대입
# 모두 소문자로 구성해줄 것
params = {
    "mirror_id": "PwMlwGkZ88",
}

# 보내고자 하는 Data를 JSON 형식으로 변환 (GET에서는 변환 불 필요)
# data = json.dumps(params)

# JSON 데이터를 포함하여 GET 요청을 보냄
response = requests.get(URL, params=params)

# 송신 결과 확인
print(response.json())