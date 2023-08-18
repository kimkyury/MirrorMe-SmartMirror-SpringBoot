# 1. 빌드 시 사용되는 환경 변수 등의 주요 내용 상세 기재

## 1️⃣ 사용한 JVM, 웹서버, WAS 제품 등의 종류, 설정값, 버전

| Name | Value | 
| --- | --- | 
| java | 11 |
| Spring Boot (gradle) | 2.7.13 | 
| MariaDB | 10.11 |
| Redis | 7.0 |
| IntelliJ | 2019.3.5,  2023.01.03 |
| Frontend 웹 서버 | Docker + Nginx |
| Backend 웹 서버 | Docker |
| WAS | Apache Tomcat |
| Docker | 24.0.4 |

| Name | Value |
| --- | --- |
| Device | Lttepanda 3 Delta |
| Os | Ubuntu 22.04 |
| Python | 3.10.12 |
| opencv-contrib-python | 4.8.0.74 |
| tensorflow-gpu | 2.9.0 |
| cuda | 11.2 |
| Django | 3.2.18 |



## 2️⃣ 빌드 시 사용되는 환경 변수 등의 주요 내용 상세 기재

### Frontend

1. Git 설치 및 연동(**/home/ubuntu 경로에서**)
   
    ```java
    apt-get install git
    git clone https://lab.ssafy.com/s09-webmobile3-sub2/S09P12E101.git
    # 로그인
    ```
    
2. docker-compose.yml 파일 실행
   
    ```java
    docker-compose up -d
    ```
    
    - docker-compose.yml 파일
    
    ```java
    version: "3.7"
    
    services:
      nginx:
        image: woneee99/nginx
        restart: always
        container_name: nginx
        build:
          context: ./
          dockerfile: Dockerfile
        ports:
          - "80:80"
        networks:
          - frontend
      client:
        build:
          context: ./ 
          dockerfile: Dockerfile
        networks:
          - frontend  
    networks:
      frontend:
        driver: bridge
    ```
    

### Backend

- backend/src/main/resources/application.yml 파일 추가
  
    ```java
    spring:
      datasource:
        url: jdbc:mariadb://i9e101.p.ssafy.io:3306/mlm
        driver-class-name: org.mariadb.jdbc.Driver
        username: ${MARIADB_USER}
        password: ${MARIADB_PASSWORD}
      redis:
        host: i9e101.p.ssafy.io
        port: 6379
        password: ${REDIS_PASSWORD}
      jpa:
        generate-ddl: true
        show-sql: true
    
    google:
      client-id: ${CLIENT_ID}
      client-secret: ${CLIENT_SECRET}
      redirect-uri: <http://i9e101.p.ssafy.io:8080/oauth/google/callback>
    
    iot:
      N: ${N}
      E: ${E}
      D: ${D}
    
    server:
      address: 0.0.0.0
      port: 8090
    
    data:
      service-key: ${SERVICE_KEY}
    
    chatgpt:
      api-key: ${CHAT}
    
    ```
    
- build 과정
    - 등록된 환경변수를 포함시켜 build 진행
    
    ```java
    ./gradlew build -PN=20453 -PE=20053 -PD=16957 -PMARIADB_USER=root -PMARIADB_PASSWORD=mlmMDB6 -PMARIADB_ROOT_PASSWORD=mlmMDB6 -PREDIS_PASSWORD=woneee99 -PCLIENT_ID="627028807402-fobgohrdmv1ov823iiij7omtp89p2onb.apps.googleusercontent.com" -PCLIENT_SECRET=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 -PSERVICE_KEY=%2FoTPUAndmigHQ%2BpPwXOuYoVbqfXclp89LQ0mnAeXcFidTxdpxB9h9c2qIbJGNqkIFfkQgFeWqU4cLC3%2FHu%2BkMQ%3D%3D -PCHAT=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 -PTZ=Asia/Seoul
    ```

### IoT

- google 인증

