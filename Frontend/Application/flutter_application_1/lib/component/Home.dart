import 'package:flutter/material.dart';
import './todayweather.dart';
import './weekweather.dart';

class Home extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    // 홈 컴포넌트의 내용을 작성
    return ListView(
      children: [
        SizedBox(height: 20,),
        // 날씨
        Container(
          width: 350,
          height: 360,
          margin: EdgeInsets.only(
            left: 20,
            right: 20,
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
          child: Column(
            children: [
              SizedBox(height: 10,), ////////////////////// 상세 조정 필요////////////////////////
              TodayWeather(), // 일간 날씨
              Divider( // 가로 선 추가
                color: Color(0xFF171717),
                height: 0,
                thickness: 1,
                indent: 15, // 선 좌측 여백
                endIndent: 15, // 선 우측 여백
              ),
              WeekWeather(), // 주간 날씨
              SizedBox(height: 10,), ////////////////////// 상세 조정 필요////////////////////////
            ],
          ),
        ),
        SizedBox(height: 20,),
        Container(
          // 오늘 일정
          padding: EdgeInsets.all(10),
          height: 150,
          margin: EdgeInsets.only(
            left: 20,
            right: 20,
          ),
          child: Column(
            children: [
              Container(
                // 제목
                margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text('Today ',
                      style: TextStyle(
                        color: Color(0xff111111),
                        fontSize: 20,
                        fontFamily: 'NanumSquareRoundOTFEB',
                        fontWeight: FontWeight.w400,
                        fontStyle: FontStyle.normal,
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
                  ],
                ),
              )
            ],
          ),
        ),
        SizedBox(height: 20,),
        Container(
          // 할 일
          padding: EdgeInsets.all(10),
          height: 150,
          margin: EdgeInsets.only(
            left: 20,
            right: 20,
          ),
          child: Column(
            children: [
              Container(
                // 제목
                margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text('Todo',
                      style: TextStyle(
                        color: Color(0xff111111),
                        fontSize: 20,
                        fontFamily: 'NanumSquareRoundOTFEB',
                        fontWeight: FontWeight.w400,
                        fontStyle: FontStyle.normal,
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
                  ],
                ),
              ),
              Container(
                // 일정 한 개
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(children: [
                        Icon(
                          Icons.circle,
                          color: Colors.red,
                          size: 15,
                        ),
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
                  ],
                ),
              )
            ],
          ),
        ),
      ],
    );
  }
}
