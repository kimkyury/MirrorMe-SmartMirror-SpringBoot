import 'package:flutter/material.dart';
import './Tasks.dart';
import './Schedules.dart';

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
          height: 161,
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
        ),
        SizedBox(height: 20,),
        Schedules(),
        SizedBox(height: 20,),
        Tasks(),
      ],
    );
  }
}
