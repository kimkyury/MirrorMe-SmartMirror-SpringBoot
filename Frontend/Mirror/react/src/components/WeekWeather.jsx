import React, { useState, useEffect } from 'react';
import axios from 'axios';

function WeekWeather(props) {
  const [weekInfo, setWeekInfo] = useState([]);
  const [firstDayInfo, setFirstDayInfo] = useState([]);
  const [secondDayInfo, setSecondDayInfo] = useState([]);
  const [midtemperInfo, setMidTemperInfo] = useState([]);
  const [midrainInfo, setMidRainInfo] = useState([]);

  useEffect(() => {
    // 다음 일주일 정보 채우기
    const currentTime = new Date();
    const currentHour = currentTime.getHours();
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

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
    const day = String(currentTime.getDate()).padStart(2, '0');
    const baseDate = `${year}${month}${day}`;
    const baseTime = "0500";
    let numOfRows = 1000;
    let pageNo = 1;
    
    // 06시가 지났는지를 기준으로, 첫 번째와 두 번째 날짜 결정
    const firstDay = (currentHour < 6 ? `${year}${month}${day}` : `${year}${month}${String(Number(day) + 1).padStart(2, '0')}`);
    const secondDay = currentHour < 6 ? `${year}${month}${String(Number(day) + 1).padStart(2, '0')}` : `${year}${month}${String(Number(day) + 2).padStart(2, '0')}`;
    
    // firstDay 기상 정보
    axios.get("weather/short", {
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      const todayWeather = res.data.response.filter((data) => data.fcstDate === firstDay);
      console.log(todayWeather)

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
      console.log(res.data.response)
      const todayWeather = res.data.response.filter((data) => data.fcstDate === secondDay);
      console.log(todayWeather)
      
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
    }).catch((error) => {
      console.log(error);
    });

    // 중기 날씨 정보 저장
    axios.get("weather/mid", {
      params: { numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      console.log(res.data.response);
      setMidTemperInfo(res.data.response);
    }).catch((error) => {
      console.log(error);
    });
  }, []);

  return (
    <div>
      {/* 요일 정보와 날씨 정보를 함께 출력 */}
      {weekInfo.map((day, index) => (
        <div key={index}>
          <span>
            {day} | 
            최고기온 : {index === 0 ? firstDayInfo.tmx : index === 1 && secondDayInfo.tmx ? secondDayInfo.tmx : midtemperInfo[`taMax${index + 1}`]} | 
            최저기온 : {index === 0 ? firstDayInfo.tmn : index === 1 && secondDayInfo.tmn ? secondDayInfo.tmn : midtemperInfo[`taMin${index + 1}`]}
          </span>
        </div>
      ))}
    </div>
  );
}

export default WeekWeather;
