import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function ToDoList(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(0)

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6Nv9yn4eUt2_oMXx4vht3BP716dGrO3_n2-p5_DyGMacdFM0jbs5Ru5uJ0BYPeqB686m9UM_cNnNOWnrJSg1ZQ9X_9lp5FzXJl4XFQ9YBWG8CbpN4eF-l-bEoFu9QRFdC7zlMXSbDW2BOolrhGG7xMmaCgYKAQgSARMSFQFWKvPl_QrKgMFIFDCOfviplZ13Jg0163';

    axios.get("/tasks", {
      params: { accessToken : accessToken },
    }).then((res) => {
      console.log(res.data.response)
      setSchedules(res.data.response)
    })
    .catch((error) => {
      console.log(error);
    });

    axios.get("/tasks/count", {
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