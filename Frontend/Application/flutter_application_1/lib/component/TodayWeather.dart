import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:intl/intl.dart';

class TodayWeather extends StatefulWidget {
  @override
  _TodayWeatherState createState() => _TodayWeatherState();
}

class _TodayWeatherState extends State<TodayWeather> {
  Map<String, dynamic> weatherInfo = {};
  Map<String, dynamic> ultraInfo = {};
  bool isLoading = true;

  final skyicons = {
    1: '001.png', 2: '002.png', 3: '003.png', 4: '004.png',
    5: '005.png', 6: '006.png', 7: '007.png'
  };

  final skys = {
    1: '맑음', 2: '구름많음', 3: '흐림', 4: '비', 5: '눈/비', 6: '눈', 7: '소나기'
  };

  @override
  void initState() {
    super.initState();
    _fetchWeatherData();
  }

  @override
  void dispose() {
    super.dispose();
  }

  Future<void> _fetchWeatherData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/weather/short';

    var houseHoldId = 1;
    final pageNo = '1';
    final numOfRows = '500';
    var baseTime = '0200';

    DateTime currentTime = DateTime.now();
    var koreanTime = currentTime.toUtc().add(Duration(hours: 9));

    String year = koreanTime.year.toString();
    String month = koreanTime.month.toString().padLeft(2, '0');
    var currentHour = koreanTime.hour;
    var currentMin = koreanTime.minute;
    var date;

    if (currentHour < 2 || (currentHour == 2 && currentMin < 45)) {
      date = koreanTime.subtract(Duration(days: 1));
    } else {
      date = koreanTime;
    }

    var today = '${koreanTime.year}${koreanTime.month.toString().padLeft(2, '0')}${koreanTime.day.toString().padLeft(2, '0')}';
    var baseDate = '${koreanTime.year}${koreanTime.month.toString().padLeft(2, '0')}${koreanTime.day.toString().padLeft(2, '0')}';

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
        final todayWeatherList = List<Map<String, dynamic>>.from(responseData['response']);

        final List<dynamic> todayWeather = todayWeatherList
            .where((data) => data['fcstDate'] == today)
            .toList();

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
        final sky = skyData.first['sky'];

        if (mounted) {
          setState(() {
            weatherInfo['tmn'] = tempertureMin;
            weatherInfo['tmx'] = tempertureMax;
            weatherInfo['pop'] = pop;
            weatherInfo['pty'] = pty;
            weatherInfo['sky'] = sky;
          });
        }

        final ultraUrl = 'http://i9e101.p.ssafy.io:8080/weather/ultra';

        var ultrabasetime;
        if (currentMin > 45) {
          ultrabasetime = '${('${(currentHour).toString().padLeft(2, '0')}30')}';
        } else {
          ultrabasetime = '${('${(currentHour - 1).toString().padLeft(2, '0')}30')}';
        }

        var ultraHouseHoldId = '1';

        final Map<String, String> ultraParams = {
          'baseTime': ultrabasetime,
          'numOfRows': numOfRows,
          'pageNo': pageNo,
          'houseHoldId': ultraHouseHoldId,
        };

        final ultraResponse = await http.get(
          Uri.parse(ultraUrl).replace(queryParameters: ultraParams),
        );

        if (ultraResponse.statusCode == 200) {
          final ultraResponseData = json.decode(utf8.decode(ultraResponse.bodyBytes));
          final ultraWeatherData = ultraResponseData['response'];

          setState(() {
            ultraInfo = ultraWeatherData;
            isLoading = false;
          });

        } else {
          throw Exception('두 번째 API 호출 실패');
        }
      } else {
        throw Exception('첫 번째 API 호출 실패');
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
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            isLoading
                ? CircularProgressIndicator()
                : Column(
                    children: [
                      Container(
                        child: Row(
                          children: [
                            Image.asset(
                              'lib/assets/weather/path.png',
                              width: 20,
                            ),
                            Text(
                              '${ultraInfo['region']}',
                              style: TextStyle(
                                color: Color(0xffb2b2b2),
                                fontSize: 10,
                                fontFamily: 'NanumSquareRoundEB',
                              ),
                            ),
                          ],
                        ),
                      ),
                      SizedBox(height: 5,),
                      Container(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Container(
                              width: 80,
                              height: 80,
                              child: Image.asset('lib/assets/weather/${skyicons[weatherInfo['sky']]}'),
                            ),
                            Container(
                              child: Column(
                                children: [
                                  Text('${ultraInfo['t1H']}℃', style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: 'NanumSquareRoundEB',
                                  ),),
                                  SizedBox(height: 7,),
                                  Row(
                                    children: [
                                      Text('${weatherInfo['tmx'].toInt()}℃ / ',
                                        style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',)),
                                      Text('${weatherInfo['tmn'].toInt()}℃',
                                          style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',)
                                        ),
                                    ],
                                  )
                                ],
                              ),
                            ),
                            Container(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: [
                                  Text('${skys[weatherInfo['sky']]}', 
                                    style: TextStyle(
                                      fontFamily: 'NanumSquareRoundEB',
                                    )
                                  ),
                                  SizedBox(height: 5),
                                  Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Icon(Icons.water_drop, size: 16),
                                      SizedBox(width: 8),
                                      Text(
                                        '${ultraInfo['reh'].toInt()}%',
                                        style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',
                                        ),
                                      ),
                                    ],
                                  ),
                                  SizedBox(height: 5),
                                  Row(
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Icon(Icons.beach_access, size: 16),
                                      SizedBox(width: 8),
                                      Text(
                                        '${weatherInfo['pop'].toInt()}%',
                                        style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',
                                        ),
                                      ),
                                    ],
                                  ),
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

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: Center(
        child: TodayWeather(),
      ),
    ),
  ));
}
