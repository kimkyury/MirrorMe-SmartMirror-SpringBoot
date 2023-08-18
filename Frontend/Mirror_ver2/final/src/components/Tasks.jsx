import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CircularProgress } from '@mui/material';

function Tasks(props) {
  const [tasks, setTasks] = useState([]);  // 할 일 목록
  const [tasksCount, setTasksCount] = useState(tasks.length)  // 할 일 목록 개수
  const [isLoading, setIsLoading] = useState(true);

  const accessToken = props.userAccessToken;
  const refreshToken = props.userRefreshToken;

  useEffect(() => {
    const fetchData = async () => {
      try {
        // 스케줄 데이터 가져오기
        const tasksResponse = await axios.get("/tasks", {
          headers: { access_token: accessToken },
          withCredentials: true,
        });
        const response = tasksResponse.data.response;
        setTasks(response[0].items);

        // // 스케줄 카운트 가져오기
        // const countResponse = await axios.get("/tasks/count", {
        //   headers: { access_token : `${accessToken}` },
        //   withCredentials: true,
        // });
        // console.log(countResponse.data.response)
        // setTasksCount(countResponse.data.response);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [accessToken]);

  useEffect (() => {
    setTasksCount(tasks.length);
  }, [tasks]);

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
    <div>
      {isLoading ? (
          <div className="loading-container">
            <CircularProgress />
          </div>
        ) : (
          <div>
            <h3>오늘의 일정</h3>
            {tasksCount >= 4 ? <div><p>+ {tasksCount - 3}</p></div> : null}
            <hr />
            {!tasks.length ? <p>등록된 일정이 없습니다.</p> : null}
            <ul>
              {tasks.slice(0, 3).map((task, index) => (
                <li key={index}>{task.title}</li>
              ))}
            </ul>
          </div>
        )}

    </div>
  );
}

export default Tasks;