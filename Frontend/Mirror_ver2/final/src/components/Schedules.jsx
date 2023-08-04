import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function Schedules(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(schedules.length);

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6PutUnNo7eSvZjrNU924KYbJFooVUHae6MPNSRCSQ49fn62i2ONd6keZFkJUQ5UDfomwVhXpiGYgI-EWIm-BFZ4F3V8H4VygblYaqV4S9pf_JW5RGOz1E5JSvy_zOICv6tBaue4YfQ6TQw25Ny815M_aCgYKAcYSARMSFQFWKvPlwtmk-lUDI6IlKngsM1Y1rA0163';

    axios.get("/schedule/today", {
      params: { accessToken : accessToken },
    }).then((res) => {
      console.log(res.data.response)
      setSchedules(res.data.response)
    })
    .catch((error) => {
      console.log(error);
    });

    axios.get("/schedule/today/count", {
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
      { schedules.slice(0, 3).map((schedule, index) => {
        return <div><li key={index}>{ schedule.summary }</li></div>
      })}
    </>
  );
}

export default Schedules;