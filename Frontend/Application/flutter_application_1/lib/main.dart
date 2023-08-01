import 'package:flutter/material.dart';
import './component/News.dart';
import './component/Emotions.dart';
import './component/Home.dart';
import './component/Family.dart';
import './component/Settings.dart';

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
    News(),
    Emotions(),
    Home(),
    Family(),
    Settings(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'M',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: [
          Icon(Icons.message), // 메세지
          Icon(Icons.connect_without_contact), // 연결
        ],
      ),
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
