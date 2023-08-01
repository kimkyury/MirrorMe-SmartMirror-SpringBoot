import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Weather from './components/Weather';
import CurrentDate from './components/CurrentDate';
import Character from './components/Character';
import ToDoList from './components/ToDoList';
import FavoriteNews from './components/FavoriteNews';

import LivingRoom from './LivingRoom';
import Entrance from './Entrance';

function First(props) {
  const [randomNumber, setRandomNumber] = useState(0);

  const [user, setUser] = useState('이소정');

  useEffect(() => {
    const randomNumber = Math.floor(Math.random() * 101);
    setRandomNumber(randomNumber);
  }, []);

  return (
    <div className="App">
      <Link to="/second">Second</Link>
      <Link to="/last">Last</Link>
      <div className="container">
        <div className="weather bordered">
          <Weather></Weather>
        </div>
        <div>
          {randomNumber < 50 ? <h1>거실 UI</h1> : <h1>현관 UI</h1>}
        </div>
        <div className="CurrentDate bordered">
          <CurrentDate></CurrentDate>
        </div>
      </div>
      <div className="mirror-area">
        {/* <div className="bordered">
          {isVideoMessageVisible && <VideoMessage isVisible={true} onClose={closeVideoModal} />}
        </div> */}
        {randomNumber < 50 ? <LivingRoom /> : <Entrance />}
      </div>
    </div>
  );
}

export default First;
