import 'package:flutter/material.dart';

class TodayWeather extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.amber,
      width: 350,
      height: 150,
      margin: EdgeInsets.only(
        left: 20,
        right: 20,
        bottom: 10,
        ),
      child: Container(
          // 오늘 날씨 정보 넣자
          child: Column(
            children: [
              Container(
                child: Row(
                  children: [
                    Container(
                      // 좌표 사진으로 바꾸기
                      width: 15,
                      height: 15,
                      color: Colors.black,
                    ),
                    Text('부산광역시, 대한민국'),
                  ]
                )
              ),
              Container(
                child: Row(
                  
                ),
              )
            ],
          )
        ),
      );
  }
}