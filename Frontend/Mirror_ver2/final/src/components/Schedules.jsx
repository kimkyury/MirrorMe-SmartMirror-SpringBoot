import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress } from '@mui/material';

function Schedules(props) {
  const [schedules, setSchedules] = useState([]);
  const [schedulesCount, setSchedulesCount] = useState(schedules.length);
  const [isLoading, setIsLoading] = useState(true);

  const userAccessToken = props.userAccessToken;
  const userRefreshToken = props.userRefreshToken;

  useEffect(() => {
    const fetchData = async () => {
      try {
        // 스케줄 데이터 가져오기
        const scheduleResponse = await axios.get("/schedule/today", {
          headers: { access_token: userAccessToken },
          withCredentials: true,
        });
        setSchedules(scheduleResponse.data.response);

        // 스케줄 카운트 가져오기
        const countResponse = await axios.get("/schedule/today/count", {
          headers: { access_token : userAccessToken },
          withCredentials: true,
        });
        setSchedulesCount(countResponse.data.response);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [userAccessToken]);

  useEffect (() => {
    if (isLoading) {
      const timeout = setTimeout(() => {
        setIsLoading(false);
      }, 2000);

      return () => {
        clearTimeout(timeout);
      };
    }
  }, [isLoading])

  return (
    <>
        {isLoading ? (
          <div className="loading-container">
            <CircularProgress />
          </div>
        ) : (
          <div>
            <h3>오늘의 일정</h3>
            {schedulesCount >= 4 ? <div><p>+ {schedulesCount - 3}</p></div> : null}
            <hr />
            {!schedules.length ? <p>등록된 일정이 없습니다.</p> : null}
            <ul>
              {schedules.slice(0, 3).map((schedule, index) => (
                <li key={index}>{schedule.summary}</li>
              ))}
            </ul>
          </div>
        )}
    </>
  );
}

export default Schedules;