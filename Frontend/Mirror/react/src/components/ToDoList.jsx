import React from 'react';
import { useState } from 'react';

function ToDoList(props) {
  const [toDoList, setTodoList] = useState([
    '일정 1',
    '일정 2',
    '일정 3',
  ]);

  return (
    <>
      <h3>오늘의 일정</h3>
      { toDoList.map((item, index) => {
        return <li>{ item }</li>
      })}
    </>
  );
}

export default ToDoList;