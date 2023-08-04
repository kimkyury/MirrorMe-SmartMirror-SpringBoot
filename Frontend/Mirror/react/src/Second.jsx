import React from 'react';
import WeekWeather from './components/WeekWeather';

import NavBar from './NavBar';

function Second(props) {
  return (
    <div className="App">
      <div>
        <NavBar></NavBar>
      </div>
      <p>Second</p>
      <WeekWeather></WeekWeather>
    </div>
  );
}

export default Second;