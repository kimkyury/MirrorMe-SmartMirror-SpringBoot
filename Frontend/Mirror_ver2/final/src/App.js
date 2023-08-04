import React, { useState } from 'react';
import { CSSTransition } from 'react-transition-group';
import './App.css';

import TodayWeather from './components/TodayWeather';
import WeekWeather from './components/WeekWeather';

function App() {
  const [isVisible, setIsVisible] = useState(false);

  const toggleVisibility = () => {
    setIsVisible(prevState => !prevState);
  };

  return (
    <div>
      <button onClick={toggleVisibility}>토글 컴포넌트</button>
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
