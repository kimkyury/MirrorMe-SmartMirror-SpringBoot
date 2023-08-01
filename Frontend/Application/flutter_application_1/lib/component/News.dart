import 'package:flutter/material.dart';

class News extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        Container( // 키워드 별 컨테이너 한 개
          padding: EdgeInsets.all(10),
          height: 130,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row( // 키워드 제목
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    child: Row(
                      children: [
                        Icon(Icons.sports_football, color: Colors.black,),
                        Text('스포츠', style: TextStyle(
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500
                        ),),
                      ],
                    ),
                  ),
                  Text('업데이트 시간') // 추후 업데이트 시간으로 변경
                ],
              ),
              Container( // 기사 목록
                child: Column(
                children: [
                  Row( // 뉴스 기사 1
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 2
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 3
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                ],
                ),
              ),
            ],
          ),
        ),
        
        Container( // 키워드 별 컨테이너 한 개
          padding: EdgeInsets.all(10),
          height: 130,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row( // 키워드 제목
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    child: Row(
                      children: [
                        Icon(Icons.computer, color: Colors.black,),
                        Text('IT/과학', style: TextStyle(
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500
                        ),),
                      ],
                    ),
                  ),
                  Text('업데이트 시간') // 추후 업데이트 시간으로 변경
                ],
              ),
              Container( // 기사 목록
                child: Column(
                children: [
                  Row( // 뉴스 기사 1
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 2
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 3
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}