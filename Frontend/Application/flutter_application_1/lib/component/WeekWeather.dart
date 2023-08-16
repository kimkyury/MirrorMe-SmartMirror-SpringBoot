import 'package:flutter/material.dart';

class WeekWeather extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.amber,
      width: 350,
      height: 150,
      margin: EdgeInsets.only(
        left: 20,
        right: 20,
        top: 10,
        ),
      child: Container(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
              Container( // 하루 날씨
                width: 40,
                height: 130,
                color: Colors.pink, 
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container( // 날짜
                      child: Text('날짜'),
                    ),
                    Container( // 요일
                      child: Text('요일'),
                    ),
                    Container( // 하늘상태
                      width: 100,
                      height: 40,
                      color: Colors.black,
                    ),
                    Container( // 최고/최저 기온
                      child: Text('기온'),
                    ),
                    Container( // 강수확률
                      child: Text('강수'),
                    ),
                  ],
                ),
              ),
            ],
          ),
        )
    );
  }
}