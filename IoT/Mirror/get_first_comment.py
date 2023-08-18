###############################################################################################
###############################################################################################
import requests

print("서버에 유저 데이터 요청")

URL_MENT = "http://i9e101.p.ssafy.io:8080/api/iot/text/first?userEmail="

response = requests.get(URL_MENT + "aeae23")

if response.json()["success"]:
    text_code = response.json()["response"]["textCode"]
    text_content = response.json()["response"]["textContent"]
    print(text_code, text_content)

print("데이터 수신 완료")
