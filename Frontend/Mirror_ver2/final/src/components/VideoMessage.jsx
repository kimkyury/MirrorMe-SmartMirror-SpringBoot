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
    const fetchIndividualMessage = async (videoId) => {
      try {
        const res = await axios.get('video/message', {
          params: { videoId: videoId }
        });
        console.log(res.data.response)
        setCurrentMessage(res.data.response);
      } catch (error) {
        console.error(error);
      }
    };
  
    if (messageList.length > 0) {
      const filteredMessage = messageList.find(message => message.videoId === currentMessageIndex + 4); // videoId는 4부터 시작
      if (filteredMessage) {
        fetchIndividualMessage(filteredMessage.videoId);
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

  let messageType = '';
  if (currentMessage) {
    if (currentMessage.type === 'v') {
      messageType = '영상';
    } else if (currentMessage.type === 'a') {
      messageType = '음성';
    }
  }

  return (
    <div className="video-message-container">
      <div className="message-content">
        {currentMessage ? (
          <div className="message">
            <p>{currentMessage.sendUserEmail}님의 {messageType}메세지</p>
            {currentMessage.type === 'v' ? (
              <video controls>
                {/* 주소 줄여서 수정 필요 */}
                <source src={currentMessage.imgStr} type="video/mp4" />
              </video>
            ) : (
              <p>{currentMessage.content}</p>
            )}
            <p>보낸 날짜 : {currentMessage.date}</p>
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
