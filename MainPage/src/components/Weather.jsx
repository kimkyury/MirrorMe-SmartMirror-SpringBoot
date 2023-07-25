import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

function Weather(props) {
  return (
    <>
      <div>
        <p>날씨 아이콘</p>
      </div>
      <div>
        <div>
          <h3>현재 기온</h3>
          <h4>강수 확률</h4>
        </div>
      </div>
    </>
  );
}

export default Weather;