import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function ToDoList(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(0)

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6PHpl7nnM5onPZwn3cDbXBqeUIHkb27rtCTp-v6swhKRpr-Agxt7soOI_iJPJqkszFjF21vH-qFOsa8XlUbKsIj3FjK2T54wYXupkUwMDQhql6OIzcyyjS5bvxgPQ9yhlwQKYnmIq5zcX_V3RrFUQMbaCgYKAfESARMSFQFWKvPlIxvv4-uSXbi-StD_tTCjfw0163';

    axios.get("schedule/today", {
      params: { accessToken : accessToken },
    }).then((res) => {
      console.log(res.data.response)
      setSchedules(res.data.response)
    })
    .catch((error) => {
      console.log(error);
    });

    axios.get("schedule/today/count", {
      params: { accessToken : accessToken },
    }).then((res) => {
      console.log(res.data.response)
      setSchedulesCount(res.data.response)
    })
    .catch((error) => {
      console.log(error);
    });
  },[]);

  return (
    <>
      <div>
        <h3>오늘의 일정</h3>
        { schedulesCount >= 4 ? <div><p>+ { schedulesCount - 3 }</p></div> : null }
      </div>
      <hr />
      { !schedules.length ? <p>등록된 일정이 없습니다.</p> : null }
      { schedules.map((schedule, index) => {
        return <div><li key={index}>{ schedule.summary }</li></div>
      })}
    </>
  );
}

export default ToDoList;