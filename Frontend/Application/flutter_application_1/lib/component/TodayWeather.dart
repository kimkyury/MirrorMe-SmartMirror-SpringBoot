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
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
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
                color: Colors.green,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Container( //날씨 아이콘
                      width: 80,
                      height: 80,
                      color: Colors.red,
                      child: Text('날씨 아이콘'),
                    ),
                    Container( // 기온
                      child: Text('기온'),
                    ),
                    Container( // 최고, 최저 기온
                      child: Text('최고/최저 기온'),
                    ),
                    Container( // 우측 정보들
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.end, // 우측 정렬
                        children: [
                          Text('하늘 상태'),
                          Text('습도'),
                          Text('강수확률'),
                        ],
                      ),
                    ), // 오른쪽 
                  ]
                ),
              )
            ],
          )
        ),
      );
  }
}