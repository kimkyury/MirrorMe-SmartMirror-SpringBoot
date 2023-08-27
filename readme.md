# <center>  Outline of MirrorMe </center>
- 제작기간 : 2023년 7월 4일 2023(Tue) ~ 2023년 8월 18일(Fri)
- 프로젝트 주제: **가족 소통**을 위한 **스마트미러**
- 팀 명: 1OT(One of Team)
- 서비스명: *MirrorMe (MLM)*

## 👨‍👩‍👧‍👦 Outline of 1OT
- IOT : 신성환(팀장), 김성현 ( 🛩 [IOT 상세 README](https://lab.ssafy.com/s09-webmobile3-sub2/S09P12E101/-/tree/master/IoT) )
- BACKEND: 김규리, 황주원 ( 🛩 [BACKEND 상세 README](https://lab.ssafy.com/s09-webmobile3-sub2/S09P12E101/-/tree/master/Backend) )
- FRONTEND: 이소정, 이진형 ( 🛩 [FRONTEND 상세 README](https://lab.ssafy.com/s09-webmobile3-sub2/S09P12E101/-/tree/master/Frontend) ) 


## 😎 About Service of MLM
### Application
- Application에서 GoogleOAuth로 로그인을 진행합니다.
- 사용자는 간단히 자신의 프로필(사진포함)/집안 정보를 기입하고, SmartMirror의 QR을 인식합니다. (프로필 사진은 IOT서버 내의 openCV로 학습되어 FaceID가 생성됩니다.)
- 이후 사용자가 Application 로그인시 다음과 같은 페이지를 조회할 수 있습니다.

***- Application 내의 페이지 목록***
1. 가정 위치 기반 날씨 정보 & 개인 일정 조회 페이지
2. SmartMirror에서 촬영된 영상비디오 조회/저장 페이지
3. 그래프를 통한 데일리 감정 기록 조회 페이지
4. 연락 횟수에 대한 가족 마음 온도 조회 페이지

### Mirror
- 사용자가 나타나면 Application정보로 만들어진 faceID를 통해 사용자를 인식합니다
- 해당 사용자의 가정에 대한 날씨정보를 Mirror의 UI로 출력합니다.
- 해당 사용자에게 맞춤형 인사, 비서 음성을 출력합니다.
    - ✔ *감정 기반, 전 날에 화나거나 슬픈 감정이 있는 구성원에 대한 정보 알림* 
    - ✔ *가족 이벤트(생일과 같은) 존재시 해당 구성원의 일정기반 선물 추천 알림*
    - ✔ *Google Calendar내의 일정들을 요약한 3줄 정리 알림*
    - ✔* 수신된 영상비디오에 대하여 조회 권유 알림*
- 사용자의 음성 요청시 해당 요구사항을 수행합니다.
    - ✔ *사용자의 유투브 영상 출력 요구시 수행*
    - ✔ *사용자의 영상메시지 촬영 요구시 수행*

## 👀 MLM Action Sequence Diagram
![title](./imgForReadme/MLM-SequenceDiagram.png)   


## 🙋‍♀️ MLM Technology Stach Diagram
![title](./imgForReadme/MLM-SkillDiagram.png)   
