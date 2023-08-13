import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VideoMessage() {
  const [messageList, setMessageList] = useState([]);
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [currentMessage, setCurrentMessage] = useState(null);

  const userEmail = 'test@gmail.com'; // 사용자 이메일 추후 수정

  useEffect(() => {
    async function fetchMessageList() {
      try {
        const res = await axios.get('video', {
          params: { userEmail: userEmail },
        });
        setMessageList(res.data.response);
      } catch (error) {
        console.error(error);
      }
    }

    fetchMessageList();
  }, []);

  useEffect(() => {
    if (messageList.length > 0) {
      const firstVideoId = messageList[0].videoId;
      fetchIndividualMessage(firstVideoId);
    }
  }, [messageList]);

  async function fetchIndividualMessage(videoId) {
    try {
      const res = await axios.get('video/message', {
        params: { videoId: videoId },
        responseType: 'blob',
      });

      setCurrentMessage(res.data);

      if (res.data.type === 'v') {
        playVideoMessage(res.data);
      } else if (res.data.type === 'a') {
        playAudioMessage(res.data);
      }
    } catch (error) {
      console.error(error);
    }
  }

  async function fetchStreamingData(url) {
    try {
      const res = await fetch(url);
      const arrayBuffer = await res.arrayBuffer();
      return arrayBuffer;
    } catch (error) {
      console.error(error);
      return null;
    }
  }

  function playAudioMessage(audioUrl) {
    (async () => {
      try {
        const arrayBuffer = await fetchStreamingData(audioUrl);
        if (!arrayBuffer) return;

        const audioContext = new AudioContext();
        const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
        const source = audioContext.createBufferSource();
        source.buffer = audioBuffer;
        source.connect(audioContext.destination);
        source.start();
      } catch (error) {
        console.error(error);
      }
    })();
  }

  function playVideoMessage(videoUrl) {
    (async () => {
      try {
        const arrayBuffer = await fetchStreamingData(videoUrl);
        if (!arrayBuffer) return;

        const video = document.getElementById('video-player');
        video.src = videoUrl;
        video.controls = true;
        video.autoplay = false;
      } catch (error) {
        console.error(error);
      }
    })();
  }

  function handlePrevMessage() {
    if (currentMessageIndex > 0) {
      setCurrentMessageIndex(currentMessageIndex - 1);
    }
  }

  function handleNextMessage() {
    if (currentMessageIndex < messageList.length - 1) {
      setCurrentMessageIndex(currentMessageIndex + 1);
    }
  }

  let messageType = '';
  if (messageList[currentMessageIndex]) {
    messageType = messageList[currentMessageIndex].type === 'v' ? '영상' : '음성';
  }

  return (
    <div className="video-message-container">
      <div className="message-content">
        {currentMessage ? (
          <div className="message">
            <p>
              {messageList[currentMessageIndex].sendUserEmail}님의 {messageType}메세지
            </p>
            <video controls style={{ width:"800", height:"400" }}>
              <source
                src={`video/message?videoId=${messageList[currentMessageIndex].videoId}`}
                // width="800"
                // height="400"
                type="video/mp4"
              />
            </video>
            <p>보낸 날짜 : {messageList[currentMessageIndex].date}</p>
          </div>
        ) : (
          <p>메세지가 없습니다.</p>
        )}
      </div>
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
    </div>
  );
}

export default VideoMessage;
