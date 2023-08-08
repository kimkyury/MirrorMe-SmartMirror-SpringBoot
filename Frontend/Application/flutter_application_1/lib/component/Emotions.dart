import 'package:flutter/material.dart';

class Emotions extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Emotions'),
      ),
      body: Column(
        children: [
          Container(
            padding: EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.blue,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  '지난주 나의 감정 Report',
                  style: TextStyle(fontSize: 18, color: Colors.white),
                ),
                SizedBox(height: 8),
                Text(
                  '여기에 실제 감정 데이터를 추가하세요.',
                  style: TextStyle(fontSize: 16, color: Colors.white),
                ),
              ],
            ),
          ),
          SizedBox(height: 20),
          Container(
            width: double.infinity,
            padding: EdgeInsets.all(16),
            decoration: BoxDecoration(
              border: Border.all(color: Colors.grey.shade300),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  '그래프 형태의 그림',
                  style: TextStyle(fontSize: 18),
                ),
                SizedBox(height: 8),
                Container(
                  height: 200, // 그래프의 높이를 조절해주세요.
                  // 실제 그래프를 추가하세요.
                  child: Placeholder(),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
