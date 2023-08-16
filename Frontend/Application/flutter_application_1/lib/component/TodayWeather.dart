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
          child: Text('일간 날씨'),
        ),
      );
  }
}