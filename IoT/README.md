<center><h1>Outline of IoT</h1></center>


Duration : July 4, 2023 (Tue) ~ August 18, 2023 (Fri)

Theme : Smart Mirror for Family Communication

Service Name : ***MirrorMe (MLM)***

Member : :angel:ShinSeongHwan, :skull:KimSungHyun



## :computer:Development Environment

Device : Lttepanda 3 Delta

Os : Ubuntu 22.04

Python : 3.10.12

opencv-contrib-python : 4.8.0.74

google-api-core : 2.11.1

tensorflow-gpu : 2.9.0

cuda : 11.2

Django : 3.2.18



## :bookmark_tabs:Installation

- 메인서버 실행

```bash
pip3 install -r main_requirement.txt
python3 main.py
```

- AISpeaker 연결

```bash
pip3 install -r aispeaker_requirement.txt
python3 AISpeaker_Client/aispeaker.py
```

- Video 연결

```bash
pip3 install -r video_requirement.txt
python3 Video_Client/video_main.py
```

- crontab 설정

```bash
crontab -e
```

```bash
*/30 * * * * ./send_message.sh
```

```bash
chmod +x ./send_message.sh
```

- ai처리 서버

```
pip3 install django
pip3 install tensorflow==2.9.0
python manage.py runserver
```

- ngrok

```
ngrok http 8000
```



## 📺File Path

```
Mirror
├ Ai_Server
├ AISpeaker_Client
│├ aispeaker.py
│├ nlp.py
│├ stt_streaming.py
│└ tts.py
├ Serial_Arduino
│├ serial_arduino
││└ serial_arduino.ino
│└ serial_client.py
├ Video_Client
│├ Message
││├ To_Be_Sent
││├ audio_recoding.py
││├ I9E101T.pem
││├ merge_video.py
││├ send_message.sh
││└ video_recoding.py
│├ Models
││├ best_black_model.h5
││├ emotion_model.hdf5
││└ haarcascade_frontalface_default.xml
│├ Recognition
││├ Face_Image
││├ Image
││├ find_user.py
││└ get_user_face.py
│├ video_main.py
│└ video_query.md
├ aispeaker_requirement.txt
├ get_first_comment.py
├ get_user_info.py
├ main.py
├ main_requirement.txt
└ video_requirement.txt
```



## 🧬Architecture Diagram

