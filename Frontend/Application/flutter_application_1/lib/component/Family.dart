import 'package:flutter/material.dart';

class Family extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // 가족 컴포넌트의 내용을 작성
    return ListView(
      children: [
        Container(
          color: Colors.amber,
          height: 300, // 가족 수에 맞출 지 추후 논의 필요
          child: Column( // 우리 가족 마음온도
            children: [
              Container( // 제목 줄
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      child: Row(
                        children: [
                          Icon(Icons.heart_broken),
                          Text('우리 가족 마음 온도', style: TextStyle(
                            color: Colors.black,
                            fontWeight: FontWeight.w500,
                            fontSize: 23
                          ),),
                        ],
                      ),
                    ),
                    Text('업데이트 시간')
                  ]
                ),
              ),
              Container( // 온도계 하나
                
              ),
            ],
          ),
        ),
      ],
    );
  }
}