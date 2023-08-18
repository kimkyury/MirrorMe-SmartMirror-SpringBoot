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
  List<String> tasks = [];
  List<bool> isCheckedList = [];

  @override
  void initState() {
    super.initState();
    _fetchData();
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
      padding: EdgeInsets.all(10),
      height: 500,
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
                  'ToDo',
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
          Expanded(
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
                        margin: EdgeInsets.fromLTRB(0, 5, 0, 5),
                        child: Row(children: [
                          GestureDetector(
                            onTap: () {
                              setState(() {
                                isCheckedList[index] = !isCheckedList[index];
                              });
                            },
                            child: Image.asset(
                              isChecked
                                  ? 'lib/assets/icons/done.png'
                                  : 'lib/assets/icons/notyet.png',
                              width: 15,
                              height: 15,
                            ),
                          ),
                          SizedBox(width: 5,),
                          Text(
                            task,
                            style: TextStyle(
                              color:
                                  isChecked ? Colors.grey : Color(0xff111111),
                              fontSize: 12,
                              fontFamily: 'NanumSquareRoundEB',
                              fontWeight: isChecked
                                  ? FontWeight.w700
                                  : FontWeight.w400,
                              fontStyle: FontStyle.normal,
                              decoration: isChecked
                                  ? TextDecoration.lineThrough
                                  : TextDecoration.none,
                            ),
                            softWrap: true,
                          )
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
