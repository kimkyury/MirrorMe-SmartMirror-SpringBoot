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
          Row(
            children: [
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '주원언니', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 6),
                        _ChartData('슬픔', 4),
                        _ChartData('분노', 5),
                        _ChartData('무표정', 5),
                      ],
                      xValueMapper: (_ChartData data, _) => data.emotion,
                      yValueMapper: (_ChartData data, _) => data.value,
                      dataLabelSettings: DataLabelSettings(isVisible: true),
                    ),
                  ],
                ),
              ),
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '너구리', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 12),
                        _ChartData('슬픔', 2),
                        _ChartData('분노', 1),
                        _ChartData('무표정', 7),
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
          Divider(height: 10,),
          Row(
            children: [
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '이진형', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 4),
                        _ChartData('슬픔', 5),
                        _ChartData('분노', 6),
                        _ChartData('무표정', 7),
                      ],
                      xValueMapper: (_ChartData data, _) => data.emotion,
                      yValueMapper: (_ChartData data, _) => data.value,
                      dataLabelSettings: DataLabelSettings(isVisible: true),
                    ),
                  ],
                ),
              ),
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '삼촌', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 5),
                        _ChartData('슬픔', 10),
                        _ChartData('분노', 12),
                        _ChartData('무표정', 17),
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
          Divider(height: 10,),
          Row(
            children: [
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '김성현', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 7),
                        _ChartData('슬픔', 6),
                        _ChartData('분노', 5),
                        _ChartData('무표정', 4),
                      ],
                      xValueMapper: (_ChartData data, _) => data.emotion,
                      yValueMapper: (_ChartData data, _) => data.value,
                      dataLabelSettings: DataLabelSettings(isVisible: true),
                    ),
                  ],
                ),
              ),
              Container(
                height: 200,
                width: 160,
                child: SfCircularChart(
                  title: ChartTitle(
                    text: '이소정', // 그래프 제목
                    alignment: ChartAlignment.center,
                    textStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 10,
                      fontFamily: 'NanumSquareRoundEB',
                      fontWeight: FontWeight.w400,
                      fontStyle: FontStyle.normal,
                    ),
                  ),
                  // legend: Legend(isVisible: true, position: LegendPosition.top,),
                  series: 
                  <CircularSeries>[
                    DoughnutSeries<_ChartData, String>(
                      dataSource: <_ChartData>[
                        _ChartData('기쁨', 6),
                        _ChartData('슬픔', 4),
                        _ChartData('분노', 5),
                        _ChartData('무표정', 10),
                      ],
                      xValueMapper: (_ChartData data, _) => data.emotion,
                      yValueMapper: (_ChartData data, _) => data.value,
                      dataLabelSettings: DataLabelSettings(isVisible: true),
                    ),
                  ],
                ),
              ),
            ],
          )      
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