import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';

import '../css/Weather.css';
const houseHoldId = 1;

function WeekWeather(props) {
  const [weekInfo, setWeekInfo] = useState([]);
  const [firstDayInfo, setFirstDayInfo] = useState([]);
  const [secondDayInfo, setSecondDayInfo] = useState([]);
  const [midtemperInfo, setMidTemperInfo] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [midrainInfo, setMidRainInfo] = useState([]);

  useEffect(() => {
    // 다음 일주일 정보 채우기
    const currentTime = new Date();
    const currentHour = currentTime.getHours();
    const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];

    const nowday = currentTime.getDay(); // 06시 이전 : 오늘부터 7개 요일
    const tomorrow = (nowday + 1) % 7; // 06시 이후 : 내일부터 7개 요일

    setWeekInfo(prevWeekInfo => { // 요일 정보 업데이트
      return days.map((day, index) => {
        const dayIndex = (currentHour < 6 ? nowday : tomorrow) + index;
        return `${days[dayIndex % 7]}`;
      });
    });

    // 최고, 최저 기온 구하기
    const year = currentTime.getFullYear();
    const month = String(currentTime.getMonth() + 1).padStart(2, '0');
    let day = '';
    const today = `${year}${month}${currentTime.getDate()}`;
    
    // 02:45 이전 날짜 처리
    if (currentHour > 3) {
      day = String(currentTime.getDate()).padStart(2, '0');
    } else if (currentHour === 2 && currentTime.getMinutes() > 45) {
      day = String(currentTime.getDate()).padStart(2, '0');
    } else {
      day = String(currentTime.getDate()-1).padStart(2, '0');
    }
    
    let baseDate = `${year}${month}${day}`;
    const baseTime = "0500";
    let numOfRows = 1000;
    let pageNo = 1;
    
    // 요청 보내는 시간을 기준으로 수정
    // 06시가 지났는지를 기준으로, 첫 번째와 두 번째 날짜 결정
    let firstDay = currentHour < 6 ? `${year}${month}${day}` : `${year}${month}${String(Number(day) + 1).padStart(2, '0')}`
    let secondDay = currentHour < 6 ? `${year}${month}${String(Number(day) + 1).padStart(2, '0')}` : `${year}${month}${String(Number(day) + 2).padStart(2, '0')}`;
    if ( baseDate != today ) {
      firstDay = currentHour < 6 ? `${year}${month}${String(Number(day) + 1).padStart(2, '0')}` : `${year}${month}${String(Number(day) + 2).padStart(2, '0')}`;
      secondDay = currentHour < 6 ? `${year}${month}${String(Number(day) + 2).padStart(2, '0')}` : `${year}${month}${String(Number(day) + 3).padStart(2, '0')}`;
    }
    
    // firstDay 기상 정보
    axios.get("weather/short", {
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo, houseHoldId: houseHoldId },
    }).then((res) => {
      const todayWeather = res.data.response.filter((data) => data.fcstDate === firstDay);

      const tempertureMin = todayWeather.find((data) => data.category === 'TMN');
      const tempertureMax = todayWeather.find((data) => data.category === 'TMX');
      const popInfo = todayWeather.find((data) => data.category === 'POP');
      const ptyInfo = todayWeather.find((data) => data.category === 'PTY');
      const skyInfo = todayWeather.find((data) => data.category === 'SKY');

      setFirstDayInfo({
        tmn: tempertureMin.tmn,
        tmx: tempertureMax.tmx,
        pop: popInfo.pop,
        pty: ptyInfo.pty,
        sky: skyInfo.sky,
      }, () => {
        console.log('firstDayInfo', firstDayInfo);
      });
    }).catch((error) => {
      console.log(error);
    });

    // secondDay 기상 정보
    axios.get("weather/short", {
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo, houseHoldId: houseHoldId },
    }).then((res) => {
      // console.log(res.data.response)
      // console.log(secondDay)
      const todayWeather = res.data.response.filter((data) => data.fcstDate === secondDay);
      
      const tempertureMin = todayWeather.find((data) => data.category === 'TMN');
      const tempertureMax = todayWeather.find((data) => data.category === 'TMX');
      const popInfo = todayWeather.find((data) => data.category === 'POP');
      const ptyInfo = todayWeather.find((data) => data.category === 'PTY');
      const skyInfo = todayWeather.find((data) => data.category === 'SKY');
      
      setSecondDayInfo({
        tmn: tempertureMin.tmn,
        tmx: tempertureMax.tmx,
        pop: popInfo.pop,
        pty: ptyInfo.pty,
        sky: skyInfo.sky,
      }, () => {
        console.log('secondDayInfo', secondDayInfo);
      });
      setIsLoading(false);
    }).catch((error) => {
      console.log(error);
    });
    
    // 중기 날씨 정보 저장
    axios.get("weather/mid", {
      params: { baseDate:baseDate, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      setMidTemperInfo(res.data.response);
    }).catch((error) => {
      console.log(error);
    });

    // 18시 기준으로 baseDate 설정
    day = String(currentTime.getDate()).padStart(2, '0');
    baseDate = currentHour < 18 ? `${year}${month}${String(Number(day) - 1).padStart(2, '0')}` : `${year}${month}${day}`

    axios.get("weather/mid/rain", {
      params: { baseDate:baseDate, numOfRows: numOfRows, pageNo: pageNo }
    }).then((res) => {
      console.log(res.data.response)
      setMidRainInfo(res.data.response)
    }).catch((error) => {
      console.log(error)
    })
  }, []);

  const skyImages = {
    1: `${process.env.PUBLIC_URL}/images/weather/001.png`,
    2: `${process.env.PUBLIC_URL}/images/weather/002.png`,
    3: `${process.env.PUBLIC_URL}/images/weather/003.png`,
    4: `${process.env.PUBLIC_URL}/images/weather/004.png`,
    5: `${process.env.PUBLIC_URL}/images/weather/005.png`,
    6: `${process.env.PUBLIC_URL}/images/weather/006.png`,
    7: `${process.env.PUBLIC_URL}/images/weather/007.png`,
    '맑음': `${process.env.PUBLIC_URL}/images/weather/001.png`,
    '구름많음': `${process.env.PUBLIC_URL}/images/weather/002.png`,
    '흐림': `${process.env.PUBLIC_URL}/images/weather/003.png`,
    '흐리고 비': `${process.env.PUBLIC_URL}/images/weather/004.png`,
    '눈 비': `${process.env.PUBLIC_URL}/images/weather/005.png`,
    '눈': `${process.env.PUBLIC_URL}/images/weather/006.png`,
    '소나기': `${process.env.PUBLIC_URL}/images/weather/007.png`,
  };
  
  return (
    <div>
      {/* 주간 날씨 테이블 */}
      <TableContainer className='weather-table'>
        <Table>
          {/* 제목행 필요할 경우 주석 활용 */}
          <TableHead>
            {/* <TableRow>
              <TableCell>아이콘</TableCell>
              <TableCell>요일</TableCell>
              <TableCell>최고기온</TableCell>
              <TableCell>최저기온</TableCell>
              <TableCell>강수확률</TableCell>
            </TableRow> */}
          </TableHead>
          <TableBody>
            {/* 아이콘 추가를 위한 작업 필요 */}
            {isLoading ? (
              <TableRow>
                <TableCell align="center">
                  <CircularProgress />
                </TableCell>
              </TableRow>
            ) : (
              weekInfo.map((day, index) => (
                <TableRow key={index}>
                  <TableCell>
                    <img
                      src={skyImages[index === 0 ? firstDayInfo.sky : (index === 1 && secondDayInfo.sky) ? secondDayInfo.sky : midrainInfo[`wf${index + 1}Am`]]}
                      alt="weather-icon"
                      style={{ maxWidth: '100px', height: 'auto' }}
                    />
                  </TableCell>
                  <TableCell>{day}</TableCell>
                  <TableCell>
                      {index === 0 ? firstDayInfo.tmx : index === 1 && secondDayInfo.tmx ? secondDayInfo.tmx : midtemperInfo[`taMax${index + 1}`]}℃
                  </TableCell>
                  <TableCell>
                      {index === 0 ? firstDayInfo.tmn : index === 1 && secondDayInfo.tmn ? secondDayInfo.tmn : midtemperInfo[`taMin${index + 1}`]}℃
                  </TableCell>
                  <TableCell>
                      {index === 0 ? firstDayInfo.pop : index === 1 && secondDayInfo.pop ? secondDayInfo.pop : midrainInfo[`rnSt${index + 1}Am`]}%
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default WeekWeather;
