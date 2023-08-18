import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

void main() {
  runApp(MaterialApp(
    home: Scaffold(
      appBar: AppBar(title: Text('Emotion Frequency')),
      body: MyEmotions(),
    ),
  ));
}

class MyEmotions extends StatelessWidget {
  const MyEmotions({Key? key});  

  @override
  Widget build(BuildContext context) {
    final List<_ChartData> chartData = [
      _ChartData('MON', 12, 10, 14, 20),
      _ChartData('TUE', 14, 11, 18, 23),
      _ChartData('WED', 16, 10, 15, 20),
      _ChartData('THU', 12, 22, 16, 24),
      _ChartData('FRI', 18, 16, 18, 20),
      _ChartData('SAT', 16, 12, 20, 24),
      _ChartData('SUN', 17, 16, 11, 21),
    ];

    return Container(
      width: 350,
      height: 280,
      margin: EdgeInsets.only(
        left: 20,
        right: 20,
      ),
      child: Column(
        children: [
          Container(
            padding: EdgeInsets.all(10),
            margin: EdgeInsets.fromLTRB(0, 20, 0, 0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text( '지난 주 나의 감정',
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
          Expanded(
            child: SfCartesianChart(
              primaryXAxis: CategoryAxis(),
              legend: Legend(
                isVisible: true,
                position: LegendPosition.bottom,
                ), // 범례 활성화
              series: <ChartSeries>[
                StackedColumnSeries<_ChartData, String>(
                  dataSource: chartData,
                  xValueMapper: (_ChartData data, _) => data.day,
                  yValueMapper: (_ChartData data, _) => data.emotion1,
                  name: '기쁨',
                ),
                StackedColumnSeries<_ChartData, String>(
                  dataSource: chartData,
                  xValueMapper: (_ChartData data, _) => data.day,
                  yValueMapper: (_ChartData data, _) => data.emotion2,
                  name: '슬픔',
                ),
                StackedColumnSeries<_ChartData, String>(
                  dataSource: chartData,
                  xValueMapper: (_ChartData data, _) => data.day,
                  yValueMapper: (_ChartData data, _) => data.emotion3,
                  name: '분노',
                ),
                StackedColumnSeries<_ChartData, String>(
                  dataSource: chartData,
                  xValueMapper: (_ChartData data, _) => data.day,
                  yValueMapper: (_ChartData data, _) => data.emotion4,
                  name: '무표정',
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
  _ChartData(this.day, this.emotion1, this.emotion2, this.emotion3, this.emotion4);
  final String day;
  final num emotion1;
  final num emotion2;
  final num emotion3;
  final num emotion4;  
}
