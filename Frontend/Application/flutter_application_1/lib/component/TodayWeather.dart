import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:intl/intl.dart';

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
    var nowday = '';

    DateTime currentTime = DateTime.now();

    var koreanTime = currentTime.toUtc().add(Duration(hours: 9));

    String year = koreanTime.year.toString();
    String month = koreanTime.month.toString().padLeft(2, '0');
    var currentHour = koreanTime.hour;
    var currentMin = koreanTime.minute;
    var date;

    if (currentHour < 2 || (currentHour == 2 && currentMin < 45)) {
      // 02:45 이전인 경우 어제 날짜로 설정
      date = koreanTime.subtract(Duration(days: 1));
    } else {
      date = koreanTime;
    }

    var today = '${koreanTime.year}${koreanTime.month.toString().padLeft(2, '0')}${koreanTime.day.toString().padLeft(2, '0')}';
    var baseDate = '${koreanTime.year}${koreanTime.month.toString().padLeft(2, '0')}${koreanTime.day.toString().padLeft(2, '0')}';
    
    // print('currentHour = $currentHour');
    // print('baseDate = $baseDate');
    // print('today = $today');

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

        // print('Response Data: ${response.body}');

        // 데이터 처리
        final List<dynamic> todayWeather = todayWeatherList
            .where((data) => data['fcstDate'] == today)
            .toList();

        print('Filtered Weather Data: $todayWeather');

        final tempertureMinData = todayWeather
          .where((data) => data['category'] == 'TMN')
          .toList();
        final tempertureMin = tempertureMinData.first['tmn'];

        final tempertureMaxData = todayWeather
          .where((data) => data['category'] == 'TMX')
          .toList();
        final tempertureMax = tempertureMaxData.first['tmx'];

        final popData = todayWeather
          .where((data) => data['category'] == 'POP')
          .toList();
        final pop = popData.first['pop'];

        final ptyData = todayWeather
          .where((data) => data['category'] == 'PTY')
          .toList();
        final pty = ptyData.first['pty'];

        final skyData = todayWeather
          .where((data) => data['category'] == 'SKY')
          .toList();
          print('skyData = $skyData');
        final sky = skyData.first['sky'];

        // 날씨 정보를 저장
        setState(() {
          weatherInfo['tmn'] = tempertureMin;
          weatherInfo['tmx'] = tempertureMax;
          weatherInfo['pop'] = pop;
          weatherInfo['pty'] = pty;
          weatherInfo['sky'] = sky;
          isLoading = false; // 데이터 로딩 완료
        });
        // print('weatherInfo = $weatherInfo');
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
