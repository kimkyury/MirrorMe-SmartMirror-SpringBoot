import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';
import 'package:intl/intl.dart'; // DateFormat 추가

class Schedules extends StatefulWidget {
  final String accessToken;
  final String refreshToken;

  Schedules({required this.accessToken, required this.refreshToken});

  @override
  _SchedulesState createState() => _SchedulesState();
}

class _SchedulesState extends State<Schedules> {
  List<Map<String, dynamic>> schedules = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchData();
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/schedule/today';

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
        final newSchedules = List<Map<String, dynamic>>.from(responseData['response']);

        setState(() {
          schedules = newSchedules;
          isLoading = false;
        });

        print('Response Data: ${response.body}');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
      setState(() {
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(10),
      height: 230,
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
                  'Today',
                  style: TextStyle(
                    color: Color(0xff111111),
                    fontSize: 20,
                    fontFamily: 'NanumSquareRoundEB',
                    fontWeight: FontWeight.w400,
                    fontStyle: FontStyle.normal,
                  ),
                ),
                SizedBox(width: 7),
                Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    SizedBox(height: 5),
                    Text(
                      '${DateFormat('MMMM, dd yyyy').format(DateTime.now())}',
                      style: TextStyle(
                        color: Color(0xff111111),
                        fontSize: 13,
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
          Expanded(
            child: isLoading
                ? Center(child: CircularProgressIndicator())
                : schedules.isEmpty
                    ? Center(
                        child: Text(
                          '오늘의 일정이 없습니다',
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 14,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ),
                      )
                    : ListView.builder(
                        itemCount: schedules.length,
                        itemBuilder: (BuildContext context, int index) {
                          final schedule = schedules[index];
                          return Container(
                            margin: EdgeInsets.symmetric(vertical: 5), // 여기에 마진 추가
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Container(
                                  child: Row(
                                    children: [
                                      Container(
                                        width: 15, // 변경: 이미지 요소 크기 수정
                                        height: 15, // 변경: 이미지 요소 크기 수정
                                        child: Image.asset('lib/assets/icons/blue.png'),
                                      ),
                                      SizedBox(width: 5),
                                      Text(
                                        schedule['summary'],
                                        style: TextStyle(
                                          color: Color(0xff111111),
                                          fontSize: 12, // 변경: 글자 크기 수정
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
                          );
                        },
                      ),
          ),
        ],
      ),
    );
  }
}