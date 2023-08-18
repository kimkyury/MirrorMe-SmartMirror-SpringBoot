import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Settings extends StatefulWidget {
  final String accessToken;
  final String refreshToken;

  Settings({required this.accessToken, required this.refreshToken});

  @override
  _SettingsState createState() => _SettingsState();
}

class _SettingsState extends State<Settings> {
  String userName = '';
  String userEmail = '';

  // initState 메소드를 이용하여 페이지가 로드될 때 한 번 실행
  @override
  void initState() {
    super.initState();
    _fetchData(); // 페이지가 로드될 때 데이터를 가져오도록 설정
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/user/profile'; 
    
    // String accessToken = 'ya29.a0AfB_byDgekAtBNbBvXv2U_k2beWGeFig1riSIwnUMjGsMrNPeLvobC8SzflAAahddaOwSaAQCrCYTO61T873QelF9wnfmZsYfJam5w0zb892BFKcJiG0KdEvaWhS0pe2GHIFPWu44VlkCfIFZYtIl2jXrDxdVK3saCgYKAYoSARISFQHsvYlscmPmaHddHNDhwF2EReRftA0167';
    // String refreshToken = '1//0evNs0GmidlHhCgYIARAAGA4SNwF-L9Ir3sLRMdYucUhG6XF4P0UTM2Erq6hW3sbB7JO88F60_qPdxuf_7dtKNflysCcqWLCrtQo';

    var headers = {
      'Content-Type': 'application/json; charset=utf-8',
      'access_token': widget.accessToken, // access_token 추가
    };

    var cookies = {
      'refresh_token': widget.refreshToken, // refresh_token을 쿠키에 추가
    };

    try {
      final response = await http.get(
        Uri.parse(url),
        headers: headers,
        // cookie: cookies,
      );

      if (response.statusCode == 200) {
        final responseData = json.decode(utf8.decode(response.bodyBytes));
        final newProfile = responseData['response'];

        setState(() {
          userName = newProfile['userName'];
          userEmail = newProfile['userEmail'];
        });

        print('Response Data: ${response.body}');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
      setState(() {
      });
    }
  }

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
                    Text(userName,
                      style: TextStyle(
                        color: Color(0xff111111),
                        fontSize: 20,
                        fontFamily: 'NanumSquareRoundEB',
                        fontWeight: FontWeight.w400,
                        fontStyle: FontStyle.normal,
                      ),
                    ),
                    SizedBox(height: 10),
                    Text(userEmail,
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
                SizedBox(height: 10),
                Container(
                  // 첫 번째 세부 항목
                  padding: EdgeInsets.all(10),
                  width: 275,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(15),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey.withOpacity(0.5),
                        spreadRadius: 2,
                        blurRadius: 5,
                        offset: Offset(0, 3),
                      ),
                    ],
                  ),
                  child: Text(
                    'MirrorMe - 현관',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 16,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  
                ),
                SizedBox(height: 10), // 항목 사이 간격 조절
                Container(
                  // 두 번째 세부 항목
                  padding: EdgeInsets.all(10),
                  width: 275,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(15),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey.withOpacity(0.5),
                        spreadRadius: 2,
                        blurRadius: 5,
                        offset: Offset(0, 3),
                      ),
                    ],
                  ),
                  child: Text(
                    'MirrorMe - 거실',
                    style: TextStyle(
                      color: Color(0xff111111),
                      fontSize: 16,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                ),
                SizedBox(height: 10), // 항목 사이 간격 조절
              ],
            ),
          ),
          Divider(height: 10,),
          SizedBox(height: 20,),
          // Container(
          //   padding: EdgeInsets.all(10),
          //   width: 350,
          //   height: 161,
          //   margin: EdgeInsets.only(
          //     left: 20,
          //     right: 20,
          //   ),
          //   child: Column(
          //     children: [
          //       Container(
          //         margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
          //         child: Row(
          //           crossAxisAlignment: CrossAxisAlignment.center,
          //           children: [
          //             Text(
          //               'FAQ',
          //               style: TextStyle(
          //                 color: Color(0xff111111),
          //                 fontSize: 20,
          //                 fontFamily: 'NanumSquareRoundEB',
          //                 fontWeight: FontWeight.w400,
          //                 fontStyle: FontStyle.normal,
          //               ),
          //             ),
          //           ],
          //         ),
          //       ),
          //       // 첫 번째 질문과 답변
          //       Padding(
          //         padding: const EdgeInsets.only(left: 10), // 들여쓰기
          //         child: Column(
          //           crossAxisAlignment: CrossAxisAlignment.start,
          //           children: [
          //             Align(
          //               alignment: Alignment.centerLeft,
          //               child: Text(
          //                 'Q. 질문 1',
          //                 style: TextStyle(
          //                   color: Color(0xff111111),
          //                   fontSize: 14,
          //                   fontFamily: 'NanumSquareRoundEB',
          //                   fontWeight: FontWeight.w400,
          //                   fontStyle: FontStyle.normal,
          //                 ),
          //               ),
          //             ),
          //             SizedBox(height: 4),
          //             Align(
          //               alignment: Alignment.centerLeft,
          //               child: Text(
          //                 'A. 답변 1',
          //                 style: TextStyle(
          //                   color: Color(0xff111111),
          //                   fontSize: 12,
          //                   fontFamily: 'NanumSquareRoundEB',
          //                   fontWeight: FontWeight.w400,
          //                   fontStyle: FontStyle.normal,
          //                 ),
          //               ),
          //             ),
          //           ],
          //         ),
          //       ),

          //       SizedBox(height: 10),
          //       // 두 번째 질문과 답변
          //       Padding(
          //         padding: const EdgeInsets.only(left: 10), // 들여쓰기
          //         child: Column(
          //           crossAxisAlignment: CrossAxisAlignment.start,
          //           children: [
          //             Align(
          //               alignment: Alignment.centerLeft,
          //               child: Text(
          //                 'Q. 질문 2',
          //                 style: TextStyle(
          //                   color: Color(0xff111111),
          //                   fontSize: 14,
          //                   fontFamily: 'NanumSquareRoundEB',
          //                   fontWeight: FontWeight.w400,
          //                   fontStyle: FontStyle.normal,
          //                 ),
          //               ),
          //             ),
          //             SizedBox(height: 4),
          //             Align(
          //               alignment: Alignment.centerLeft,
          //               child: Text(
          //                 'A. 답변 2',
          //                 style: TextStyle(
          //                   color: Color(0xff111111),
          //                   fontSize: 12,
          //                   fontFamily: 'NanumSquareRoundEB',
          //                   fontWeight: FontWeight.w400,
          //                   fontStyle: FontStyle.normal,
          //                 ),
          //               ),
          //             ),
          //           ],
          //         ),
          //       ),
          //     ],
          //   ),
          // ),
        ],
      ),
    );
  }
}
