import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';

// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';
// import Col from 'react-bootstrap/Col';

import Weather from './components/Weather';
import CurrentDate from './components/CurrentDate';
import ToDoList from './components/ToDoList';
// import VideoMessage from './VideoMessage';
import FavoriteNews from './components/FavoriteNews';
import Character from './components/Character';

function App() {
  const [isVideoMessageVisible, setVideoMessageVisible] = useState(false);
  const [isLivingRoomVisible, setLivingRoomVisible] = useState(false);

  const [user, setUser] = useState('123');

  // Open Living Room Modal
  const openVideoMessageModal = () => {
    setVideoMessageVisible(true);
  };

  // Close Living Room Modal
  const closeVideoMessageModal = () => {
    setVideoMessageVisible(false);
  };
  
  return (
    <div className="App">
      <div className="container">
        <div className="weather bordered">
          <Weather></Weather>
        </div>
        <div className="CurrentDate bordered">
          <CurrentDate></CurrentDate>
        </div>
      </div>
      <div className="mirror-area">
      </div>
      <div className="bordered">
        <ToDoList></ToDoList>
      </div>
      {/* <div className="bordered">
        {isVideoMessageVisible && <VideoMessage isVisible={true} onClose={closeVideoModal} />}
      </div> */}
      {/* <button onClick={openVideoMessageModal}>Open Video Message Modal</button>
      {isVideoMessageVisible && <VideoMessage onClose={closeVideoMessageModal} />} */}
      <div className="bordered">
        <FavoriteNews></FavoriteNews>
      </div>
      <div className="bordered">
        <Character></Character>
      </div>
    </div>
  );
}

export default App;
