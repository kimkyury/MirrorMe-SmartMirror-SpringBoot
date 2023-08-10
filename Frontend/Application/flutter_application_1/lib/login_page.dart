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
              child: Center(
                child: Image.asset('lib/assets/MirrorMe_Main.png'),
              ),
            ),
            SizedBox(
                height:
                    20),
            GestureDetector(
              onTap: () {
                _handleGoogleSignIn(context); // Google 로그인 핸들러 호출
              },
              child: Container(
                width: 330,
                height: 50,
                margin: EdgeInsets.only(
                  left: 30,
                  right: 30,
                ),
                decoration: BoxDecoration(
                  color: Colors.black,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Center(
                  child: Text(
                    'Login',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
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
              style: ElevatedButton.styleFrom(
                primary: Colors.black, // 배경색을 Container와 일치시킴
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
              ),
              child: Text('다른 페이지로 이동'),
            ),
          ],
        ),
      ),
    );
  }
}
