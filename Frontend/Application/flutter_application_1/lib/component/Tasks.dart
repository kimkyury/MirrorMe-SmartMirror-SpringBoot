import 'package:flutter/material.dart';

class Tasks extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
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
                Text(
                  'Todo',
                  style: TextStyle(
                    color: Color(0xff111111),
                    fontSize: 20,
                    fontFamily: 'NanumSquareRoundEB',
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
                    Text('일정1'),
                  ]),
                ),
                Text('마감일?'),
              ],
            ),
          ),
          Container(
            // 일정 한 개
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  child: Row(
                    children: [
                    Icon(
                      Icons.circle,
                      color: Colors.red,
                      size: 15,
                    ),
                    Text('일정2'),
                  ]),
                ),
                Text('마감일?'),
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
                    Text('일정3'),
                  ]),
                ),
                Text('마감일?'),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
