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
      body: Center(
        child: Text('Intro Page'),
      )
    );
  }
}