import React from 'react';
import './Entrance.css';
import ToDoList from './components/ToDoList';
import Character from './components/Character';

function Entrance(props) {
  return (
    <div>
      <div className="bordered">
        <ToDoList></ToDoList>
      </div>
      <div className="bordered">
        <Character></Character>
      </div>
    </div>
  );
}

export default Entrance;