import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';

import './App.css';

import TodayWeather from './components/TodayWeather';
import WeekWeather from './components/WeekWeather';

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  const options = { hour12: true, hour: "2-digit", minute: "2-digit", second: "2-digit" };
  const formattedTime = currentTime.toLocaleTimeString("en-US", options);

  const [timePart, AMPM] = formattedTime.split(" ");
  const formattedTimeWithAmPm = `${AMPM} ${timePart}`;

  const [isVisible, setIsVisible] = useState(false);

  const toggleVisibility = () => {
    setIsVisible(prevState => !prevState);
  };

  return (
    <div>
      <div className="time">{formattedTimeWithAmPm}</div>
      <div className="btn-container"><button className="btn" onClick={toggleVisibility}>토글 컴포넌트</button>\</div>
      <div className="animated-container">
        <CSSTransition
          in={isVisible}
          timeout={300}
          classNames="slide"
          unmountOnExit
        >
          <div className="animated-content">
            <div className="bordered">
              <TodayWeather />
            </div>
            <div className="bordered">
              <WeekWeather />
            </div>
          </div>
        </CSSTransition>
      </div>
    </div>
  );
}

export default App;

