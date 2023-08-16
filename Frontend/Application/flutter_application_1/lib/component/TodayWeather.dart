import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TodayWeather extends StatefulWidget {
  @override
  _TodayWeatherState createState() => _TodayWeatherState();
}

class _TodayWeatherState extends State<TodayWeather> {
  Map<String, dynamic> weatherInfo = {}; // 날씨 정보 저장
  bool isLoading = true; // 로딩 완료 확인

  @override
  void initState() {
    super.initState();
    _fetchWeatherData();
  }

  Future<void> _fetchWeatherData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/weather/short';

    // API 호출에 필요한 파라미터 설정
    var houseHoldId = 1;
    final pageNo = '1';
    final numOfRows = '500';
    var baseTime = '0200';
    var day = '';

    DateTime currentTime = DateTime.now(); // 현재 시간 가져오기
    String year = currentTime.year.toString();
    String month = currentTime.month.toString().padLeft(2, '0');
    var currentHour = currentTime.hour;

    // 02:45 이전 날짜 처리
    if (currentHour > 3) {
      day = currentTime.day.toString().padLeft(2, '0');
    } else if (currentHour == 2 && currentTime.minute > 45) {
      day = currentTime.day.toString().padLeft(2, '0');
    } else {
      day = (currentTime.day - 1).toString().padLeft(2, '0');
    }

    var baseDate = '$year$month$day';
    String today = '$year$month${currentTime.day}';

    print('baseDate: $baseDate');
    try {
      final Map<String, String> params = {
        'baseDate': baseDate,
        'baseTime': baseTime,
        'numOfRows': numOfRows,
        'pageNo': pageNo,
        'houseHoldId': houseHoldId.toString(),
      };

      final response = await http.get(
        Uri.parse(url).replace(queryParameters: params),
      );

      if (response.statusCode == 200) {
        final responseData = json.decode(response.body);
        final todayWeatherList =
            List<Map<String, dynamic>>.from(responseData['response']);

        print('Response Data: ${response.body}');

        // 데이터 처리
        final List<dynamic> todayWeather = todayWeatherList
            .where((data) => data['fcstDate'] == today)
            .toList();

        final tempertureMin = todayWeather.firstWhere(
          (data) => data['category'] == 'TMN',
        )['fcstValue'];

        final tempertureMax = todayWeather.firstWhere(
          (data) => data['category'] == 'TMX',
        )['fcstValue'];

        final popInfo = todayWeather.firstWhere(
          (data) => data['category'] == 'POP',
        )['fcstValue'];

        final ptyInfo = todayWeather.firstWhere(
          (data) => data['category'] == 'PTY',
        )['fcstValue'];

        final skyInfo = todayWeather.firstWhere(
          (data) => data['category'] == 'SKY',
        )['fcstValue'];

        // 날씨 정보를 저장
        setState(() {
          weatherInfo['tmn'] = tempertureMin;
          weatherInfo['tmx'] = tempertureMax;
          weatherInfo['pop'] = popInfo;
          weatherInfo['pty'] = ptyInfo;
          weatherInfo['sky'] = skyInfo;
          isLoading = false; // 데이터 로딩 완료
        });
      } else {
        throw Exception('API 호출 실패');
      }
    } catch (error) {
      print('에러 발생: $error');
      setState(() {
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 350,
      height: 150,
      margin: EdgeInsets.only(
        left: 20,
        right: 20,
        bottom: 10,
      ),
      child: Container(
        // 오늘 날씨 정보 넣기
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            // 날씨 정보 로딩 중이면 로딩 아이콘 표시
            isLoading
                ? CircularProgressIndicator()
                : Column(
                    children: [
                      Container(
                        child: Row(
                          children: [
                            Image.asset(
                              'lib/assets/weather/path.png', // path icon
                              width: 20,
                            ),
                            SizedBox(width: 10),
                            Text(
                              '부산광역시, 대한민국',
                              style: TextStyle(
                                color: Color(0xffb2b2b2),
                                fontSize: 10,
                                fontFamily: 'NanumSquareRoundEB',
                              ),
                            ),
                          ],
                        ),
                      ),
                      Container(
                        color: Colors.green,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Container(
                              // 날씨 아이콘
                              width: 80,
                              height: 80,
                              color: Colors.red,
                              child: Text('날씨 아이콘'),
                            ),
                            Container(
                              // 기온 정보 표시
                              child: Text(
                                '기온',
                              ),
                            ),
                            Container(
                              // 최고, 최저 기온
                              child: Column(
                                children: [
                                  Container(
                                    // 나중에 SizedBox로 바꾸기
                                    color: Colors.brown,
                                    width: 30,
                                    height: 20,
                                  ),
                                  Text('최고/최저 기온'),
                                ],
                              ),
                            ),
                            Container(
                              // 우측 정보들
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: [
                                  Text('하늘 상태'),
                                  Text('습도'),
                                  Text('강수확률'),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
          ],
        ),
      ),
    );
  }
}
