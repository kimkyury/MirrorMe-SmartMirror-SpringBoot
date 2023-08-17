import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class FamilyEmotion extends StatelessWidget {
  const FamilyEmotion({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 350,
      height: 220,
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
          Container(
            height: 150,
            child: SfCircularChart(
              legend: Legend(isVisible: true),
              series: <CircularSeries<_ChartData, String>>[
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