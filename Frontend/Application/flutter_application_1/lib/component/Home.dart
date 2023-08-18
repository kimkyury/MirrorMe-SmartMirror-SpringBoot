import 'package:flutter/material.dart';

import './Tasks.dart';
import './Schedules.dart';
import './TodayWeather.dart';
import './WeekWeather.dart';


class Home extends StatelessWidget {
  final String accessToken;
  final String refreshToken;

  Home({required this.accessToken, required this.refreshToken});

  @override
  Widget build(BuildContext context) {
    // 홈 컴포넌트의 내용을 작성
    return SingleChildScrollView(
      child: Container(
        color: Colors.white,
        child: Column(
          children: [
            SizedBox(height: 20,),
            // 날씨
            Container(
              width: 350,
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
                  // Divider( // 가로 선 추가
                  //   color: Color(0xFF171717),
                  //   height: 0,
                  //   thickness: 1,
                  //   indent: 15, // 선 좌측 여백
                  //   endIndent: 15, // 선 우측 여백
                  // ),
                  // WeekWeather(), // 주간 날씨
                  SizedBox(height: 10,), ////////////////////// 상세 조정 필요////////////////////////
                ],
              ),
            ),
            SizedBox(height: 20,),
            Schedules(
              accessToken: accessToken,
              refreshToken: refreshToken,         
            ),
            Divider(height: 10,),
            SizedBox(height: 20,),
            Tasks(
              accessToken: accessToken,
              refreshToken: refreshToken, 
            ),
          ],
        ),
      )
      
    );
  }
}
