import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function ToDoList(props) {
  const [schedules, setSchedules] = useState("");
  const [schedulesCount, setSchedulesCount] = useState(0)

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6PB-FKVCkj_YoVM-R1PnLzzs8uFk3UlaoZl6wR7OwQE8RKkiXPxNjiB6yq13nbv-bStmchQKjFB0QeyackaElRPuEW1DlyUj8imbzubzmwbA-gLTuTWQ_BC7TPFM-wG9T_jP_wCNtWweLOfl0tur2UCaCgYKAbUSARMSFQFWKvPlLpo13NlY6diPLx2K5rjQbg0163';

    axios.get("http://192.168.0.31:8080/schedule/today", {
      params: { accessToken : accessToken },
    }).then((res) => {
      setSchedules(res.data.response)
    })
    .catch((error) => {
      console.log(error);
    });

    axios.get("http://192.168.0.31:8080/schedule/today/count", {
      params: { accessToken : accessToken },
    }).then((res) => {
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
      {/* { schedules.map((schedule, index) => {
        return <li>{ schedule.summary }</li>
      })} */}
    </>
  );
}

export default ToDoList;