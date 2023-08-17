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
class _TasksState extends State<Tasks> with AutomaticKeepAliveClientMixin<Tasks> {
  List<String> tasks = []; // 일정을 저장할 리스트
  List<bool> isCheckedList = [];  // 체크 상태를 저장하는 리스트

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
      'access_token': widget.accessToken,
    };

    try {
      final response = await http.get(
        Uri.parse(url),
        headers: headers,
      );

      if (response.statusCode == 200) {
        final responseData = json.decode(utf8.decode(response.bodyBytes));
        final taskItems = responseData['response'][0]['items'];

        final newTasks = List<String>.from(
          taskItems.map((task) {
            return task['title'];
          }),
        );

        setState(() {
          tasks = newTasks;
          isCheckedList = List<bool>.filled(tasks.length, false);
        });

        print('Response Data: ${response.body}');
        print('tasks: ${tasks}');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
    }
  }

  @override
  bool get wantKeepAlive => true;


  @override
  Widget build(BuildContext context) {
    return Container(
          // 오늘 일정
          padding: EdgeInsets.all(10),
          height: 500,
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
              Expanded( // 리스트뷰가 남은 공간을 모두 차지할 수 있도록 Expanded 위젯을 추가합니다.
                child: ListView.builder(
                  itemCount: tasks.length,
                  itemBuilder: (BuildContext context, int index) {
                    final task = tasks[index];
                    bool isChecked = isCheckedList[index];

                    return Container(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Container(
                            child: Row(children: [
                              Checkbox(
                                value: isChecked,
                                onChanged: (bool? value) {
                                  setState(() {
                                    isCheckedList[index] = value ?? false;  // 해당 항목의 체크 상태 변경
                                  });
                                },
                                materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                              ),
                              Text(
                                task,
                                style: TextStyle(
                                  color: isChecked ? Colors.grey : Color(0xff111111),
                                  fontSize: 12,
                                  fontFamily: 'NanumSquareRoundEB',
                                  fontWeight: isChecked ? FontWeight.w700 : FontWeight.w400,  // 밑줄 적용 여부에 따라 폰트 무게 변경
                                  fontStyle: FontStyle.normal,
                                  decoration: isChecked ? TextDecoration.lineThrough : TextDecoration.none,  // 밑줄 추가 여부
                                ),
                                softWrap: true,
                              )// 일정 제목 표시
                            ]),
                          ),
                        ],
                      ),
                    );
                  },
                ),
              ),
            ],
          ),
        );
  }
}