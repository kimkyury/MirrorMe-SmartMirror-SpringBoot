import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

function Weather(props) {
  return (
    <>
      <div className="weather-icon">
        <p>날씨 아이콘</p>
      </div>
      <div>
        <div className="weather-right">
          <h3 className="temperture">현재 기온</h3>
          <h4 className="chance-of-rain">강수 확률</h4>
        </div>
      </div>
    </>
  );
}

export default Weather;