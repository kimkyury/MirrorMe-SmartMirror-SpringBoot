import 'package:flutter/material.dart';
import 'package:flutter_application_1/household.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TodayWeather extends StatefulWidget {
  @override
  _TodayWeatherState createState() => _TodayWeatherState();
}

class _TodayWeatherState extends State<TodayWeather> {
  Map<String, dynamic> weatherInfo = {};
  Map<String, dynamic> ultraInfo = {};
  bool isLoading = true;
  bool imageLoading = true;

  @override
  void initState() {
    super.initState();
    fetchWeatherData();
  }

  Future<void> fetchWeatherData() async {
    try {
      // 변수 설정
      final houseHold = '1'; /////////////하드코딩에서 수정하기/////////////
      final currentTime = DateTime.now();
      final year = currentTime.year.toString();
      final month = currentTime.month.toString().padLeft(2, '0');
      final currentHour = currentTime.hour;
      var day = '';

      // 02:45 이전 날짜 처리
      if (currentHour > 3) {
        day = currentTime.day.toString().padLeft(2, '0');
      } else if (currentHour == 2 && currentTime.minute > 45) {
        day = currentTime.day.toString().padLeft(2, '0');
      } else {
        day = (currentTime.day - 1).toString().padLeft(2, '0');
      }

      final baseDate = '$year$month$day';
      final baseTime = '0200'; // 최저 기온 수신 가능 시간
      final today = '$year$month${currentTime.day.toString().padLeft(2, '0')}';

      // 최고, 최저 기온, 하늘 상태 API 호출
      const String baseUrl = 'http://i9e101.p.ssafy.io:8080/weather/short'; // API 경로
      final Map<String, String> params = {
        'baseDate': baseDate,
        'baseTime': baseTime,
        'numOfRows': '500',
        'pageNo': '1',
        'houseHoldId': houseHold,
      };
      final Uri uri = Uri.parse(baseUrl).replace(queryParameters: params);

      final response = await http.get(uri);

      if (response.statusCode == 200) {
        final List<dynamic> responseData = json.decode(response.body)['response'];

        // 오늘 날짜의 정보 가져오기
        final currentTime = DateTime.now();
        final String today = '${currentTime.year}${currentTime.month.toString().padLeft(2, '0')}${currentTime.day.toString().padLeft(2, '0')}';

        final todayWeather = responseData.firstWhere((data) => data['fcstDate'] == today);
        
        print(todayWeather);

        // 필요한 정보 추출 및 상태에 저장
        setState(() {
          weatherInfo['tmn'] = todayWeather['tmn'];
          weatherInfo['tmx'] = todayWeather['tmx'];
          weatherInfo['pop'] = todayWeather['pop'];
          weatherInfo['pty'] = todayWeather['pty'];
          weatherInfo['sky'] = todayWeather['sky'];
        });

        // 이미지 로딩 함수 호출
        await loadWeatherImages();
      } else {
        throw Exception('Failed to load weather data');
      }
    } catch (error) {
      print('Error fetching weather data: $error');
      setState(() {
        isLoading = false;
      });
    }
  }

  Future<void> loadWeatherImages() async {
    List<String> skyImages = [
      'lib/assets/weather/001.png',
      'lib/assets/weather/002.png',
      'lib/assets/weather/003.png',
      'lib/assets/weather/004.png',
      'lib/assets/weather/005.png',
      'lib/assets/weather/006.png',
      'lib/assets/weather/007.png'
    ];

    try {
      await Future.wait(skyImages.map((src) async {
        final image = AssetImage(src);
        await precacheImage(image, context);
      }));

      setState(() {
        imageLoading = false;
      });
    } catch (error) {
      print('Error loading images: $error');
      setState(() {
        imageLoading = false;
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
            Container(
              child: Row(
                children: [
                  Image.asset(
                    'lib/assets/weather/path.png', // path icon
                    width: 10,
                  ),
                  SizedBox(width: 8),
                  Text(
                    '부산광역시, 대한민국',
                    style: TextStyle(
                      color: Color(0xffb2b2b2),
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundOTFR',
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
                    child: Image.asset(
                      'lib/assets/weather/${weatherInfo['sky']}.png', // 날씨 아이콘 이미지 경로
                      width: 40,
                      height: 40,
                    ),
                  ),
                  Container(
                    // 기온
                    child: Text(
                      '${ultraInfo['t1H']}℃', // 실시간 기온 정보 사용
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
                        Text(
                          '${weatherInfo['tmx']}℃ / ${weatherInfo['tmn']}℃', // 최고, 최저 기온 정보 사용
                        ),
                      ],
                    ),
                  ),
                  Container(
                    // 우측 정보들
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      // 우측 정렬
                      children: [
                        Text('하늘 상태'),
                        Text('습도'),
                        Text('강수확률'),
                      ],
                    ),
                  ), // 오른쪽
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: TodayWeather(),
  ));
}