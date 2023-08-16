import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:google_sign_in/google_sign_in.dart';

import './main_page.dart';
import './profile.dart';
import './signin_page.dart';

import 'dart:convert';

class LoginPage extends StatelessWidget {
  LoginPage({Key? key}) : super(key: key);

  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  Future<void> _handleLogin(BuildContext context) async {

    // Get the values entered in the text fields
    final String email = emailController.text;
    final String password = passwordController.text;

    final Map<String, String> body = {
      'userEmail': email,
      'password': password,
    };

    final String url = 'http://i9e101.p.ssafy.io:8080/oauth/login/tokens'; // Replace with your login API URL

    try {
      final response = await http.post(
        Uri.parse(url),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(body),
      );

      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        if (responseData['response'] != null) {
          final accessToken = responseData['response']['accessToken'];
          final refreshToken = responseData['response']['refreshToken'];
          print('accessToken: $accessToken');
          print('refreshToken: $refreshToken');

          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => MyHomePage()),
          );
        } else {
          showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text('로그인 실패'),
                content: Text('비밀번호를 잘못 입력하셨습니다.'),
                actions: [
                  TextButton(
                    onPressed: () {
                      Navigator.of(context).pop(); // 메세지 창 닫기
                    },
                    child: Text('확인'),
                  ),
                ],
              );
            },
          );
        }
      } else {
        showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text('로그인 실패'),
                content: Text('이메일을 잘못 입력하셨습니다.'),
                actions: [
                  TextButton(
                    onPressed: () {
                      Navigator.of(context).pop(); // 메세지 창 닫기
                    },
                    child: Text('확인'),
                  ),
                ],
              );
            },
          );
        // Failed to log in
        print('Login failed. Status code: ${response.statusCode}');
      }
    } catch (e) {
      print('Error during login: $e');
    }
  }

  // Future<void> _handleGoogleSignIn(BuildContext context) async {
  //   try {
  //     final GoogleSignIn _googleSignIn = GoogleSignIn(
  //       scopes: [
  //         'https://www.googleapis.com/auth/calendar.readonly',
  //         'https://www.googleapis.com/auth/tasks.readonly',
  //         'openid',
  //         'profile',
  //         'email',
  //       ],
        
  //       );
  //     final GoogleSignInAccount? googleSignInAccount = await _googleSignIn.signIn();
      
  //     if (googleSignInAccount != null) {
  //       final authCode = await googleSignInAccount.serverAuthCode;
  //       print('googleSignInAccount : $googleSignInAccount');
  //       print('authCode : $authCode');

  //       final email = await googleSignInAccount.email;

  //       Navigator.push(
  //         context,
  //         MaterialPageRoute(builder: (context) => Signin(email: email)), // Pass email to Signup page
  //       );
  //     }
  //   } catch (error) {
  //     print('Error during Google Sign In: $error');
  //   }
  // }

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
            SizedBox(height: 20),
            // Email Text Field
            Container(
              width: 330,
              height: 50,
              margin: EdgeInsets.only(
                left: 30,
                right: 30,
              ),
              decoration: BoxDecoration(
                color: Colors.white,
                border: Border.all(
                  color: Color(0xffdddddd),
                  width: 1,
                ),
                borderRadius: BorderRadius.circular(10),
              ),
              child: TextFormField(
                controller: emailController,
                decoration: InputDecoration(
                  hintText: 'Google 이메일',
                  border: InputBorder.none,
                  contentPadding: EdgeInsets.symmetric(horizontal: 20),
                ),
              ),
            ),
            SizedBox(height: 20),
            // Password Text Field
            Container(
              width: 330,
              height: 50,
              margin: EdgeInsets.only(
                left: 30,
                right: 30,
              ),
              decoration: BoxDecoration(
                color: Colors.white,
                border: Border.all(
                  color: Color(0xffdddddd),
                  width: 1,
                ),
                borderRadius: BorderRadius.circular(10),
              ),
              child: TextFormField(
                controller: passwordController,
                obscureText: true, // Hide password
                decoration: InputDecoration(
                  hintText: '비밀번호',
                  border: InputBorder.none,
                  contentPadding: EdgeInsets.symmetric(horizontal: 20),
                ),
              ),
            ),
            SizedBox(height: 20),
            // Login Button
            GestureDetector(
              onTap: () {
                _handleLogin(context);
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
                child: Align(
                  alignment: Alignment.center,
                  child: Text(
                    'Login',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 14,
                      fontFamily: 'AppleSDGothicNeo',
                      fontWeight: FontWeight.w700,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                ),
              ),
            ),
            // "다른 페이지로 이동" Button
            // ElevatedButton(
            //   onPressed: () {
            //     Navigator.push(
            //       context,
            //       MaterialPageRoute(
            //         builder: (context) => MyHomePage(),
            //       ),
            //     );
            //   },
            //   style: ElevatedButton.styleFrom(
            //     primary: Colors.black,
            //     shape: RoundedRectangleBorder(
            //       borderRadius: BorderRadius.circular(10),
            //     ),
            //   ),
            //   child: Text('다른 페이지로 이동'),
            // ),
          ],
        ),
      ),
    );
  }
}
