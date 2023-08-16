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
        title: Image.asset('lib/assets/MirrorMe_Main.png'),
        backgroundColor: Colors.white,
        automaticallyImplyLeading: false,  // 뒤로가기 화살표 제거
        actions: [
          Row(
            children: [
              IconButton(
                icon: Image.asset('lib/assets/messageicon.png'),
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
                icon: Image.asset('lib/assets/connecticon.png'),
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
          padding: EdgeInsets.all(15),
          height: 80,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              buildNavItem(
                _currentIndex == 0
                    ? Image.asset('lib/assets/newsiconcolor.png') // 선택된 화면에 맞는 이미지
                    : Image.asset('lib/assets/newsicon.png'),
                0,
              ),
              buildNavItem(
                _currentIndex == 1
                    ? Image.asset('lib/assets/emotioniconcolor.png') // 선택된 화면에 맞는 이미지
                    : Image.asset('lib/assets/emotionicon.png'),
                1,
              ),
              buildNavItem(
                _currentIndex == 2
                    ? Image.asset('lib/assets/homeiconcolor.png') // 선택된 화면에 맞는 이미지
                    : Image.asset('lib/assets/homeicon.png'),
                2,
              ),
              buildNavItem(
                _currentIndex == 3
                    ? Image.asset('lib/assets/familyiconcolor.png') // 선택된 화면에 맞는 이미지
                    : Image.asset('lib/assets/familyicon.png'),
                3,
              ),
              buildNavItem(
                _currentIndex == 4
                    ? Image.asset('lib/assets/settingiconcolor.png') // 선택된 화면에 맞는 이미지
                    : Image.asset('lib/assets/settingicon.png'),
                4,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget buildNavItem(Image image,  int index) {
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
          image,
        ],
      ),
    );
  }
}