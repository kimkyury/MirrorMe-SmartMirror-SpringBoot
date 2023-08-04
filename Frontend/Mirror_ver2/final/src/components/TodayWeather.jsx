import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TodayWeather(props) {
  const [weatherInfo, setWeatherInfo] = useState({});
  const [ultraInfo, setUltraInfo] = useState([]);


  useEffect(() => {
    let numOfRows = 500;
    let pageNo = 1;
    const currentTime = new Date();
    const year = currentTime.getFullYear();
    const month = String(currentTime.getMonth() + 1).padStart(2, '0');
    const day = String(currentTime.getDate()).padStart(2, '0');
    const baseDate = `${year}${month}${day}`;
    const baseTime = "0200";

    // 오늘 날짜로 필터링 후 최저 기온, 최고기온, 강수확률, 강수형태, 하늘상태 저장
    axios.get("weather/short", {
      params: { baseDate: baseDate, baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      const todayWeather = res.data.response.filter((data) => data.fcstDate === baseDate);

      const tempertureMin = todayWeather.find((data) => data.category === 'TMN');
      const tempertureMax = todayWeather.find((data) => data.category === 'TMX');
      const popInfo = todayWeather.find((data) => data.category === 'POP');
      const ptyInfo = todayWeather.find((data) => data.category === 'PTY');
      const skyInfo = todayWeather.find((data) => data.category === 'SKY');
      
      setWeatherInfo({
        tmn : tempertureMin.tmn,
        tmx : tempertureMax.tmx,
        pop : popInfo.pop,
        pty : ptyInfo.pty,
        sky : skyInfo.sky
      });
    }).catch((error) => {
      console.log(error);
    });

    const currentHour = currentTime.getHours();
    const ultrabasetime = `${('0' + currentHour).slice(-2)}00`;


    // 초단기 예보 업데이트 시간 고려해서 수정 필요
    axios.get("weather/ultra", {
      params : { baseTime: ultrabasetime, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res => {
      console.log(res.data.response);
      setUltraInfo(res.data.response); // 현재 날씨 업데이트
    })).catch((error) => {
      console.log(error);
    })
  }, []);

  let todaySky = '';
  // 비, 눈 등이 오지 않을 때 하늘 정보 활용
  if (weatherInfo.pty === 0) {
    if (weatherInfo.sky === 1) {
      todaySky = '맑음';
    } else if (weatherInfo.sky === 3) {
      todaySky = '구름많음';
    } else if (weatherInfo.sky === 4) {
      todaySky = '흐림';
    }
  } else { // 아니면 비, 눈 정보 활용
    if (weatherInfo.pty === 1) {
      todaySky = '비';
    } else if (weatherInfo.pty === 2) {
      todaySky = '비와 눈';
    } else if (weatherInfo.pty === 3) {
      todaySky = '눈';
    } else if (weatherInfo.pty === 4) {
      todaySky = '소나기';
    }
  }

  // 값이 구해지기 전에는 로딩중
  // if (weatherInfo.length === 0 || ultraInfo.length === 0) {
  //   return <div>Loading...</div>
  // }

  return (
    <>
      <div className="weather-container">
        <div className="weather-left">
          <div className="weather-icon">
            {/* 추후 수정 */}
            <p>날씨 아이콘</p>
          </div>
          <div className="weather-condition">
            <p>{todaySky}</p>
          </div>
        </div>
        <div>
          <div className="weather-right">
            
            {/* 실시간 기온 */}
            <h3>{ultraInfo.t1H}℃</h3>

            {/* 오늘 최고, 최저기온 */}
            <h3 className="temperture">{weatherInfo.tmx}℃ / {weatherInfo.tmn}℃ </h3>

            {/* 실시간 습도 */}
            <h5 className="chance-of-rain">습도 : {ultraInfo.reh}%</h5>
            <h5 className="chance-of-rain">강수 확률 : {weatherInfo.pop}%</h5>
          </div>
        </div>
      </div>
    </>
  );
}

export default TodayWeather;