import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:google_sign_in/google_sign_in.dart';

import './main_page.dart';
import './profile.dart';
import './signin_page.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({Key? key}) : super(key: key);

  Future<void> _handleGoogleSignIn(BuildContext context) async {
    try {
      final GoogleSignIn _googleSignIn = GoogleSignIn(
        scopes: [
          'https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/tasks.readonly',
          'openid',
          'profile',
          'email',
        ],
        );
      final GoogleSignInAccount? googleSignInAccount = await _googleSignIn.signIn();
      
      if (googleSignInAccount != null) {
        final authCode = await googleSignInAccount.serverAuthCode;
        print('googleSignInAccount : $googleSignInAccount');
        print('authCode : $authCode');

        final email = await googleSignInAccount.email;

        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Signin(email: email)), // Pass email to Signup page
        );
      }
    } catch (error) {
      print('Error during Google Sign In: $error');
    }
  }

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
            SizedBox(
                height:
                    20), // Adding some space between the logo and the login button
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
                    _handleGoogleSignIn(context); // Google 로그인 핸들러 호출
                  },
                  child: Text('로그인'),
                ),
              ),
            ),
            SizedBox(height: 20), // Adding space between the two buttons
            ElevatedButton(
              // "다른 페이지로 이동" 버튼 추가
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => MyHomePage()), // 새로운 페이지로 이동
                );
              },
              child: Text('다른 페이지로 이동'),
            ),
          ],
        ),
      ),
    );
  }
}
