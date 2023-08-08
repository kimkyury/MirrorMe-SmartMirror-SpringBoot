import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Home extends StatelessWidget {
  Future<void> fetchData() async {
    final url = Uri.parse('http://i9e101.p.ssafy.io:8080/weather/mid');

    final Map<String, int> queryParams = {
      'numOfRows': 100,
      'pageNo': 1,
    };
    final uri = Uri.https(url.authority, url.path, queryParams);

    final response = await http.get(uri, headers: {
      'Content-Type': 'application/json', // 필요한 경우 헤더를 추가
    });

    if (response.statusCode == 200) {
      // 데이터를 성공적으로 받았을 때의 처리
      print('Response data: ${response.body}');
    } else {
      // 요청이 실패했을 때의 처리
      print('Request failed with status: ${response.statusCode}');
    }
  }

  @override
  Widget build(BuildContext context) {
    // 홈 컴포넌트의 내용을 작성
    return ListView(
      children: [
        Container(
          // 날씨
          height: 150,
          color: Colors.amber,
          child: Text('날씨'),
        ),
        Container(
          // 오늘 일정
          padding: EdgeInsets.all(10),
          height: 150,
          color: const Color.fromARGB(255, 239, 110, 153),
          child: Column(
            children: [
              Container(
                // 제목
                margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Icon(
                      Icons.schedule,
                      color: Colors.black,
                    ),
                    Text(
                      '오늘의 일정',
                      style: TextStyle(
                          // 오늘 날짜도 추가할 지 논의 필요
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500),
                    )
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
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
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
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
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
                        Text('일정1')
                      ]),
                    ),
                    Text('시간')
                  ],
                ),
              )
            ],
          ),
        ),
        Container(
          // 할 일
          padding: EdgeInsets.all(10),
          height: 150,
          color: Color.fromARGB(255, 110, 198, 239),
          child: Column(
            children: [
              Container(
                // 제목
                margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Icon(
                      Icons.schedule,
                      color: Colors.black,
                    ),
                    Text(
                      '할 일',
                      style: TextStyle(
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500),
                    )
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
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
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
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
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
                        Text('일정1')
                      ]),
                    ),
                    Text('마감일?')
                  ],
                ),
              )
            ],
          ),
        ),
      ],
    );
  }
}
