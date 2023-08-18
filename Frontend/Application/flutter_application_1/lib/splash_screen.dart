import 'package:flutter/material.dart';
import './login_page.dart';

class Splash extends StatefulWidget {
  const Splash({super.key});

  @override
  _SplashState createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  double opacity = 0.0;

  @override
  void initState() {
    super.initState();
    // 애니메이션 시작
    Future.delayed(Duration(seconds: 1), () {
      setState(() {
        opacity = 1.0;
      });
    });
    // 페이지 전환
    Future.delayed(Duration(seconds: 3), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => LoginPage()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: AnimatedOpacity(
          duration: Duration(seconds: 2), // 애니메이션 지속 시간 설정
          opacity: opacity,
          child: Image.asset('lib/assets/MirrorMe_Splash.png'),
        ),
      ),
    );
  }
}
