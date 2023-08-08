import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VideoMessage() {
  const [messageList, setMessageList] = useState([]);
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [currentMessage, setCurrentMessage] = useState(null);
  const userEmail = 'test2@google.com'; // 사용자 이메일

  useEffect(() => {
    // 전체 메세지 리스트 받아오는 함수
    const fetchMessageList = async () => {
      try {
        const res = await axios.get('video', {
          params: { userEmail: userEmail },
        });
        setMessageList(res.data.response); // 전체 메세지 리스트 업데이트
      } catch (error) {
        console.error(error);
      }
    };

    fetchMessageList();
  }, []);

  useEffect(() => {
    // 개별 메세지 받아오는 함수
    const fetchIndividualMessage = async (videoId, userEmail) => {
      try {
        const res = await axios.get('video/message', {
          params: { videoId: videoId, userEmail: userEmail },
        });
        setCurrentMessage(res.data.content); // 개별 메세지 컨텐츠 업데이트
      } catch (error) {
        console.error(error);
      }
    };
  
    if (messageList.length > 0) {
      const filteredMessage = messageList.find(message => message.videoId === currentMessageIndex);
      if (filteredMessage) {
        const { videoId, userEmail } = filteredMessage;
        fetchIndividualMessage(videoId, userEmail);
      }
    }
  }, [currentMessageIndex, messageList]);

  const handlePrevMessage = () => {
    if (currentMessageIndex > 0) {
      setCurrentMessageIndex(currentMessageIndex - 1);
    }
  };

  const handleNextMessage = () => {
    if (currentMessageIndex < messageList.length - 1) {
      setCurrentMessageIndex(currentMessageIndex + 1);
    }
  };

  return (
    <div className="video-message-container">
      <div className="message-content">
        {currentMessage ? (
          <div className="message">
            <p>{currentMessage}</p>
          </div>
        ) : (
          <p>메세지가 없습니다.</p>
        )}
      </div>
      <div className="message-navigation">
        <button onClick={handlePrevMessage} disabled={currentMessageIndex === 0}>이전 메세지</button>
        <button onClick={handleNextMessage} disabled={currentMessageIndex === messageList.length - 1}>다음 메세지</button>
      </div>
    </div>
  );
}

export default VideoMessage;
