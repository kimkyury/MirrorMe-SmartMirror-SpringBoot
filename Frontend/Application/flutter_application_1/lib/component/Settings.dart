import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Settings extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SizedBox(height: 20,),
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
                      fontFamily: 'NanumSquareRoundOTFEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text('Email',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundOTFR',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  SizedBox(height: 5),
                  Text('지역',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundOTFR',
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

      ],

    );
  }
}
