- 처음에 유저를 인식하였을때

  ```json
  {
      "order" : "userInfo",
      "query" : {
          "userId" : id값,
          "userEmail" : email주소
      }
  }

order로 userInfo를 받으면 쿼리값을 video_main에 전역변수로 저장해 둘 예정

- 음성 혹은 비디오 메세지를 전송할 때

  ```json
  {
      "order" : "video_start" or "audio_start",
      "query" : {
      	"target_user" : 받는사람 email 주소
  	}
  }
  ```

이미 전역변수로 로그인 유저의 정보를 가지고 있으므로 어떤 타입의 메세지를 전송할지와 받는 사람 주소만 있으면 됨.

- 유저 로그아웃

  ```json
  {
  	"order" : "logout",
  	"query" : {
  		"result" : succes 이런식으로 뭐 성공여부만 나타내면 될듯?
  	}
  }
  ```

로그아웃 신호를 받으면 전역변수 초기화