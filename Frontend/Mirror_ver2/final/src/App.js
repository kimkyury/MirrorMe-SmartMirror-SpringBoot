import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import { Button, Snackbar } from '@mui/material';

import './App.css';

import Logo from './components/Logo';
import Snackbars from './components/SnackBars';
import Modals from './components/Modals';
import PresentCardList from './components/PresentCardList';

const userEmail = 'test2@gmail.com'; // 사용자 이메일 추후 수정

function App() {
  // 현재 시간
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

  // 스낵바
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleButtonClick = () => {
    setOpenSnackbar(true);
  };

  const handleSnackbarClose = () => {
    setOpenSnackbar(false);
  };

  // Socket
  const [message, setMessage] = useState('');
  const [messageTextArea, setMessageTextArea] = useState('');
  const [webSocket, setWebSocket] = useState(null);

  // Snackbars Props
  const [snackbarsCommandMessage, setSnackbarsCommandMessage] = useState('');
  const [tts, setTts] = useState('');
  const [ttsType, setTtsType] = useState('');
  const [userEmail, setUserEmail] = useState('');

  // Modals Props
  const [modalsCommandMessage, setModalsCommandMessage] = useState('');
  const [youtubeKey, setYoutubeKey] = useState('');

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
      const data = JSON.parse(event.data);
      setSnackbarsCommandMessage(data.order);
      setModalsCommandMessage(data.order);
      setMessageTextArea(prev => prev + "Receive From Server => " + snackbarsCommandMessage + "\n");
      if (data.order == 'TTS') {
        setTts(data.query.content);
        setTtsType(data.query.type);
        setMessageTextArea(prev => prev + "Receive From Server => " + tts + "\n");
      } else if (data.order == 'USERINFO') {
        console.log(data.query.email);
        setUserEmail(data.query.email);
      } else if (data.order == 'YOUTUBE') {
        setYoutubeKey(data.query.key);
      }
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
      {/* 사용자 이메일 정보 넘겨받기 전까지 Logo Component 보여주기 */}
      <script src="https://cdn.jsdelivr.net/npm/react@17.0.2/umd/react.production.min.js" integrity="sha384-7hS1HB/8C1l1g6XTaKP2HvbQg/2jBzXB2X0J/+Uz3Pkb3q1/4H0z2cVBMzqGtJ3" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/react-dom@17.0.2/umd/react-dom.production.min.js" integrity="sha384-Rn9HT+yy0cAmzD7h4p9BaaVG6g2PfE8ii+05BuYp9gRBy2Cjgr99WQQpkKd3m9L/" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/@mui/system@5.4.3/dist/mui.min.js" integrity="sha384-oFyjBA1gBAq3z2f3Q2ikzGq/KJQ2BlLJpLuH6lg6b4RtrR+vjp5b3HYJoLk6MBo2" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/@mui/material@5.4.3/dist/mui.min.js" integrity="sha384-3nQFj60gZkVx0nq0HP3zqv4mAP+q0/w7foV7mqHn6g+LrTADwG8zBks6XQfnwTo7" crossorigin="anonymous"></script>
      {userEmail ? (
        <Logo/>
        ) :(
        <div>
          <div className="time">{formattedTimeWithAmPm}</div>
          <div className="btn-container">
            {/* <sendMessage/> */}
            <Modals
              commandMessage={modalsCommandMessage}
              youtubeKey={youtubeKey}
            />
            <Snackbars
              commandMessage={snackbarsCommandMessage}
              tts={tts}
              ttsType={ttsType}
              userEmail={userEmail}
            />
          </div>
          <button onClick={toggleVisibility}>
            {isVisible ? 'PresentCard 숨기기' : 'PresentCard 보이기'}
          </button>
          <div>
            <CSSTransition
              in={isVisible} // Control whether the transition is active
              timeout={500} // Duration of the transition in milliseconds
              classNames="present-card" // CSS class names for the transition states
              unmountOnExit // Remove the component from the DOM when not in the 'in' state
            >
              <div>
                <PresentCardList />
              </div>
            </CSSTransition>
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
        )}
    </div>
  );
}

export default App;
