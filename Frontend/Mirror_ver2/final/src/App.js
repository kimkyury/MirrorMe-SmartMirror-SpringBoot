import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import { Button, Snackbar } from '@mui/material';
import axios from 'axios';

import './App.css';

import Logo from './components/Logo';
import Snackbars from './components/SnackBars';
import Modals from './components/Modals';
import PresentCardList from './components/PresentCardList';
import GestureHelp from './components/GestureHelp';
import CommandHelp from './components/CommandHelp';
import VoiceAnimation from './components/VoiceAnimation';


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

  // 출현 후 특정 시간 이후에 사라짐
  useEffect (() => {
    if (isVisible) {
      const timeout = setTimeout(() => {
        setIsVisible(false);
      }, 7000);

      return () => {
        clearTimeout(timeout);
      };
    }
  }, [isVisible])

  // 스낵바
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

  const [snackbarsCommandMessage, setSnackbarsCommandMessage] = useState('');
  const [tts, setTts] = useState('');
  const [ttsType, setTtsType] = useState('');

  // 이메일 및 토큰
  const [userEmail, setUserEmail] = useState('');
  const [userAccessToken, getUserAccessToken] = useState('');
  const [userRefreshToken, getUserRefreshToken] = useState('');

  const [modalsCommandMessage, setModalsCommandMessage] = useState('');
  const [youtubeKey, setYoutubeKey] = useState('');

  const [messageReceiver, setMessageReceiver] = useState('');
  const [mirrorSaying, setMirrorSaying] = useState(false);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:9998");
    setWebSocket(socket);

    socket.onopen = () => {
      setMessageTextArea(prev => prev + "Server connect...\n");
    };
    socket.onclose = () => {
      setMessageTextArea(prev => prev + "Server Disconnect...\n");
    };
    socket.onerror = () => {
      setMessageTextArea(prev => prev + "error...\n");
    };
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setSnackbarsCommandMessage(data.order);
      setModalsCommandMessage(data.order);
      setMessageTextArea(prev => prev + "Receive From Server => " + snackbarsCommandMessage + "\n");
      if (data.order === 'TTS') {  // TTS
        setTts(data.query.content);
        setMirrorSaying(true);
        setTtsType(data.query.type);
        setMessageTextArea(prev => prev + "Receive From Server => " + tts + "\n");
      } else if (data.order === 'USERINFO') { // userEmail 받아오기
        setUserEmail(data.query.email);
      } else if (data.order === 'YOUTUBE') {  // 유튜브
        setYoutubeKey(data.query.key);
      } else if (data.order === 'MESSAGESENDSTART') {  // 메세지 전송
        setMessageReceiver(data.query.receiver);
      } else if (data.order === 'TTS') { // 거울 말 시작한다
        setMirrorSaying(true);
      } else if (data.order === 'TTS_end') { // 거울 말 끝낸다
        setMirrorSaying(false);
      }
    };

    console.log(userEmail);

    return () => {
      socket.close();
    };
  }, []);

  useEffect(() => {
    if (userEmail) {
      const fetchData = async () => {
        try {
          // 스케줄 데이터 가져오기
          const tokenResponse = await axios.get("/oauth/tokens", {
            params: { userEmail: userEmail },
          });
          const response = tokenResponse.data.response;
            getUserAccessToken(response.accessToken);
            getUserRefreshToken(response.refreshToken);

        } catch (error) {
          console.error('Error fetching data:', error);
        }

      };

      fetchData();
    }
  }, [userEmail]);

  const sendMessage = () => {
    if (webSocket && webSocket.readyState === WebSocket.OPEN) {
      setMessageTextArea(prev => prev + "Send to Server => " + message + "\n");
      webSocket.send(message);
      setMessage('');
    }
  };

  return (
    <div className="App">
      <script src="https://cdn.jsdelivr.net/npm/react@17.0.2/umd/react.production.min.js" integrity="sha384-7hS1HB/8C1l1g6XTaKP2HvbQg/2jBzXB2X0J/+Uz3Pkb3q1/4H0z2cVBMzqGtJ3" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/react-dom@17.0.2/umd/react-dom.production.min.js" integrity="sha384-Rn9HT+yy0cAmzD7h4p9BaaVG6g2PfE8ii+05BuYp9gRBy2Cjgr99WQQpkKd3m9L/" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/@mui/system@5.4.3/dist/mui.min.js" integrity="sha384-oFyjBA1gBAq3z2f3Q2ikzGq/KJQ2BlLJpLuH6lg6b4RtrR+vjp5b3HYJoLk6MBo2" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/@mui/material@5.4.3/dist/mui.min.js" integrity="sha384-3nQFj60gZkVx0nq0HP3zqv4mAP+q0/w7foV7mqHn6g+LrTADwG8zBks6XQfnwTo7" crossorigin="anonymous"></script>
      {!userEmail ? 
        <Logo/> :
        <div>
          <div className="time">{formattedTimeWithAmPm}</div>
          <div className="btn-container">
            <Modals
              commandMessage={modalsCommandMessage}
              youtubeKey={youtubeKey}
              userEmail={userEmail}
              messageReceiver={messageReceiver}
            />
            <Snackbars
              commandMessage={snackbarsCommandMessage}
              tts={tts}
              ttsType={ttsType}
              userAccessToken={userAccessToken}
              userRefreshToken={userRefreshToken}
            />
          </div>
          <button onClick={toggleVisibility}>
            {isVisible ? 'PresentCard 숨기기' : 'PresentCard 보이기'}
          </button>
          <div>
            <CSSTransition
              in={isVisible}
              timeout={500}
              classNames="present-card"
              unmountOnExit
            >
              <div>
                <PresentCardList />
              </div>
            </CSSTransition>
          </div>
          <div>
            {/* <CommandHelp /> */}
            {/* <GestureHelp /> */}
          </div>
          <form className="socket">
            <input
              id="textMessage"
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
            />
            <input onClick={sendMessage} value="Send" type="button" />
            <input onClick={() => webSocket.close()} value="Disconnect" type="button" />
          </form>
          <br />
          <textarea
            id="messageTextArea"
            rows="10"
            cols="50"
            value={messageTextArea}
            readOnly
          ></textarea>
          <div className="voice-animation">
            {mirrorSaying && <VoiceAnimation />}
          </div>
        </div>
      }
    </div>
  );
}

export default App;
