import React, { useState, useEffect } from 'react';

function Tasks(props) {
  const [tasks, setTasks] = useState([]);  // 할 일 목록
  const [tasksCount, setTasksCount] = useState(tasks.length)  // 할 일 목록 개수

  return (
    <div>
      <h3>할 일 목록</h3>
      { tasksCount >= 4 ? <div><p>+ { tasksCount - 3 }</p></div> : null }
      <hr />
      { !tasks.length ? <p>등록된 일정이 없습니다.</p> : null }
      { tasks.slice(0, 3).map((task, index) => {
        return <div><li key={index}>{ task }</li></div>
      })}

    </div>
  );
}

export default Tasks;