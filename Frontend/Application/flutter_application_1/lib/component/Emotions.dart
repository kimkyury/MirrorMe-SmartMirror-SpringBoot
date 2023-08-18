import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import './MyEmotions.dart';
import './FamilyEmotion.dart';

class Emotions extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: ListView(
        children: [
          MyEmotions(),
          SizedBox(height: 20,),
          Divider(height: 10,),
          SizedBox(height: 20,),
          FamilyEmotion(),
        ],
      )
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: Text('Emotions')),
      body: Emotions(),
    ),
  ));
}
