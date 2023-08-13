import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function Schedules(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(schedules.length);

  const accessToken = props.userAccessToken;
  const refreshToken = props.userRefreshToken;

  useEffect(() => {
    const fetchData = async () => {
      try {
        // 스케줄 데이터 가져오기
        const scheduleResponse = await axios.get("/schedule/today", {
          headers: { Authorization: `Bearer ${accessToken}` },
          withCredentials: true,
        });
        setSchedules(scheduleResponse.data.response);

        // 스케줄 카운트 가져오기
        const countResponse = await axios.get("/schedule/today/count", {
          headers: { access_token : `${accessToken}` },
          withCredentials: true,
        });
        setSchedulesCount(countResponse.data.response);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [accessToken]);

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