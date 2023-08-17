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
  Map<String, dynamic> ultraInfo = {}; // 초단기 날씨 정보 저장
  // List<Map<String, dynamic>> ultraInfo = []; // 초단기 날씨 정보 저장
  
  bool isLoading = true; // 로딩 완료 확인

  final skyicons = {1: '001.png', 2: '002.png', 3: '003.png', 4: '004.png', 5: '005.png', 6: '006.png', 7: '007.png'};
  final skys = {1: '맑음', 2: '구름많음', 3: '흐림', 4: '비', 5: '눈/비', 6: '눈', 7: '소나기'};

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
        if (mounted) {
          setState(() {
            weatherInfo['tmn'] = tempertureMin;
            weatherInfo['tmx'] = tempertureMax;
            weatherInfo['pop'] = pop;
            weatherInfo['pty'] = pty;
            weatherInfo['sky'] = sky;
            isLoading = false; // 데이터 로딩 완료
          });
        }
        // print('weatherInfo = $weatherInfo');
        print('weatherInfo sky = ${weatherInfo['sky']}');
        print('skyicons[weatherInfo sky] gpt = ${skyicons['${weatherInfo['sky']}']}');
        print('skyicons[weatherInfo sky] = ${skyicons[weatherInfo['sky']]}');

      // ultra
      final ultraUrl = 'http://i9e101.p.ssafy.io:8080/weather/ultra';

      // baseTime
      var ultrabasetime;
      if (currentMin > 45) {
        ultrabasetime = '${('${(currentHour).toString().padLeft(2, '0')}30')}';
      } else {
        ultrabasetime = '${('${(currentHour - 1).toString().padLeft(2, '0')}30')}';
      }

      var houseHoldId = '1';
      final pageNo = '1';
      final numOfRows = '500';


      final Map<String, String> params = {
        'baseTime': ultrabasetime,
        'numOfRows': numOfRows,
        'pageNo': pageNo,
        'houseHoldId': houseHoldId.toString(),
      };

      final ultraResponse = await http.get(
        Uri.parse(ultraUrl).replace(queryParameters: params), // 필요한 파라미터 추가
      );

      if (ultraResponse.statusCode == 200) {
        // 두 번째 API 응답 처리
        // final ultraResponseData = json.decode(ultraResponse.body);
        final ultraResponseData = json.decode(utf8.decode(ultraResponse.bodyBytes)); // 한글깨짐 해결
        final ultraWeatherData = ultraResponseData['response'];
      
        // final ultraWeatherList = List<Map<String, dynamic>>.from(ultraResponseData['response']);
        
        print('Response Ultra Data: $ultraWeatherData');

        setState(() {
          ultraInfo = ultraWeatherData;
        });
        print('Ultra Info: $ultraInfo');
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

///////////////////////////////////////////////////////////////////////////////////

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
                            Text(
                              '${ultraInfo['region']}',
                              // '부산광역시, 대한민국',
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
                              // 날씨 아이콘
                              width: 80,
                              height: 80,
                              child: Image.asset('lib/assets/weather/${skyicons[weatherInfo['sky']]}'),
                            ),
                            Container(
                              // 기온 정보 표시
                              child: Column(
                                children: [
                                  Text('${ultraInfo['t1H']}℃', style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: 'NanumSquareRoundEB',
                                  ),),
                                  SizedBox(height: 7,),
                                  Row(
                                    children: [
                                      Text('${weatherInfo['tmx']}℃ / ',
                                        style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',)),
                                      Text('${weatherInfo['tmn']}℃',
                                          style: TextStyle(
                                          fontFamily: 'NanumSquareRoundEB',)
                                        ),
                                    ],
                                  )
                                ],
                              ),
                              // child: Text(
                              //   '${ultraInfo['t1H'].toInt()}℃', style: TextStyle(
                              //     fontSize: 25
                              //   ),
                              // ),
                            ),
                            // Container(
                            //   child: Column(
                            //     children: [
                            //       // Container(
                            //       //   // 나중에 SizedBox로 바꾸기
                            //       //   color: Colors.brown,
                            //       //   width: 30,
                            //       //   height: 20,
                            //       // ),
                            //       Text('${weatherInfo['tmx'].toInt()}℃'),
                            //       Text('${weatherInfo['tmn'].toInt()}℃'),
                            //     ],
                            //   ),
                            // ),
                            Container(
                              // 우측 정보들
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.end,
                                children: [
                                  Text('${skys[weatherInfo['sky']]}', 
                                    style: TextStyle(
                                      fontFamily: 'NanumSquareRoundEB',
                                    )
                                  ),
                                  Text('습도 :  ${weatherInfo['pop']}%',
                                    style: TextStyle(
                                      fontFamily: 'NanumSquareRoundEB',
                                    )
                                  ),
                                  Text('강수확률 : ${weatherInfo['pop']}%',
                                    style: TextStyle(
                                      fontFamily: 'NanumSquareRoundEB',
                                    )
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
