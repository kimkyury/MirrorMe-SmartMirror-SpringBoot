import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class FamilyEmotion extends StatelessWidget {
  const FamilyEmotion({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 350,
      // height: 220,
      margin: EdgeInsets.only(
        left: 20,
        right: 20,
      ),
      child: Column(
        children: [
          Container(
            padding: EdgeInsets.all(10),
            margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text('지난주 우리 가족 감정',
                  style: TextStyle(
                    color: Color(0xff111111),
                    fontSize: 20,
                    fontFamily: 'NanumSquareRoundEB',
                    fontWeight: FontWeight.w400,
                    fontStyle: FontStyle.normal,
                  ),
                ),
              ],
            ),
          ),
          Positioned(
            top: 0,
            child: Text(
              '감정 분포',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ),
          Container(
            height: 150,
            child: SfCircularChart(
              legend: Legend(isVisible: true),
              series: 
              <CircularSeries>[
                DoughnutSeries<_ChartData, String>(
                  dataSource: <_ChartData>[
                    _ChartData('기쁨', 30),
                    _ChartData('슬픔', 20),
                    _ChartData('분노', 25),
                    _ChartData('무표정', 25),
                  ],
                  xValueMapper: (_ChartData data, _) => data.emotion,
                  yValueMapper: (_ChartData data, _) => data.value,
                  dataLabelSettings: DataLabelSettings(isVisible: true),
                  name: '감정 분포',
                ),
                DoughnutSeries<_ChartData, String>(
                  dataSource: <_ChartData>[
                    _ChartData('기쁨', 30),
                    _ChartData('슬픔', 10),
                    _ChartData('분노', 50),
                    _ChartData('무표정', 10),
                  ],
                  xValueMapper: (_ChartData data, _) => data.emotion,
                  yValueMapper: (_ChartData data, _) => data.value,
                  dataLabelSettings: DataLabelSettings(isVisible: true),
                  name: '감정 분포',
                ),
              ],
              
            ),
          ),
        ],
      ),
    );
  }
}

class _ChartData {
  _ChartData(this.emotion, this.value);

  final String emotion;
  final int value;
}