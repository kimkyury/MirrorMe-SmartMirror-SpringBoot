import 'package:flutter/material.dart';

// import './main_page.dart';
import './profile.dart';

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
                    Navigator.push( // 구글 로그인 버튼이 눌렸을 때 Profile 페이지로 이동합니다.
                      context,
                      MaterialPageRoute(builder: (context) => Profile()),
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