// import 'package:flutter/material.dart';

// class Family extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     // 가족 컴포넌트의 내용을 작성
//     return Container(
//       color: Colors.white,
//       child: ListView(
//       children: [
//         SizedBox(height: 20,),
//         // 우리 가족 목록
//         Container(
//           padding: EdgeInsets.all(10),
//           width: 350,
//           height: 161,
//           margin: EdgeInsets.only(
//             left: 20,
//             right: 20,
//           ),
//           child: Column(
//             children: [
//               Container(
//                 margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
//                 child: Row(
//                   crossAxisAlignment: CrossAxisAlignment.center,
//                   children: [
//                     Text(
//                       '우리 가족 목록',
//                       style: TextStyle(
//                         color: Color(0xff111111),
//                         fontSize: 20,
//                         fontFamily: 'NanumSquareRoundEB',
//                         fontWeight: FontWeight.w400,
//                         fontStyle: FontStyle.normal,
//                       ),
//                     ),
//                   ],
//                 ),
//               ),
//               SizedBox(height: 10),
//               Padding(
//                 padding: const EdgeInsets.only(left: 10), // 들여쓰기
//                 child: Column(
//                   crossAxisAlignment: CrossAxisAlignment.start,
//                   children: [
//                     Align(
//                       alignment: Alignment.centerLeft,
//                       child: Text(
//                         '가족 1',
//                         style: TextStyle(
//                           color: Color(0xff111111),
//                           fontSize: 16,
//                           fontFamily: 'NanumSquareRoundEB',
//                           fontWeight: FontWeight.w400,
//                           fontStyle: FontStyle.normal,
//                         ),
//                       ),
//                     ),
//                     SizedBox(height: 10),
//                     Align(
//                       alignment: Alignment.centerLeft,
//                       child: Text(
//                         '가족 2',
//                         style: TextStyle(
//                           color: Color(0xff111111),
//                           fontSize: 16,
//                           fontFamily: 'NanumSquareRoundEB',
//                           fontWeight: FontWeight.w400,
//                           fontStyle: FontStyle.normal,
//                         ),
//                       ),
//                     ),
//                     SizedBox(height: 10),
//                     Align(
//                       alignment: Alignment.centerLeft,
//                       child: Text(
//                         '가족 3',
//                         style: TextStyle(
//                           color: Color(0xff111111),
//                           fontSize: 16,
//                           fontFamily: 'NanumSquareRoundEB',
//                           fontWeight: FontWeight.w400,
//                           fontStyle: FontStyle.normal,
//                         ),
//                       ),
//                     ),
//                   ],
//                 ),
//               ),
//               // 추가적인 질문과 답변을 이어서 나열하세요.
//             ],
//           ),
//         ),
//         Divider(height: 10,),
//         SizedBox(height: 20,),
//         // 우리 가족 마음 온도
//         Container(
//           padding: EdgeInsets.all(10),
//           width: 350,
//           height: 161,
//           margin: EdgeInsets.only(
//             left: 20,
//             right: 20,
//           ),
//           child: Column(
//             children: [
//               Container(
//                 // 제목
//                 margin: EdgeInsets.fromLTRB(0, 0, 0, 10),
//                 child: Row(
//                   crossAxisAlignment: CrossAxisAlignment.center,
//                   children: [
//                     Text('우리 가족 마음 온도',
//                       style: TextStyle(
//                         color: Color(0xff111111),
//                         fontSize: 20,
//                         fontFamily: 'NanumSquareRoundEB',
//                         fontWeight: FontWeight.w400,
//                         fontStyle: FontStyle.normal,
//                       ),
//                     ),
//                   ],
//                 ),
//               ),
//             ],
//           ),
//         ),
//       ],
//     )
//     );
//   }
// }