![Architecture](https://i.ibb.co/pnZfQYb/IoT-di.png)



## ⚙Tech

- Open CV와 Face_recognition을 활용한 얼굴 인식 및 사용자 확인

- Open CV, Pyaudio를 활용한 영상/음성 메세지 녹화 및 Moviepy를 활용한 인코딩

- Open CV와 Mideapipe를 활용한 gesture_recognition 

- Shell script를 활용한 SCP 작성, crontab 스케쥴로 실행하여 ec2서버로 영상/음성메세지 저장

- [한국인 표정 감정 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=82)를 활용한 [CNN 모델](https://i.ibb.co/XxGSX8R/model-plot.png) 설계Tensor Flow를 활용한 감정 AI 학습 및 keras로 모델 적용

  ```
  _________________________________________________________________
   Layer (type)                Output Shape              Param #
  =================================================================
   conv2d (Conv2D)             (None, 254, 254, 32)      320
  
   max_pooling2d (MaxPooling2D  (None, 127, 127, 32)     0
   )
  
   conv2d_1 (Conv2D)           (None, 125, 125, 64)      18496
  
   max_pooling2d_1 (MaxPooling  (None, 62, 62, 64)       0
   2D)
  
   conv2d_2 (Conv2D)           (None, 60, 60, 64)        36928
  
   dropout (Dropout)           (None, 60, 60, 64)        0
  
   flatten (Flatten)           (None, 230400)            0
  
   dense (Dense)               (None, 256)               58982656
  
   dropout_1 (Dropout)         (None, 256)               0
  
   dense_1 (Dense)             (None, 128)               32896
  
  =================================================================
  Total params: 59,071,296
  Trainable params: 59,071,296
  Non-trainable params: 0
  _________________________________________________________________
  
  ```


![Emotion](https://i.ibb.co/dgLs2ty/GIF-2023-08-16-11-22-03.gif)  <--- 감정 분석 ai 사용 예

- RSA암호화 및 복호화 알고리즘 작성

```python
def Encryption(Sentence : str, n : int, e : int) -> str:
    return "".join([chr(pow(i,e,n)) for i in base64.b64encode(Sentence.encode('utf-8'))])

def Decryption(Sentence: str, n: int, d: int) -> str:
    return base64.b64decode("".join([chr(pow(j,d,n)) for j in [ord(i) for i in Sentence]])).decode('utf-8')
```

- Lattepanda CPU가 AVX 미지원으로 django를 사용한 감정 AI 서버 작성 및 ngrok으로 임시 포트 포워딩
- Socket 통신, RestAPI 수신, Serial 통신
- 코루틴 구분을 통한 명령관리 및 수행

- Google Cloud 플랫폼을 통한 STT, TTS, NLP



## :foggy:Role

- ShinSeongHwan
  - Make smart mirror
  - Face_recognition and gesture_recognition
  - Recording video and voice messages and SCP (Secure Copy) to ec2
  - RSA encryption/decryption
  - Emotion_recognition Ai development and django server setup
- KimSungHyun
  - Make smart mirror
  - Implementation of AI Speaker
  - Websocket connection to react
  - State management of smart mirror



## :man_factory_worker:Manufacturing Process

1. 재료 구매

   - 액자, 중고 모니터, 반사필름

     <div class="separator" style="clear: both;">
     	<img src="https://i.ibb.co/1qP1j1W/Kakao-Talk-20230817-235116487.jpg" alt="case" style="zoom:50%;" />
     	<img src="https://i.ibb.co/Fbpqrdj/2640371-3.jpg" alt="monitor" style="zoom:40%;" />
     	<img src="https://i.ibb.co/MNgPqd9/1231323.png" alt="film" style="zoom:40%;" />
     </div>

2. 모니터 베젤 제거

   <img src="https://i.ibb.co/P95gCp4/1.gif" alt="vezel" style="zoom:67%;" /> 

3. 디스플레이 공간 외 빛 차단

   <img src="https://i.ibb.co/z7kDkQR/2.gif" alt="taping" style="zoom:67%;" /> 

4. 디스플레이 고정

   <img src="https://i.ibb.co/gWZnLVB/3.gif" alt="silicon" style="zoom:67%;" /> 

5. 블럭 부착 및 기판 고정

   <div class="separator" style="clear: both;">
   	<img src="https://i.ibb.co/HLSnpGM/4.gif" alt="block" style="zoom:67%;" />
   	<img src="https://i.ibb.co/zXrkqzG/4-5.gif" alt="bolt" style="zoom:67%;" />
   </div>

6. 빈 공간 메우기

   ![](https://i.ibb.co/0sqBCdN/5.gif) 

7. 완성

   <div class="separator" style="clear: both;">
   	<img src="https://i.ibb.co/ZWg3Mr0/Kakao-Talk-20230818-004023132.jpg" alt="" style="zoom:10%;" />
   	<img src="https://i.ibb.co/996Bhrc/Kakao-Talk-20230818-004023132-01.jpg" alt="monitor" style="zoom:10%;" />
   </div>



## 🎡Process

### Shin Seong Hwan

##### 7월 24일 (월)

- 아두이노를 통한 초음파 센서 코드를 작성

- 우분투 환경 및 기타 환경 세팅

##### 7월 25일 (화)
- 메인 서버 코드(C++) 작성
- Serial 통신 시도
- 라떼판다에서 GPIO로 직접 접근 방법 모색

##### 7월 26일 (수)

- Open CV 빌드 및 환경 설정

- Open CV를 활용한 얼굴 인식 구현
- 동영상 녹화 저장(소리X)

##### 7월 27일 (목)

- vcpkg를 활용한 C++ 라이브러리 관리
- 음성 메세지 저장
- C++ 환경에서 REST API 방법 모색

##### 7월 28일 (금)

- GUI, AI를 사용에 용이하기 위해 C++환경에서 Python으로 변경

- REST API 통신 대신 SCP를 구현한 shell script를 통해 ec2 서버에 메세지 저장

##### 7월 31일 (월)

- 기존 코드 Python으로 재작성
- 영상 메세지 저장, moviepy로 인코딩

##### 8월 1일 (화)

- 얼굴 인식을 통한 사용자 구별 구현
- 제스쳐 인식 코드 작성
- 소켓통신을 구현
- 감정 데이터 셋 서칭

##### 8월 2일 (수)

- 기기 고유번호 생성 알고리즘 구현
- RSA 알고리즘 구현
- 사용자 데이터 요청 구현

- AI_Hub 한국인 감정 표정 데이터 다운로드 (800Gb)

##### 8월 3일 (목)

- Tensor Flow를 활용한 CNN model 설계

##### 8월 4일 (금)
- Web socket 통신으로 메인 서버와 연동
- 스레드 관리

##### 8월 7일 (월)

- 데이터 전처리 재 검토 & Callback을 통한 best model 저장

##### 8월 8일 (화)
- Ubuntu 환경에서 환경 세팅 및 오류 수정

##### 8월 9일 (수)

- 제스쳐 추가 및 감도조절
- 제스처 신호를 통한 신호 전송 작성

##### 8월 10일 (목)
- 데이터 라벨링 재 검토 및 전처리 과정 검토

##### 8월 11일 (금)
- 라벨링 완료 및 흑백 얼굴 사진으로 전처리 실행

##### 8월 14일 (월)
- 사진 Size 조절 및 모델 수정

##### 8월 16일 (수)

- 코드 리팩토링 및 카메라 접근 오류 수정

---

### Kim Sung Hyun

##### 7월 31일 (월)
- Google Cloud Platform의 STT, TTS, NLA와 API 통신 구현
- STT와 TTS를 연결하여 부름에 대답하는 형태로 구현

##### 8월 1일 (화)
- NLA를 통해 형태소를 구분하고 이를 통해서 명령 구분 구현

##### 8월 2일 (수)
- webSocket.io 테스트 서버 제작
- react와 통신 테스트

##### 8월 4일 (금)
- webSocket.io 테스트 서버 , AISpeaker, Video 연결 성공
- Python threading, asyncio 모듈 공식문서 학습

##### 8월 9일 (수)
- react와 통신 메세지 json key 결정후 webSocket.io 테스트 서버 적용
- nlp를 통해 구분된 명령을 Socket.io 서버에서 처리

##### 8월 10일 (목)
- Youtube search API 사용하여 검색 결과 영상의 key를 받아오기
- 거울 동작에 필요한 데이터 받아오는 기능 구현

##### 8월 11일 (금)
- 요청에 따라 AISpeaker에서  마이크 연결을 제어
- 거울의 추천, 안내 메세지 받아오기 기능 추가

##### 8월 14일 (월)
- 얼굴 인식 이후 인식된 사용자의 정보를 react와 video측으로 전달

##### 8월 15일 (화)
- 감정분석 API 임시배포

##### 8월 16일 (수)
- 아두이노 초음파 센서와 Serial통신
- 요청에 따라 Video에서 녹화와, 제스처 인식 등 기능 제어

