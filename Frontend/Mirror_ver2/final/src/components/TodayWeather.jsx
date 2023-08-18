import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress, Button } from '@mui/material';

import '../css/Weather.css';
import WeekWeather from './WeekWeather';
const houseHoldId = 1;

function TodayWeather(props) {
  const [weatherInfo, setWeatherInfo] = useState({});
  const [ultraInfo, setUltraInfo] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const [imageLoading, setImageLoading] = useState(true);
  // const [showWeekWeather, setShowWeekWeather] = useState(false);

  const showWeekWeather = props.showWeekWeather;

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
        params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo, houseHoldId: houseHoldId },
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

        const skyImages = [
          `${process.env.PUBLIC_URL}/images/weather/001.png`,
          `${process.env.PUBLIC_URL}/images/weather/002.png`,
          `${process.env.PUBLIC_URL}/images/weather/003.png`,
          `${process.env.PUBLIC_URL}/images/weather/004.png`,
          `${process.env.PUBLIC_URL}/images/weather/005.png`,
          `${process.env.PUBLIC_URL}/images/weather/006.png`,
          `${process.env.PUBLIC_URL}/images/weather/007.png`
        ];
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
        params: { baseTime: ultrabasetime, numOfRows: numOfRows, pageNo: pageNo, houseHoldId: houseHoldId },
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

  const skyicons = {1: '001.png', 2: '002.png', 3: '003.png', 4: '004.png', 5: '005.png', 6: '006.png', 7: '007.png'};
  const skys = {1: '맑음', 2: '구름많음', 3: '흐림', 4: '비', 5: '눈/비', 6: '눈', 7: '소나기'};

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
                <img src={`${process.env.PUBLIC_URL}/images/weather/${skyicons[weatherInfo.sky-1]}`} alt="weather icon" width="100%"/>
                <h2>{skys[weatherInfo.sky-1]}</h2>
              </div>
              <div className="weather-info">
                <h2>{ultraInfo.t1H}℃</h2>
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
                <Button onClick={showWeekWeather} variant="contained" color="primary" style={{ display: 'none' }}>
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
