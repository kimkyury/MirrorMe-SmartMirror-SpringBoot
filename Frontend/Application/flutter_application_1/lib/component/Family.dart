import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:math';

class Family extends StatefulWidget {
  final String accessToken;
  final String refreshToken;

  Family({required this.accessToken, required this.refreshToken});

  @override
  _FamilyMemberState createState() => _FamilyMemberState();
}

class _FamilyMemberState extends State<Family> {
  List<Map<String, dynamic>> members = [];
  PageController _pageController = PageController();
  int _currentPage = 0;

  List<int> temperatures = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchData(); // 페이지가 로드될 때 데이터를 가져오도록 설정
  }

  Future<void> _fetchData() async {
    final url = 'http://i9e101.p.ssafy.io:8080/user/friends'; 

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
        final newMembers = List<Map<String, dynamic>>.from(responseData['response']);

        final List<int> newTemperatures = newMembers.map<int>((member) {
          return Random().nextInt(100);
        }).toList();

        setState(() {
          members = newMembers;
          temperatures = newTemperatures;
          isLoading = false;
        });

        print('Response Data: ${response.body}');
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during HTTP request: $e');
      isLoading = false;
    }
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: ListView(
      children: [
        SizedBox(height: 20,),
        Container(
          padding: EdgeInsets.all(10),
          height: 200,
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
                    Text('우리 가족 목록',
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
                : members.isEmpty
                  ? Center(child: Text('등록된 가족이 없습니다', 
                      style: TextStyle(
                        color: Color(0xff111111),
                        fontSize: 14,
                        fontFamily: 'NanumSquareRoundEB',
                        fontWeight: FontWeight.w400,
                        fontStyle: FontStyle.normal,
                      ),
                    ))
                  : Column(
                  children: [
                    Expanded(
                      child: PageView.builder(
                        controller: _pageController,
                        itemCount: members.length,
                        onPageChanged: (index) {
                          setState(() {
                            _currentPage = index;
                          });
                        },
                        itemBuilder: (BuildContext context, int index) {
                          final member = members[index];
                          return GestureDetector(
                            onTap: () {
                              // Handle tap here
                              // You can navigate to a detail page or perform an action
                            },
                            child: AnimatedContainer(
                              duration: Duration(milliseconds: 300),
                              margin: EdgeInsets.all(10),
                              padding: EdgeInsets.all(10),
                              width: 350,
                              height: 161,
                              decoration: BoxDecoration(
                                color: Colors.white,
                                borderRadius: BorderRadius.circular(15),
                                boxShadow: [
                                  BoxShadow(
                                    color: Colors.grey.withOpacity(0.5),
                                    spreadRadius: 2,
                                    blurRadius: 5,
                                    offset: Offset(0, 3),
                                  ),
                                ],
                              ),
                              child: Row(
                                children: [
                                  Container(
                                    margin: EdgeInsets.fromLTRB(25, 0, 0, 0),
                                    width: 65,
                                    height: 65,
                                    decoration: BoxDecoration(
                                      image: DecorationImage(
                                        image: AssetImage('lib/assets/profile_default.png'),
                                        fit: BoxFit.contain,
                                      ),
                                      borderRadius: BorderRadius.circular(14),
                                    ),
                                  ),
                                  SizedBox(width: 30),
                                  Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Text(
                                        member['connectUserAlias'],
                                        style: TextStyle(
                                          color: Color(0xff111111),
                                          fontSize: 20,
                                          fontFamily: 'NanumSquareRoundEB',
                                          fontWeight: FontWeight.w400,
                                          fontStyle: FontStyle.normal,
                                        ),
                                      ),
                                      SizedBox(height: 10),
                                      Text(
                                        member['connectUserName'],
                                        style: TextStyle(
                                          color: Color(0xff111111),
                                          fontSize: 10,
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
                          );
                        },
                      ),
                    ),
                    SizedBox(height: 10),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: List<Widget>.generate(members.length, (int index) {
                        return Container(
                          width: 10,
                          height: 10,
                          margin: EdgeInsets.symmetric(horizontal: 5),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: _currentPage == index ? Colors.blue : Colors.grey,
                          ),
                        );
                      }),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        SizedBox(height: 20,),
        Divider(height: 10,),
        SizedBox(height: 20,),
        Container(
          padding: EdgeInsets.all(10),
          height: 300,
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
                    Text('우리 가족 마음 온도',
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
                    ? Center(child: CircularProgressIndicator())
                    : members.isEmpty
                      ? Center(child: Text('오늘의 일정이 없습니다', 
                          style: TextStyle(
                            color: Color(0xff111111),
                            fontSize: 14,
                            fontFamily: 'NanumSquareRoundEB',
                            fontWeight: FontWeight.w400,
                            fontStyle: FontStyle.normal,
                          ),
                        ))
                : ListView.builder(
                    itemCount: members.length,
                    itemBuilder: (BuildContext context, int index) {
                      final member = members[index];
                      final temperature = temperatures[index];


                      return Container(
                        padding: EdgeInsets.symmetric(vertical: 10, horizontal: 10),
                        child: Table(
                          columnWidths: {
                            0: FlexColumnWidth(1),
                            1: FlexColumnWidth(2),
                            2: FlexColumnWidth(1),
                          },
                          children: [
                            TableRow(
                              children: [
                                TableCell(
                                  child: Text(
                                    member['connectUserAlias'],
                                    style: TextStyle(
                                      color: Color(0xff111111),
                                      fontSize: 14,
                                      fontFamily: 'NanumSquareRoundEB',
                                      fontWeight: FontWeight.w400,
                                      fontStyle: FontStyle.normal,
                                    ),
                                  ),
                                ),
                                TableCell(
                                  child: Container(
                                    height: 15,
                                    width: 100,
                                    decoration: BoxDecoration(
                                      borderRadius: BorderRadius.circular(10),
                                      // border: Border.all(color: Color(0xff111111), width: 1),
                                      border: Border.all(color: Color(0xffb2b2b2), width: 1),
                                    ),
                                    child: Row(
                                      children: [
                                        Container(
                                          width: (temperature / 100) * 100,
                                          decoration: BoxDecoration(
                                            gradient: LinearGradient(
                                              colors: [
                                                Color.fromRGBO(83, 174, 191, 1.0),  // 시작색
                                                Color.fromRGBO(110, 132, 210, 1.0), // 중간색
                                                Color.fromRGBO(123, 113, 219, 1.0), // 마지막 색
                                              ],
                                              stops: [0.0, 0.5, 1.0], // 각 색상의 위치
                                            ),
                                            borderRadius: BorderRadius.circular(10),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                                TableCell(
                                  child: Text(
                                    '$temperature ℃',
                                    textAlign: TextAlign.right,
                                    style: TextStyle(
                                      color: Color(0xff111111),
                                      fontSize: 14,
                                      fontFamily: 'NanumSquareRoundEB',
                                      fontWeight: FontWeight.w400,
                                      fontStyle: FontStyle.normal,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      );
                    },
                  ),
              ),
            ],
          ),
        ),
      ],
     )
    );
  
  }
}