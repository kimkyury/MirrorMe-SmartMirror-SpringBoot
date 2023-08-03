import 'package:flutter/material.dart';

import './main_page.dart';

class Login extends StatelessWidget {
  const Login({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              height: 200,
              width: 200,
              color: Colors.blue,
              child: Center(
                child: Text('로고'),
              ),
            ),
            SizedBox(height: 20), // Adding some space between the logo and the login button
            Container(
              height: 50,
              width: 200,
              decoration: BoxDecoration(
                color: Colors.grey,
                borderRadius: BorderRadius.circular(25),
              ),
              child: Center(
                child: ElevatedButton(
                  onPressed: () {
                    Navigator.pushReplacement( // 현재 라우트(Login)를 MyHomePage로 대체하여 이동합니다.
                      context,
                      MaterialPageRoute(builder: (context) => MyHomePage()),
                    );
                  },
                  child: Text('구글 계정으로 로그인'),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}