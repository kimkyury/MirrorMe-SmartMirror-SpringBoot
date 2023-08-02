import React from 'react';
import './Entrance.css';
import Schedules from './components/Schedules';
import Tasks from './components/Tasks';
import Character from './components/Character';

function Entrance(props) {
  return (
    <div>
      <div className="bordered">
        <Schedules></Schedules>
      </div>
      <div className="bordered">
        <Tasks></Tasks>
      </div>
      <div className="bordered">
        <Character></Character>
      </div>
    </div>
  );
}

export default Entrance;