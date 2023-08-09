import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, Button } from '@mui/material'; // CircularProgress와 Button 컴포넌트 추가

import WeekWeather from './WeekWeather';

function TodayWeather(props) {
  const [weatherInfo, setWeatherInfo] = useState({});
  const [ultraInfo, setUltraInfo] = useState([]);
  const [isLoading, setIsLoading] = useState(true); // 로딩 상태 추가
  const [showWeekWeather, setShowWeekWeather] = useState(false); // 주간 날씨 정보 표시 여부 상태 추가

  useEffect(() => {
    let numOfRows = 500;
    let pageNo = 1;
    const currentTime = new Date();
    const year = currentTime.getFullYear();
    const month = String(currentTime.getMonth() + 1).padStart(2, '0');
    const day = String(currentTime.getDate()).padStart(2, '0');
    const baseDate = `${year}${month}${day}`;
    const baseTime = '0200';

    axios
      .get('weather/short', {
        params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
      })
      .then((res) => {
        const todayWeather = res.data.response.filter((data) => data.fcstDate === baseDate);

        const tempertureMin = todayWeather.find((data) => data.category === 'TMN');
        const tempertureMax = todayWeather.find((data) => data.category === 'TMX');
        const popInfo = todayWeather.find((data) => data.category === 'POP');
        const ptyInfo = todayWeather.find((data) => data.category === 'PTY');
        const skyInfo = todayWeather.find((data) => data.category === 'SKY');

        setWeatherInfo({
          tmn: tempertureMin.tmn,
          tmx: tempertureMax.tmx,
          pop: popInfo.pop,
          pty: ptyInfo.pty,
          sky: skyInfo.sky,
        });
      })
      .catch((error) => {
        console.log(error);
      });

    const currentHour = currentTime.getHours();
    let ultrabasetime;

    if (currentTime.getMinutes() > 45) {
      ultrabasetime = `${('0' + currentHour).slice(-2)}30`;
    } else {
      ultrabasetime = `${('0' + (currentHour - 1)).slice(-2)}30`;
    }

    axios
      .get('weather/ultra', {
        params: { baseTime: ultrabasetime, numOfRows: numOfRows, pageNo: pageNo },
      })
      .then((res) => {
        setUltraInfo(res.data.response);
        setIsLoading(false);
      })
      .catch((error) => {
        console.log(error);
        setIsLoading(false);
      });
  }, []);

  let todaySky = '';

  if (weatherInfo.pty === 0) {
    if (weatherInfo.sky === 1) {
      todaySky = '/weather/001.png';
    } else if (weatherInfo.sky === 3) {
      todaySky = '/weather/002.png';
    } else if (weatherInfo.sky === 4) {
      todaySky = '/weather/003.png';
    }
  } else {
    if (weatherInfo.pty === 1) {
      todaySky = '/weather/004.png';
    } else if (weatherInfo.pty === 2) {
      todaySky = '/weather/005.png';
    } else if (weatherInfo.pty === 3) {
      todaySky = '/weather/006.png';
    } else if (weatherInfo.pty === 4) {
      todaySky = '/weather/007.png';
    }
  }

  const handleWeekWeatherClick = () => {
    setShowWeekWeather(true);
  };

  return (
    <div>
      <div className="weather-container">
        {isLoading ? (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '118px' }}>
            <CircularProgress />
          </div>
        ) : (
          <div>
            <div className="weather-left">
              <img src={todaySky} alt="weather icon" />
            </div>
            <div>
              <div className="weather-right">
                <h3>{ultraInfo.t1H}℃</h3>
                <h3 className="temperture">
                  {weatherInfo.tmx}℃ / {weatherInfo.tmn}℃
                </h3>
                <h5 className="chance-of-rain">습도 : {ultraInfo.reh}%</h5>
                <h5 className="chance-of-rain">강수 확률 : {weatherInfo.pop}%</h5>
              </div>
            </div>
            {showWeekWeather && <WeekWeather />}
            {!showWeekWeather && (
              <Button onClick={handleWeekWeatherClick} variant="contained" color="primary">
                더 보기
              </Button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default TodayWeather;