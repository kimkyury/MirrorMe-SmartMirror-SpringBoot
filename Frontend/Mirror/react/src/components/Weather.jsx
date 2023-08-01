import React, { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

function Weather(props) {
  const [weatherInfo, setWeatherInfo] = useState([]);


  return (
    <>
      <div className="weather-container">
        <div className="weather-left">
          <div className="weather-icon">
            <p>날씨 아이콘</p>
          </div>
          <div className="weather-condition">
            <p>맑음</p>
          </div>
        </div>
        <div>
          <div className="weather-right">
            <h3 className="temperture">현재 기온</h3>
            <h5 className="chance-of-rain">강수 확률</h5>
          </div>
        </div>
      </div>
    </>
  );
}

export default Weather;