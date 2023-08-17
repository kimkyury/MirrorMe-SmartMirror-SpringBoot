import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Settings extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: ListView(
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
            child: Row(
              children: [
                Container(
                  width: 90,
                  height: 90, // 왼쪽 사진 컨테이너 너비 조정
                  decoration: BoxDecoration(
                    image: DecorationImage(
                      image: AssetImage('lib/assets/profile_default.png'), // 왼쪽 사진 이미지 경로 입력
                      fit: BoxFit.cover,
                    ),
                    borderRadius: BorderRadius.circular(14),
                  ),
                ),
                SizedBox(width: 30), // 사진과 프로필 사이 간격
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
          Divider(height: 10,),
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
                        '나의 거울',
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
          ),
          Divider(height: 10,),
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
                // 첫 번째 질문과 답변
                Padding(
                  padding: const EdgeInsets.only(left: 10), // 들여쓰기
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          'Q. 질문 1',
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 14,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ),
                      ),
                      SizedBox(height: 4),
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          'A. 답변 1',
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 12,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),

                SizedBox(height: 10),
                // 두 번째 질문과 답변
                Padding(
                  padding: const EdgeInsets.only(left: 10), // 들여쓰기
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          'Q. 질문 2',
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 14,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ),
                      ),
                      SizedBox(height: 4),
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          'A. 답변 2',
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 12,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                // 추가적인 질문과 답변을 이어서 나열하세요.
              ],
            ),
          ),
        ],
      ),
    );
  }
}
