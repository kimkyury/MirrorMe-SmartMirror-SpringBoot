import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

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

  return (
    <div className="App">
      <header className="App-header">
        <div className="time">{formattedTimeWithAmPm}</div>
      </header>
    </div>
  );
}

export default App;

