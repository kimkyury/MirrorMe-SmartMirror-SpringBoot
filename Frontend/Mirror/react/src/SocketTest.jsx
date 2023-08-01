import React, { useState, useEffect } from 'react';
import socketIOClient from 'socket.io-client';


function SocketTest(props) {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const socket = socketIOClient('http://192.168.30.151:3000/');

  useEffect(() => {
    socket.on('message', (data) => {
      setResponse(data);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleRequestSocket = () => {
    socket.emit('message', message);
    setMessage('');
  };

	return (
		<div>
			<h2>통신 연결 테스트</h2>
      <button onClick={handleRequestSocket}>전송</button>
      <input type="text" value={message} onChange={handleChange} />
      <strong>Send : </strong> { message }
      <div>
        <strong>서버 응답:</strong> {response}
      </div>
		</div>
	)

}

export default SocketTest;