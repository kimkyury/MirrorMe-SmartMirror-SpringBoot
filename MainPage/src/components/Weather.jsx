import React from 'react';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

function Weather(props) {
  return (
    <Container>
      <Col>
        <p>날씨 아이콘</p>
      </Col>
      <Col>
        <Row>
          <h3>현재 기온</h3>
        </Row>
        <Row>
          <h4>강수 확률</h4>
        </Row>
      </Col>
    </Container>
  );
}

export default Weather;