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
          child: Text('주간 날씨'),
        )
    );
  }
}