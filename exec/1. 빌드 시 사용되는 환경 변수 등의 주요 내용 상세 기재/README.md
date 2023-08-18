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
