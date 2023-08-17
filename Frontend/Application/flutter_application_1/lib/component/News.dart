import 'package:flutter/material.dart';
import './NewsTab.dart';

class News extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SizedBox(height: 20,),
        // 우리 가족 목록
        Container(
          padding: EdgeInsets.all(10), // 수정된 부분
          width: 350,
          height: 161,
          margin: EdgeInsets.symmetric(horizontal: 20), // 수정된 부분
          child: Column(
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
                              SizedBox(width: 10,),
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
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                        Row( // 뉴스 기사 2
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                        Row( // 뉴스 기사 3
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                      ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(14),
            boxShadow: [
              BoxShadow(
                color: Color(0x29000000),
                offset: Offset(0, 1),
                blurRadius: 6,
                spreadRadius: 0,
              ),
            ],
          ),
        ),
        SizedBox(height: 20,),

        Container(
          padding: EdgeInsets.all(10), // 수정된 부분
          width: 350,
          height: 161,
          margin: EdgeInsets.symmetric(horizontal: 20), // 수정된 부분
          child: Column(
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
                              Icon(Icons.computer, color: Colors.black,),
                              SizedBox(width: 10,),
                              Text('IT/과학', style: TextStyle(
                                color: Colors.black,
                                fontSize: 23,
                                fontFamily: 'NanumSquareRoundEB',
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
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                        Row( // 뉴스 기사 2
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                        Row( // 뉴스 기사 3
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text('기사 제목 줄여서 출력하기 위한 예시...'),
                            Text('언론사')
                          ],
                        ),
                      ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(14),
            boxShadow: [
              BoxShadow(
                color: Color(0x29000000),
                offset: Offset(0, 1),
                blurRadius: 6,
                spreadRadius: 0,
              ),
            ],
          ),
        ),
      ],
    );
  }
}
