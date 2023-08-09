import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, CircularProgress } from '@mui/material';

import VideoMessagePlus from './VideoMessagePlus';

function VideoMessage() {
  const [messageList, setMessageList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const userEmail = 'test2@google.com';

  useEffect(() => {
    const fetchMessageList = async () => {
      try {
        const res = await axios.get('video', {
          params: { userEmail: userEmail },
        });
        setMessageList(res.data.response);
        setIsLoading(false);
      } catch (error) {
        console.error(error);
        setIsLoading(false);
      }
    };
    fetchMessageList();
  }, []);

  let messageType = '';
  if (messageList.length > 0) {
    if (messageList[0].type === 'v') {
      messageType = '영상';
    } else if (messageList[0].type === 'a') {
      messageType = '음성';
    }
  }
  const [isMessageModalOpen, setIsMessageModalOpen] = useState(false);

  const toggleMessageModal = () => {
    setIsMessageModalOpen(prevState => !prevState);
  };

  return (
    <div>
      {isLoading ? (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '118px' }}>
          <CircularProgress />
        </div>
      ) : (
        messageList.length > 0 ? (
          <div>
            <p>총 {messageList.length}개의 메세지</p>
            <p>{messageList[0].sendUserEmail}님의 {messageType}메세지</p>
            <Button className="btn" onClick={toggleMessageModal}>자세히 보기</Button>
            {isMessageModalOpen && (
              <div className="modal">
                <VideoMessagePlus />
              </div>
            )}
          </div>
        ) : (
          <p>메세지가 없습니다.</p>
        )
      )}
    </div>
  );
}

export default VideoMessage;
