#!/bin/bash

# 날짜 포맷을 지정하기 위한 함수

get_formatted_date() {
	date +%y%m%d%H%M
}

# 폴더명을 날짜로 지정
folder_name=$(get_formatted_date)

# 새로운 폴드 생성
mkdir -p "$folder_name"

# 새로운 폴더로 데이터를 옮김
mv temp/* "$folder_name"

# 권한이 너무 높으면 안됨
chmod 600 I9E101T.pem

# scp 명령어로 파일 전송
scp -i I9E101T.pem -r "$folder_name" ubuntu@i9E101.p.ssafy.io:/home/ubuntu/message/

# 폴더 삭제
rm -r "$folder_name"
