import React, { useState, useEffect } from 'react';
import socketIOClient from 'socket.io-client';

const ENDPOINT = "http://127.0.0.1:4001";

function SocketTest(props) {
  const [response, setResponse] = useState("통신을 해보고 싶어요");

  useEffect(() => {
    const socket = socketIOClient(ENDPOINT);
    socket.on("FromAPI", data => {
      setResponse(data);
    });
  }, []);

  return (
    <div>
      <h2>SocketTest</h2>
      <p>{ response }</p>
    </div>
  );
}

export default SocketTest;