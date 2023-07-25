import React from 'react';
import { useState } from 'react';

function VideoMessage(props) {
  const [user, setUser] = useState('123')

  return (
    <div className="video">
      <h3>{ user }님께 보내는 영상 메세지</h3>
      <hr />
      <p>대충 영상 나오는 화면</p>
    </div>
  );
}

export default VideoMessage;