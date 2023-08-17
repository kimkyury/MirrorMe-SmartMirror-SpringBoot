import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class Emotions extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SizedBox(height: 20,),
        // 우리 가족 목록
        Container(
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
                    Text('지난주 나의 감정',
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
          // decoration: BoxDecoration(
          //   color: Colors.white,
          //   borderRadius: BorderRadius.circular(14),
          //   boxShadow: [
          //     BoxShadow(
          //       color: Color(0x29000000),
          //       offset: Offset(0, 1),
          //       blurRadius: 6,
          //       spreadRadius: 0,
          //     ),
          //   ],
          // ),
        ),
        Divider(height: 10,),
        SizedBox(height: 20,),
        // 우리 가족 마음 온도
        Container(
          padding: EdgeInsets.all(10),
          width: 350,
          height: 161,
          margin: EdgeInsets.only(
            left: 20,
            right: 20,
          ),
          child: Column(
            children: [
              Container(
                // 제목
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
            ],
          ),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(14),
            boxShadow: [
              BoxShadow(
                color: Color(0x29000000),
                offset: Offset(0, 1),
                blurRadius: 6,
                spreadRadius: 0,
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class _ChartData {
  _ChartData(this.emotion, this.value);

  final String emotion;
  final int value;
}
