import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, CircularProgress } from '@mui/material';

import VideoMessagePlus from './VideoMessagePlus';

function VideoMessage(props) {
  const [messageList, setMessageList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);

  const [messageKey, setMessageKey] = useState(Date.now());

  const userEmail = props.userEmail;
  const commandMessage = props.commandMessage;
  const userAccessToken = props.userAccessToken;
  const userRefreshToken = props.userRefreshToken;

  useEffect(() => {
    const fetchMessageList = async () => {
      try {
        const res = await axios.get('/video', {
          headers: { access_token: userAccessToken },
          withCredentials: true,
        });
        setMessageList(res.data.response);
        setIsLoading(false);
      } catch (error) {
        console.error(error);
        setIsLoading(false);
      }
    };
    fetchMessageList();
  }, [userAccessToken]);

  function handlePrevMessage() {
    if (currentMessageIndex > 0) {
      setCurrentMessageIndex(currentMessageIndex - 1);
      setMessageKey(Date.now()); // 키를 업데이트하여 다시 렌더링되도록 함
    }
  }

  function handleNextMessage() {
    if (currentMessageIndex < messageList.length - 1) {
      setCurrentMessageIndex(currentMessageIndex + 1);
      setMessageKey(Date.now()); // 키를 업데이트하여 다시 렌더링되도록 함
    }
  }
  const [isMessageModalOpen, setIsMessageModalOpen] = useState(false);

  const toggleMessageModal = () => {
    setIsMessageModalOpen(prevState => !prevState);
  };

  useEffect(() => {
    if (!isMessageModalOpen && commandMessage === "LEFT") {
      toggleMessageModal()
    }
    if (isMessageModalOpen) {
      if (commandMessage === "LEFT") {
        handlePrevMessage()
      } else if (commandMessage === "RIGHT") {
        handleNextMessage()
      }
    }
  }, [commandMessage]);

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
            <Button className="btn" onClick={toggleMessageModal}>자세히 보기</Button>
            {isMessageModalOpen && (
              <div className="modal" style={{ display: 'none' }}>
                <div className="message-navigation">
                  <button onClick={handlePrevMessage} disabled={currentMessageIndex === 0}>
                    이전 메세지
                  </button>
                  <button
                    onClick={handleNextMessage}
                    disabled={currentMessageIndex === messageList.length - 1}
                  >
                    다음 메세지
                  </button>
                </div>
                <div>
                  <p>
                    {messageList[currentMessageIndex].sendUserEmail}님의{' '}
                    {messageList[currentMessageIndex].type === 'v' ? '영상' : '음성'}메세지
                  </p>
                  <VideoMessagePlus 
                    key={messageKey}
                    videoId={messageList[currentMessageIndex].videoId}
                    userAccessToken = {userAccessToken}
                    userRefreshToken = {userRefreshToken}
                  />
                </div>
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
