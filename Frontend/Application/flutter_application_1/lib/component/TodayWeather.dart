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
                  // 좌표 아이콘
                  Text('부산광역시, 대한민국'),
                  ]
                )
              )
            ],
          )
        ),
      );
  }
}