1. **Google Cloud Platform Console에서 프로젝트를 만듭니다.**

  아직 프로젝트를 만들지 않았다면 지금 만드세요. 프로젝트를 사용하면 배포, 액세스 제어, 청구, 서비스를 포함하여 앱의 모든 Google Cloud Platform 리소스를 관리할 수 있습니다.

  i. [클라우드 플랫폼 콘솔](https://console.cloud.google.com/)을 엽니다 .

  ii. 상단의 드롭다운 메뉴에서 프로젝트 만들기를 선택합니다.

  iii. 프로젝트에 이름을 지정하십시오.

  iv. 프로젝트 이름과 다를 수 있는 프로젝트 ID를 기록해 둡니다. 프로젝트 ID는 명령 및 구성에서 사용됩니다.

2. **프로젝트에 대한 결제를 활성화합니다.** 

   프로젝트에 대한 결제를 아직 활성화하지 않은 경우 [지금 결제를 활성화하십시오](https://console.cloud.google.com/project/_/settings) . 청구를 활성화하면 애플리케이션이 Speech API 호출과 같은 청구 가능한 리소스를 사용할 수 있습니다. [결제 설정에 대한 자세한 내용은 Cloud Platform 콘솔 도움말](https://support.google.com/cloud/answer/6288653)을 참조하세요 .

3. **프로젝트에 대한 API를 활성화합니다.** [여기를 클릭](https://console.cloud.google.com/flows/enableapi?apiid=speech&showconfirmation=true)하여 Cloud Platform Console을 방문하고 Speech API를 사용 설정하세요.

4. **필요한 경우 결제 프로젝트를 재정의합니다.** [인증을 위해 사용자 계정을](https://cloud.google.com/docs/authentication#principals) 사용하는 경우 GOOGLE_CLOUD_CPP_USER_PROJECT 환경 변수를 이전 단계에서 생성한 프로젝트로 설정해야 합니다 . serviceusage.services.use프로젝트에 대한 권한이 있어야 합니다 . 또는 다음에 설명된 대로 서비스 계정을 사용합니다.

5. **서비스 계정 사용자 인증 정보를 다운로드합니다.** 이러한 샘플은 인증을 위해 서비스 계정을 사용할 수 있습니다.

  i. [Cloud Console](http://cloud.google.com/console)을 방문 하고 다음으로 이동합니다. `API Manager > Credentials > Create credentials > Service account key`

  ii. **Service account** 에서 `New service account`을 선택합니다.

  iii. **Service account name** 아래에 선택한 서비스 계정 이름을 입력합니다. 예를 들어, `transcriber`.

  iv. **Role** 에서 `Project > Owner`을 선택합니다 .

  v. **Key type** 아래에서 선택된 상태로 둡니다 `JSON`.

  vi. **Create**를 클릭하여 새 서비스 계정을 만들고 json 자격 증명 파일을 다운로드합니다.

  vii.다운로드한 서비스 계정 자격 증명을 가리키도록 환경 변수를 설정합니다 .

  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
  ```
  자세한 내용은 [Cloud Platform 인증 가이드](https://cloud.google.com/docs/authentication#developer_workflow)를 참조하세요 .




- crontab 설정 (./Video_Client/Message/ 에서)

```bash
crontab -e
```

```bash
*/30 * * * * ./send_message.sh
```

```bash
chmod +x ./send_message.sh
```



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



- ngrok (CPU AVX 미지원 시, ngrok로 외부서버 이용)

ngrok 파일 실행 후

```
ngrok http 8000
```

![ngrok](https://i.ibb.co/C0dCQ9t/image.png)

orwarding의 주소를 Django settings.py에 추가

```django
ALLOWED_HOSTS = [$]
```



- ai처리 서버

```
pip3 install django
pip3 install tensorflow==2.9.0
python manage.py runserver
```



## 3️⃣ 배포시 특이사항 기재

### Frontend

- Dockerfile을 통해 build (Nginx와 연결)
  
    ```java
    FROM node:18.16.0-alpine as builder
    WORKDIR /app
    COPY package.json ./
    RUN npm i
    COPY ./ ./
    RUN npm run build
    
    FROM nginx 
    COPY --from=builder /app/build /usr/share/nginx/html
    ```
    

### Backend

- 배포할 파일 경로에서 docker image build 및 image upload
  
    ```java
    docker build -t woneee99/iot .
    docker push woneee99/iot
    ```
    
- ec2 서버에서 image 받아온 후, docker compose로 container background에서 실행
  
    ```java
    docker pull woneee99/iot:latest
    docker-compose up -d
    ```

## 4️⃣ DB 접속 정보 등

### MariaDB

- DB 명: mlm
- USER: root
- PASSWORD: mlmMDB6

**프로퍼티**

- -character-set-server=utf8mb4
- -collation-server=utf8mb4_unicode_ci

### Redis

- HOST: [i9e101.p.ssafy.io](http://i9e101.p.ssafy.io/)
- PORT: 6379
- PASSWORD: woneee99
