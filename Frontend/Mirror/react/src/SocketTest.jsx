import React, { useState, useEffect } from 'react';

function SocketTest() {
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
      <h2>소켓 통신 테스트222222</h2>
      <form>
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

export default SocketTest;