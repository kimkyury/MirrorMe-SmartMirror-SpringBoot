import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Weather(props) {
  const [weatherInfo, setWeatherInfo] = useState([]);
  const [temperatureInfo, setTemperatureInfo] = useState([]);

  useEffect(() => {
    const numOfRows = 500;
    const pageNo = 1;
    const baseTime = "0200"; // 기준 시간 고정

    // 최고, 최저 기온 정보 요청
    axios.get("weather/short", {
      params: { baseTime: baseTime, numOfRows: numOfRows, pageNo: pageNo },
    }).then((res) => {
      console.log(res.data.response);
      setTemperatureInfo(res.data.response); // 최고 및 최저 기온 정보 업데이트
    }).catch((error) => {
      console.log(error);
    });

    const currentTime = new Date();
    const currentHour = currentTime.getHours();
    const isBeforeDawn = currentHour >= 2 && currentHour < 5;

    // 새벽 두시 ~ 새벽 다섯시 사이가 아닐 때는 현재 시간을 기준으로 날씨 정보 요청
    if (!isBeforeDawn) {
      const getClosestTime = (currentTime) => { // 베이스시간 구하기
        const baseTimes = [5, 8, 11, 14, 17, 20, 23]; // 시간 목록 (새벽 두시는 이미 요청했으므로 제외)
        let closestTime = baseTimes[0];
        for (const time of baseTimes) {
          if (Math.abs(currentTime - time) < Math.abs(currentTime - closestTime)) {
            closestTime = time;
          }
        }
        return closestTime;
      };

      const closestTime = getClosestTime(currentHour);
      const weatherBaseTime = `${('0' + closestTime).slice(-2)}00`;

      // 날씨 정보 요청
      axios.get("weather/short", {
        params: { baseTime: weatherBaseTime, numOfRows: numOfRows, pageNo: pageNo },
      }).then((res) => {
        console.log(res.data.response);
        setWeatherInfo(res.data.response); // 날씨 정보 업데이트
      }).catch((error) => {
        console.log(error);
      });
    }
  }, []);

  let today = '';
  // 비, 눈 둥이 오지 않을 때 하늘 정보 활용
  if (temperatureInfo.pty === 0) {
    if (temperatureInfo.sky === 1) {
      today = '맑음';
    } else if (temperatureInfo.sky === 3) {
      today = '구름많음';
    } else if (temperatureInfo.sky === 4) {
      today = '흐림';
    }
  } else { // 아니면 비, 눈 정보 활용
    if (temperatureInfo.pty === 1) {
      today = '비';
    } else if (temperatureInfo.pty === 2) {
      today = '비와 눈';
    } else if (temperatureInfo.pty === 3) {
      today = '눈';
    } else {
      today = '소나기';
    }
  }

  // 값이 있는 경우 화면에 표시
  if (temperatureInfo.length === 0 || weatherInfo.length === 0) {
    return <div>Loading...</div>
  }

  return (
    <>
      <div className="weather-container">
        <div className="weather-left">
          <div className="weather-icon">
            {/* 추후 수정 */}
            <p>날씨 아이콘</p>
          </div>
          <div className="weather-condition">
            <p>{today}</p>
          </div>
        </div>
        <div>
          <div className="weather-right">
            <h3 className="temperture">{temperatureInfo.tmx}℃ / {temperatureInfo.tmn}℃ </h3>
            <h5 className="chance-of-rain">습도 : {weatherInfo.reh}%</h5>
            <h5 className="chance-of-rain">강수 확률 : {weatherInfo.pop}%</h5>
          </div>
        </div>
      </div>
    </>
  );
}

export default Weather;