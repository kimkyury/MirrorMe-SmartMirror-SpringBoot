import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';

// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';
// import Col from 'react-bootstrap/Col';

import Weather from './components/Weather';
import CurrentDate from './components/CurrentDate';
import ToDoList from './components/ToDoList';
import VideoMessage from './VideoMessage';
import FavoriteNews from './components/FavoriteNews';
import Character from './components/Character';

import LivingRoom from './LivingRoom';
import Entrance from './Entrance';

function App() {
  const [isVideoMessageVisible, setVideoMessageVisible] = useState(false);
  const [randomNumber, setRandomNumber] = useState(0);

  const [user, setUser] = useState('이소정');

  // Open Living Room Modal
  const openVideoMessageModal = () => {
    setVideoMessageVisible(true);
  };

  // Close Living Room Modal
  const closeVideoMessageModal = () => {
    setVideoMessageVisible(false);
  };

  useEffect(() => {
    const randomNumber = Math.floor(Math.random() * 101);
    setRandomNumber(randomNumber);
  }, []);
  
  return (
    <div className="App">
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
      </div>
      {/* <div className="bordered">
        {isVideoMessageVisible && <VideoMessage isVisible={true} onClose={closeVideoModal} />}
      </div> */}
      <button onClick={openVideoMessageModal}>Open Video Message Modal</button>
      {isVideoMessageVisible && <VideoMessage onClose={closeVideoMessageModal} />}
      {randomNumber < 50 ? <LivingRoom /> : <Entrance />}
    </div>
  );
}

export default App;
