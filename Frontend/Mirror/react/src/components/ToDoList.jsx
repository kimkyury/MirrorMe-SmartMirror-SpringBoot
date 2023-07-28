import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function ToDoList(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(0)

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6NRKJmgdNjFoiIPLp8OvPaG49xXtvVNGV7Lj1Xmi15U7xlZJq5xex_l6DqPFkqOKJceoGYmYBA873WUqoHuae2pU9ZsS7ICTXdAwzLNPJrEOX1DRVPpZj4VY_pgs-wCa_nBavY7858BcgoxO4TE7wy-aCgYKAckSARMSFQFWKvPlHQA1NSAUUte5UStmZtDdog0163';

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