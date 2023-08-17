import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';

class Tasks extends StatefulWidget {
  final String accessToken;
  final String refreshToken;

  Tasks({required this.accessToken, required this.refreshToken});

  @override
  _TasksState createState() => _TasksState();
}
class _TasksState extends State<Tasks> {
  List<Map<String, dynamic>> tasks = []; // 일정을 저장할 리스트

  // initState 메소드를 이용하여 페이지가 로드될 때 한 번 실행
  @override
  void initState() {
    super.initState();
    _fetchData(); // 페이지가 로드될 때 데이터를 가져오도록 설정
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/tasks'; 

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
        final newTasks = List<Map<String, dynamic>>.from(responseData['response']);


        setState(() {
          tasks = newTasks; // 메시지 리스트 업데이트
        });

        print('Response Data: ${response.body}');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
    }
  }


  @override
  Widget build(BuildContext context) {
    return Container(
          // 오늘 일정
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
                    Text('ToDo',
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
              // Expanded( // 리스트뷰가 남은 공간을 모두 차지할 수 있도록 Expanded 위젯을 추가합니다.
              //   child: ListView.builder(
              //     itemCount: tasks.length,
              //     itemBuilder: (BuildContext context, int index) {
              //       final task = tasks[index];
              //       return Container(
              //         // 일정 한 개
              //         child: Row(
              //           mainAxisAlignment: MainAxisAlignment.spaceBetween,
              //           children: [
              //             Container(
              //               child: Row(children: [
              //                 Icon(
              //                   Icons.circle,
              //                   color: Colors.red,
              //                   size: 10,
              //                 ),
              //                 Text(task['title'], 
              //                 style: TextStyle(
              //                   color: Color(0xff111111),
              //                   fontSize: 12,
              //                   fontFamily: 'NanumSquareRoundEB',
              //                   fontWeight: FontWeight.w400,
              //                   fontStyle: FontStyle.normal,
              //                 ),
              //                 ) // 일정 제목 표시
              //               ]),
              //             ),
              //           ],
              //         ),
              //       );
              //     },
              //   ),
              // ),
            ],
          ),
        );
  }
}