import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import './splash_screen.dart';

void main() async {
  runApp(const MyApp());
  // final Uri url = Uri.parse('http://192.168.30.142:8080/oauth/login/tokens');
  // final Map<String, String> headers = {
  //   'Content-Type': 'application/json; charset=UTF-8',
  // };

  // final Map<String, String> body = {
  //   'userEmail': 'mandarining0918@gmail.com',
  //   'password': '123456789',
  // };

  // try {
  //   final response = await http.post(
  //     url,
  //     headers: headers,
  //     body: jsonEncode(body), // Map을 JSON 문자열로 인코딩
  //   );

  //   if (response.statusCode == 200) {
  //     print('Request was successful');
  //   }
  // } catch (e) {
  //   print("Error: $e");
  // }

  const baseUrl = "http://i9e101.p.ssafy.io:8080";
  final queryParams = {
    'numOfRows': '100',
    'pageNo': '1',
  };

  final uri =
      Uri.parse('$baseUrl/weather/mid').replace(queryParameters: queryParams);

  try {
    var response = await http.get(uri);
    var statusCode = response.statusCode;
    var responseHeaders = response.headers;
    var responseBody = response.body;

    print("statusCode: $statusCode");
    print("responseHeaders: $responseHeaders");
    print("responseBody: $responseBody");
  } catch (e) {
    print("Error: $e");
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const Splash(),
    );
  }
}
