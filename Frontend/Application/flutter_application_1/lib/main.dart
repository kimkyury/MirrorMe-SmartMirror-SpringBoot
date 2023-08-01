import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}


class _MyHomePageState extends State<MyHomePage> {
  int _currentIndex = 2; // 기본 페이지 홈으로 설정
  final PageController _pageController = PageController();

  final List<Widget> _pages = [
    // Replace these with your actual pages or widgets
    News(),
    Emotions(),
    Home(),
    Family(),
    Settings(),
  ];

  // 전체 화면 구성
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'M',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w600,
          ),),
          actions: [
          Icon(Icons.message), // 메세지
          Icon(Icons.connect_without_contact) // 연결
        ],),
      body: PageView(
        controller: _pageController,
        children: _pages,
        onPageChanged: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
      ),
      bottomNavigationBar: BottomAppBar(
        child: Container(
          padding: EdgeInsets.all(20),
          height: 80,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              buildNavItem(Icons.newspaper, '뉴스', 0),
              buildNavItem(Icons.emoji_emotions, '감정', 1),
              buildNavItem(Icons.home, '홈', 2),
              buildNavItem(Icons.people, '가족', 3),
              buildNavItem(Icons.settings, '설정', 4),
            ],
          ),
        ),
      ),
    );
  }

  Widget buildNavItem(IconData icon, String label, int index) {
    return GestureDetector(
      onTap: () {
        _pageController.animateToPage(
          index,
          duration: Duration(milliseconds: 500),
          curve: Curves.ease,
        );
      },
      child: Column(
        children: [
          Icon(
            icon,
            color: _currentIndex == index ? Colors.blue : Colors.black,
          ),
          Text(
            label,
            style: TextStyle(
              fontSize: 10,
              color: _currentIndex == index ? Colors.blue : Colors.black,
            ),
          ),
        ],
      ),
    );
  }
}

// BottomNavigationBar별 페이지
// 뉴스
class News extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        Container( // 키워드 별 컨테이너 한 개
          padding: EdgeInsets.all(10),
          height: 130,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row( // 키워드 제목
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    child: Row(
                      children: [
                        Icon(Icons.sports_football, color: Colors.black,),
                        Text('스포츠', style: TextStyle(
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500
                        ),),
                      ],
                    ),
                  ),
                  Text('업데이트 시간') // 추후 업데이트 시간으로 변경
                ],
              ),
              Container( // 기사 목록
                child: Column(
                children: [
                  Row( // 뉴스 기사 1
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 2
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 3
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                ],
                ),
              ),
            ],
          ),
        ),
        
        Container( // 키워드 별 컨테이너 한 개
          padding: EdgeInsets.all(10),
          height: 130,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row( // 키워드 제목
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    child: Row(
                      children: [
                        Icon(Icons.computer, color: Colors.black,),
                        Text('IT/과학', style: TextStyle(
                          color: Colors.black,
                          fontSize: 23,
                          fontWeight: FontWeight.w500
                        ),),
                      ],
                    ),
                  ),
                  Text('업데이트 시간') // 추후 업데이트 시간으로 변경
                ],
              ),
              Container( // 기사 목록
                child: Column(
                children: [
                  Row( // 뉴스 기사 1
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 2
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                  Row( // 뉴스 기사 3
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('기사 제목 줄여서 출력하기 위한 예시로 글을 적음...'),
                      Text('언론사 이름')
                    ],
                  ),
                ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

// 감정
class Emotions extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Page 2'),
    );
  }
}

// 홈 화면
class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Page 3'),
    );
  }
}

// 가족
class Family extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Page 4'),
    );
  }
}

// 설정
class Settings extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Page 5'),
    );
  }
}
