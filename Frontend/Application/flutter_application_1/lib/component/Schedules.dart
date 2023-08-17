import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';

class Schedules extends StatefulWidget {
  final String accessToken;
  final String refreshToken;

  Schedules({required this.accessToken, required this.refreshToken});

  @override
  _SchedulesState createState() => _SchedulesState();
}

class _SchedulesState extends State<Schedules> {
  List<Map<String, dynamic>> schedules = []; // 일정을 저장할 리스트
  bool isLoading = true;

  // initState 메소드를 이용하여 페이지가 로드될 때 한 번 실행
  @override
  void initState() {
    super.initState();
    _fetchData(); // 페이지가 로드될 때 데이터를 가져오도록 설정
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/schedule/today'; 
    
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
        final newSchedules = List<Map<String, dynamic>>.from(responseData['response']);

        setState(() {
          schedules = newSchedules; // 메시지 리스트 업데이트
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
                    Text('Today',
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
                child: isLoading
                    ? Center(child: CircularProgressIndicator()) // 로딩 중일 때 CircularProgressIndicator 표시
                    : schedules.isEmpty
                        ? Center(child: Text('오늘의 일정이 없습니다', 
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 14,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        )) // 일정이 없을 때 메시지 표시
                        : ListView.builder(
                            itemCount: schedules.length,
                            itemBuilder: (BuildContext context, int index) {
                              final schedule = schedules[index];
                              return Container(
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Container(
                                      child: Row(
                                        children: [
                                          Icon(
                                            Icons.circle,
                                            color: Colors.red,
                                            size: 5,
                                          ),
                                          SizedBox(width: 5),
                                          Text(
                                            schedule['summary'],
                                            style: TextStyle(
                                              color: Color(0xff111111),
                                              fontSize: 12,
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