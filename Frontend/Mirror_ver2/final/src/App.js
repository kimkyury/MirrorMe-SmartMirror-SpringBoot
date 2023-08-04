import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import { Button, Snackbar } from '@mui/material';

import './App.css';

import Snackbars from './components/SnackBars'
import Modals from './components/Modals'

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

  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleButtonClick = () => {
    setOpenSnackbar(true);
  };

  const handleSnackbarClose = () => {
    setOpenSnackbar(false);
  };

  return (
    <div>
      <script src="your-react-app.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/@mui/material@5.4.0/dist/umd/mui.min.js" integrity="sha384-8LrLtBm6EuPDcO0B8kxyb3C35R4fOugpzzB9TQo49x/UTgBzw8j08LfkrDiOHl5" crossorigin="anonymous"></script>
      <div className="time">{formattedTimeWithAmPm}</div>
      {/* <div className="btn-container">
        <button className="btn" onClick={toggleVisibility}>뉴스</button> 
        <button className="btn" onClick={toggleVisibility}>가족</button> 
        <button className="btn" onClick={toggleVisibility}>감정</button> 
      </div> */}
      <div className="btn-container">
        <Modals/>
        <Snackbars />
      </div>
    </div>
  );
}

export default App;

