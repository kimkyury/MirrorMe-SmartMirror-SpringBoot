import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';

import '../css/Weather.css';

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
    
    const baseDate = `${year}${month}${day}`;
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
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
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
      });
    }).catch((error) => {
      console.log(error);
    });

    // secondDay 기상 정보
    axios.get("weather/short", {
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
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
      });
      setIsLoading(false);
    }).catch((error) => {
      console.log(error);
    });

    // 중기 날씨 정보 저장
    // ################  baseDate 보내게 해달라고 백엔드 요청  ####################
    axios.get("weather/mid", {
      params: { numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      setMidTemperInfo(res.data.response);
    }).catch((error) => {
      console.log(error);
    });
  }, []);

  return (
    <div>
      {/* 주간 날씨 테이블 */}
      <TableContainer className='weather-table'>
        <Table>
          {/* 제목행 필요할 경우 주석 활용 */}
          {/* <TableHead>
            <TableRow>
              <TableCell>요일</TableCell>
              <TableCell>최고기온</TableCell>
              <TableCell>최저기온</TableCell>
            </TableRow>
          </TableHead> */}
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
                  <TableCell>{day}</TableCell>
                  <TableCell>
                      {/* <img src='/weather/temMax.png' alt="temMax" width="10%" /> */}
                      {index === 0 ? firstDayInfo.tmx : index === 1 && secondDayInfo.tmx ? secondDayInfo.tmx : midtemperInfo[`taMax${index + 1}`]}℃
                  </TableCell>
                  <TableCell>
                      {/* <img src='/weather/temMin.png' alt="temMin" width="10%" /> */}
                      {index === 0 ? firstDayInfo.tmn : index === 1 && secondDayInfo.tmn ? secondDayInfo.tmn : midtemperInfo[`taMin${index + 1}`]}℃
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
