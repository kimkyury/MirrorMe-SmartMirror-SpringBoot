import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import './splash_screen.dart';

void main() async {
  runApp(const MyApp());

  // const baseUrl = "http://i9e101.p.ssafy.io:8080";
  // final queryParams = {
  //   'numOfRows': '100',
  //   'pageNo': '1',
  // };

  // final uri = Uri.parse('$baseUrl/weather/mid').replace(queryParameters: queryParams);

  // try {
  //   var response = await http.get(uri);
  //   var statusCode = response.statusCode;
  //   var responseHeaders = response.headers;
  //   var responseBody = response.body;

  //   print("statusCode: $statusCode");
  //   print("responseHeaders: $responseHeaders");
  //   print("responseBody: $responseBody");
  // } catch (e) {
  //   print("Error: $e");
  // }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const Splash(),
    );
  }
}