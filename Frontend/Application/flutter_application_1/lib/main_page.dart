import 'package:flutter/material.dart';
import './component/News.dart';
import './component/Emotions.dart';
import './component/Home.dart';
import './component/Family.dart';
import './component/Settings.dart';
import './component/Message.dart';
import './component/Connect.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _currentIndex = 2; // 기본 페이지 홈으로 설정
  final PageController _pageController = PageController(initialPage: 2);

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
          Row(
            children: [
              IconButton(
                icon: Icon(Icons.message),
                onPressed: () {
                  Navigator.push(
                    context,
                    PageRouteBuilder(
                      transitionDuration: Duration(milliseconds: 300),
                      pageBuilder: (_, __, ___) => Message(),
                      transitionsBuilder: (_, Animation<double> animation, __, Widget child) {
                        var curveAnimation = CurvedAnimation(parent: animation, curve: Curves.easeInOut);
                        return SlideTransition(
                          position: Tween<Offset>(begin: Offset(0, -1), end: Offset.zero).animate(curveAnimation),
                          child: child,
                        );
                      },
                    ),
                  );
                },
              ),// Add a SizedBox to create spacing between the icons
              IconButton(
                icon: Icon(Icons.connect_without_contact),
                onPressed: () {
                  Navigator.push(
                    context,
                    PageRouteBuilder(
                      transitionDuration: Duration(milliseconds: 300),
                      pageBuilder: (_, __, ___) => Connect(),
                      transitionsBuilder: (_, Animation<double> animation, __, Widget child) {
                        var curveAnimation = CurvedAnimation(parent: animation, curve: Curves.easeInOut);
                        return SlideTransition(
                          position: Tween<Offset>(begin: Offset(0, -1), end: Offset.zero).animate(curveAnimation),
                          child: child,
                        );
                      },
                    ),
                  );
                },
              ),// Add a SizedBox to create spacing between the icons
            ],
          ),// 연결
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