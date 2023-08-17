import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';

class Schedules extends StatefulWidget {
  const Schedules({super.key});

  @override
  _SchedulesState createState() => _SchedulesState();
}

class _SchedulesState extends State<Schedules> {
  List<Map<String, dynamic>> schedules = []; // 일정을 저장할 리스트

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
      'access_token': 'ya29.a0AfB_byAKygNK-Hr13FFGjoWTdqB0nTp8ViD9DaA6tULhfxhAhgFq5hNCA51PKyM4xKZXEaFGSLdYo2_qacBgqjHVZFqz5UjBrlhFEh-mpwADz4vE6k9TeR96qp-O5b3F-6LTZ7IUo1y_a9xmRHYii4b-a1eiwMa7aWbZVj-s3QaCgYKAWUSARISFQHsvYlsRiROD0hl5N93-NwuJlwDDg0177', // access_token 추가
    };

    var cookies = {
      'refresh_token': '1//0evNs0GmidlHhCgYIARAAGA4SNwF-L9Ir3sLRMdYucUhG6XF4P0UTM2Erq6hW3sbB7JO88F60_qPdxuf_7dtKNflysCcqWLCrtQo', // refresh_token을 쿠키에 추가
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
              Expanded( // 리스트뷰가 남은 공간을 모두 차지할 수 있도록 Expanded 위젯을 추가합니다.
                child: ListView.builder(
                  itemCount: schedules.length,
                  itemBuilder: (BuildContext context, int index) {
                    final schedule = schedules[index];
                    return Container(
                      // 일정 한 개
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Container(
                            child: Row(children: [
                              Icon(
                                Icons.circle,
                                color: Colors.red,
                                size: 10,
                              ),
                              Text(schedule['summary'], 
                              style: TextStyle(
                                color: Color(0xff111111),
                                fontSize: 12,
                                fontFamily: 'NanumSquareRoundEB',
                                fontWeight: FontWeight.w400,
                                fontStyle: FontStyle.normal,
                              ),
                              ) // 일정 제목 표시
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