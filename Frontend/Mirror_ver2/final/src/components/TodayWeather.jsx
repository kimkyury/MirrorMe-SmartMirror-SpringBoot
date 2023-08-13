import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, Button } from '@mui/material';

import '../css/Weather.css';
import WeekWeather from './WeekWeather';

function TodayWeather(props) {
  const [weatherInfo, setWeatherInfo] = useState({});
  const [ultraInfo, setUltraInfo] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const [imageLoading, setImageLoading] = useState(true);
  const [showWeekWeather, setShowWeekWeather] = useState(false);

  useEffect(() => {
    const numOfRows = 500;
    const pageNo = 1;
    const currentTime = new Date();
    const year = currentTime.getFullYear();
    const month = String(currentTime.getMonth() + 1).padStart(2, '0');
    const currentHour = currentTime.getHours();
    let day = '';
    
    // 02:45 이전 날짜 처리
    if (currentHour > 3) {
      day = String(currentTime.getDate()).padStart(2, '0');
    } else if (currentHour === 2 && currentTime.getMinutes() > 45) {
      day = String(currentTime.getDate()).padStart(2, '0');
    } else {
      day = String(currentTime.getDate()-1).padStart(2, '0');
    }
    
    const baseDate = `${year}${month}${day}`;
    const baseTime = '0200'; // 최저 기온 수신 가능 시간
    let today = `${year}${month}${currentTime.getDate()}`;

    axios.get('weather/short', { // 최고, 최저 기온, 하늘 상태
        params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
      })
      .then((res) => { // 오늘 날짜의 필요 정보 저장
        const todayWeather = res.data.response.filter((data) => data.fcstDate === today);

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

        const skyImages = ['/weather/001.png', '/weather/002.png', '/weather/003.png', '/weather/004.png', '/weather/005.png', '/weather/006.png', '/weather/007.png'];
        const imagePromises = skyImages.map((src) => {
          return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = src;
            img.onload = resolve;
            img.onerror = reject;
          });
        });

        Promise.all(imagePromises)
          .then(() => {
            setImageLoading(false); // 이미지 로딩 완료
          })
          .catch((error) => {
            console.error(error);
            setIsLoading(false);
          });
      })
      .catch((error) => {
        console.log(error);
        setIsLoading(false);
      });

    // 실시간 기온, 습도 정보 요청
    let ultrabasetime;
    // 매 45분마다 정보 업데이트, 베이스 시간은 매 시 30분
    if (currentTime.getMinutes() > 45) {
      ultrabasetime = `${('0' + currentHour).slice(-2)}30`;
    } else {
      ultrabasetime = `${('0' + (currentHour - 1)).slice(-2)}30`;
    }

    axios.get('weather/ultra', { // 실시간 기온, 습도
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

  // 아이콘 출력을 위한 화면 상태
  let todaySky = '';

  if (weatherInfo.pty === 0) { // 비, 눈 비해당
    if (weatherInfo.sky === 1) {
      todaySky = '/weather/001.png';
    } else if (weatherInfo.sky === 3) {
      todaySky = '/weather/002.png';
    } else if (weatherInfo.sky === 4) {
      todaySky = '/weather/003.png';
    }
  } else { // 비, 눈 해당
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

  // 주간 날씨 정보 펼치기 ///////////////////////////////// 모션 or 음성 연결 필요
  const handleWeekWeatherClick = () => {
    setShowWeekWeather(true);
  };

  return (
    <div>
      <div className="weather-container">
        {isLoading || imageLoading ? (
          // 가운데에 정렬하고 싶다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          <div className="loading-container">
            <CircularProgress />
          </div>
        ) : (
          <div>
            <div className="weather-content">
              <div className="weather-icon">
                <img src={todaySky} alt="weather icon" width="100%"/>
              </div>
              <div className="weather-info">
                <h3>{ultraInfo.t1H}℃</h3>
                <h3 className="temperture">
                  {weatherInfo.tmx}℃ / {weatherInfo.tmn}℃
                </h3>
                <h5 className="chance-of-rain">습도 : {ultraInfo.reh}%</h5>
                <h5 className="chance-of-rain">강수 확률 : {weatherInfo.pop}%</h5>
              </div>
            </div>

            {/* Accordion 처럼 넣어도 될 듯 */}
            <div className="weather-button">
              {showWeekWeather ? (
                <WeekWeather />
              ) : (
                <Button onClick={handleWeekWeatherClick} variant="contained" color="primary">
                  더 보기
                </Button>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default TodayWeather;
