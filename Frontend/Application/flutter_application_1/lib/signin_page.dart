import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import './profile.dart';

class Signin extends StatefulWidget {
  final String email;

  const Signin({required this.email, Key? key}) : super(key: key);

  @override
  _SigninState createState() => _SigninState();
}

class _SigninState extends State<Signin> {
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();

  bool _isPasswordValid = true;
  final GoogleSignIn _googleSignIn = GoogleSignIn();

  void _validatePassword() {
    setState(() {
      final password = _passwordController.text;
      final confirmPassword = _confirmPasswordController.text;

      // 최소 7자 이상이고, 영어 소문자와 숫자를 모두 포함하는지 확인
      _isPasswordValid = password.length >= 7 &&
          RegExp(r'^(?=.*[a-z])(?=.*\d).+$').hasMatch(password) &&
          password == confirmPassword;
    });
  }

  // Future<void> sendPostRequest() async {
  //   final Uri url = Uri.parse('http://192.168.30.142:8080/oauth/login/tokens');
  //   final Map<String, String> headers = {
  //     'Content-Type': 'application/json; charset=UTF-8',
  //   };

  //   final Map<String, String> body = {
  //     'userEmail': 'mandarining0918@gmail.com',
  //     'password': '123456789',
  //   };

  //   try {
  //     final response = await http.post(
  //       url,
  //       headers: headers,
  //       body: jsonEncode(body), // Map을 JSON 문자열로 인코딩
  //     );

  //     if (response.statusCode == 200) {
  //       print('Request was successful');
  //     }
  //   } catch (e) {
  //     print("Error: $e");
  //   }
  // }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        await _googleSignIn.signOut(); // 뒤로가기 버튼을 누르면 구글 로그아웃
        return true;
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text('로그인'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                controller: TextEditingController(
                    text: widget.email), // 구글 계정의 이메일을 회원가입 이메일로 자동 반영
                enabled: false, // 입력 비활성화 설정
                decoration: InputDecoration(
                  labelText: '이메일',
                ),
              ),
              SizedBox(height: 20),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: InputDecoration(
                  labelText: '비밀번호',
                  errorText: _passwordController.text.length < 7 &&
                          _passwordController.text.length > 0
                      ? '비밀번호는 영어와 숫자를 합쳐 7자 이상이어야 합니다.'
                      : null,
                ),
              ),
              TextField(
                controller: _confirmPasswordController,
                obscureText: true,
                onChanged: (_) => _validatePassword(),
                decoration: InputDecoration(
                  labelText: '비밀번호 확인',
                  errorText: _isPasswordValid ? null : '비밀번호가 일치하지 않습니다.',
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _isPasswordValid
                    ? null
                    // sendPostRequest
                    : null,
                child: Text('로그인'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }
}
