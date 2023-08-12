import 'package:flutter/material.dart';
// import './main.dart';
import './login_page.dart';

class Splash extends StatelessWidget {
  const Splash({super.key});

  @override
  Widget build(BuildContext context) {
    Future.delayed(Duration(seconds: 2), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => LoginPage()),
      );
    });
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: Image.asset('lib/assets/MirrorMe_Splash.png'),
      )
    );
  }
}