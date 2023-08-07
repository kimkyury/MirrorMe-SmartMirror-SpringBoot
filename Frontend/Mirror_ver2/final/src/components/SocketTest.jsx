import React, { useState, useEffect } from 'react';

function SocketTest() {
  const [message, setMessage] = useState('');
  const [messageTextArea, setMessageTextArea] = useState('');
  const [webSocket, setWebSocket] = useState(null);
  const [motionResult, setMotionResult] = useState(''); // 추가

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
      setMotionResult(event.data); // 모션 감지 결과 업데이트
      setMessageTextArea(prev => prev + "Receive From Server => " + event.data + "\n");
    };

    return () => {
      socket.close();
    };
  }, []);

  const sendMessage = () => {
    if (webSocket && webSocket.readyState === WebSocket.OPEN) {
      setMessageTextArea(prev => prev + "Send to Server => " + message + "\n");
      webSocket.send(message);
      setMessage('');
    }
  };

  return (
    <div>
      <h2>소켓 통신 테스트222222</h2>
      <form>
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

      <div>
        <h3>Motion Result:</h3>
        <p>{motionResult}</p>
      </div>
    </div>
  );
}

export default SocketTest;
