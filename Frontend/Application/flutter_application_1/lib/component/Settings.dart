import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Settings extends StatelessWidget {




  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SizedBox(height: 20,),
        Container(
          padding: EdgeInsets.all(10),
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
          child: Row(
            children: [
              Container(
                width: 90,
	              height: 90, // 왼쪽 사진 컨테이너 너비 조정
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage('lib/assets/messageicon.png'), // 왼쪽 사진 이미지 경로 입력
                    fit: BoxFit.cover,
                  ),
                  borderRadius: BorderRadius.circular(14),
                ),
              ),
              SizedBox(width: 10), // 사진과 프로필 사이 간격
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text('이름',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 20,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text('Email',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  SizedBox(height: 5),
                  Text('지역',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
        SizedBox(height: 20,),
        // Container(
        //   width: 389.5,
        //   height: 0,
        //   margin: EdgeInsets.only(
        //     left: 0.5,
        //     right: 0.5,
        //   ),
        //   decoration: BoxDecoration(
        //     border: Border.all(
        //       color: Color(0xffeeeeee),
        //       width: 2,
        //     ),
        //   ),
        // ),
        // SizedBox(height: 20,),
        Container(
          padding: EdgeInsets.all(10),
          width: 350,
          height: 161,
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
                      '거울 등록',
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
            ],
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
        Container(
          padding: EdgeInsets.all(10),
          width: 350,
          height: 161,
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
                      'FAQ',
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
                      child: Row(children: [
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
      ],
    );
  }
}
