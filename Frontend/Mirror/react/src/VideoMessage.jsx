import React from 'react';
import { useState } from 'react';
import './VideoMessage.css';

function VideoMessage(props) {
  const [user, setUser] = useState('123');

  // 모달 닫기 함수 호출
  const handleClose = () => {
    props.onClose();
  };

  return (
    <div>
      <div className="modal-overlay">
        <div className="video-message-modal">
          <h3>{user}님께 보내는 영상 메세지</h3>
          <hr />
          <p>대충 영상 나오는 화면</p>
          <button onClick={handleClose}>Close</button>
        </div>
      </div>
    </div>
  );
}

export default VideoMessage;
