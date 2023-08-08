import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import { Button, Snackbar } from '@mui/material';

import './App.css';

import Snackbars from './components/SnackBars'
import Modals from './components/Modals'

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  const options = { hour12: true, hour: "2-digit", minute: "2-digit", second: "2-digit" };
  const formattedTime = currentTime.toLocaleTimeString("en-US", options);

  const [timePart, AMPM] = formattedTime.split(" ");
  const formattedTimeWithAmPm = `${AMPM} ${timePart}`;

  const [isVisible, setIsVisible] = useState(false);

  const toggleVisibility = () => {
    setIsVisible(prevState => !prevState);
  };

  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleButtonClick = () => {
    setOpenSnackbar(true);
  };

  const handleSnackbarClose = () => {
    setOpenSnackbar(false);
  };

  const [message, setMessage] = useState('');
  const [messageTextArea, setMessageTextArea] = useState('');
  const [webSocket, setWebSocket] = useState(null);

  useEffect(() => {
    // 웹 서버를 접속한다.
    const socket = new WebSocket("ws://localhost:9998");
    setWebSocket(socket);

    // 소켓 접속이 되면 호출되는 함수
    socket.onopen = () => {
      setMessageTextArea(prev => prev + "Server connect...\n");
    };
    // 소켓 접속이 끝나면 호출되는 함수
    socket.onclose = () => {
      setMessageTextArea(prev => prev + "Server Disconnect...\n");
    };
    // 소켓 통신 중에 에러가 발생되면 호출되는 함수
    socket.onerror = () => {
      setMessageTextArea(prev => prev + "error...\n");
    };
    // 소켓 서버로부터 메시지가 오면 호출되는 함수.
    socket.onmessage = (event) => {
      console.log(event)
      setMessageTextArea(prev => prev + "Receive From Server => " + event.data + "\n");
    };

    return () => {
      socket.close();
    };
  }, []);

  const sendMessage = () => {
    if (webSocket && webSocket.readyState === WebSocket.OPEN) {
      setMessageTextArea(prev => prev + "Send to Server => " + message + "\n");
      // 웹 소켓으로 메시지 전송
      webSocket.send(message);
      // 메시지 초기화
      setMessage('');
    }
  };

  return (
    <div>
      <div className="time">{formattedTimeWithAmPm}</div>
      <div className="btn-container">
        <Modals/>
        <Snackbars />
      </div>
      <form className="socket">
        {/* 서버로 메시지를 보낼 텍스트 박스 */}
        <input
          id="textMessage"
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        {/* 전송 버튼 */}
        <input onClick={sendMessage} value="Send" type="button" />
        {/* 접속 종료 버튼 */}
        <input onClick={() => webSocket.close()} value="Disconnect" type="button" />
      </form>
      <br />
      {/* 출력 area */}
      <textarea
        id="messageTextArea"
        rows="10"
        cols="50"
        value={messageTextArea}
        readOnly
      ></textarea>
    </div>
  );
}

export default App;
