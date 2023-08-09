// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// function VideoMessage() {
//   const [messageList, setMessageList] = useState([]);
//   const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
//   const [currentMessage, setCurrentMessage] = useState(null);
//   const userEmail = 'test2@google.com'; // 사용자 이메일

//   useEffect(() => {
//     const fetchMessageList = async () => {
//       try {
//         const res = await axios.get('video', {
//           params: { userEmail: userEmail },
//         });
//         setMessageList(res.data.response);
//       } catch (error) {
//         console.error(error);
//       }
//     };

//     fetchMessageList();
//   }, []);

//   const fetchIndividualMessage = async (index) => {
//     try {
//       const res = await axios.get('video/message', {
//         params: { videoId: messageList[index].videoId }
//       });
//       console.log(res.data)
//       setCurrentMessage(res.data);

//       // 메시지 타입에 따라 재생
//       if (res.data.type === 'v') {
//         playVideoMessage(res.data.url);
//       } else if (res.data.type === 'a') {
//         playAudioMessage(res.data.url);
//       }
//     } catch (error) {
//       console.error(error);
//     }
//   };

//   useEffect(() => {
//     if (messageList.length > 0) {
//       fetchIndividualMessage(currentMessageIndex);
//     }
//   }, [messageList, currentMessageIndex]);

//   const fetchStreamingData = async (url) => {
//     try {
//       const response = await fetch(url);
//       const arrayBuffer = await response.arrayBuffer();
//       return arrayBuffer;
//     } catch (error) {
//       console.error('Error fetching streaming data:', error);
//       return null;
//     }
//   };

//   const playAudioMessage = async (audioUrl) => {
//     try {
//       const arrayBuffer = await fetchStreamingData(audioUrl);
//       if (!arrayBuffer) return;

//       const audioContext = new AudioContext();
//       const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
//       const source = audioContext.createBufferSource();
//       source.buffer = audioBuffer;
//       source.connect(audioContext.destination);
//       source.start();
//     } catch (error) {
//       console.error('Error playing audio message:', error);
//     }
//   };

//   const playVideoMessage = async (videoUrl) => {
//     try {
//       const arrayBuffer = await fetchStreamingData(videoUrl);
//       if (!arrayBuffer) return;

//       const video = document.getElementById('video-player');
//       const blob = new Blob([arrayBuffer], { type: 'video/mp4' });
//       const videoObjectUrl = URL.createObjectURL(blob);

//       video.src = videoObjectUrl;
//       video.controls = true;
//       video.autoplay = true;
//     } catch (error) {
//       console.error('Error playing video message:', error);
//     }
//   };

//   const handlePrevMessage = () => {
//     if (currentMessageIndex > 0) {
//       setCurrentMessageIndex(currentMessageIndex - 1);
//     }
//   };

//   const handleNextMessage = () => {
//     if (currentMessageIndex < messageList.length - 1) {
//       setCurrentMessageIndex(currentMessageIndex + 1);
//     }
//   };

//   let messageType = '';
//   if (messageList[currentMessageIndex]) {
//     if (messageList[currentMessageIndex].type === 'v') {
//       messageType = '영상';
//     } else if (messageList[currentMessageIndex].type === 'a') {
//       messageType = '음성';
//     }
//   }

//   return (
//     <div className="video-message-container">
//       <div className="message-content">
//         {currentMessage ? (
//           <div className="message">
//             <p>{messageList[currentMessageIndex].sendUserEmail}님의 {messageType}메세지</p>
//             {currentMessage.type === 'v' ? (
//               <video src="/video/message" width="1280px" height="720px" controls></video>
//             ) : (
//               <p>{currentMessage.content}</p>
//             )}
//             <p>보낸 날짜 : {messageList[currentMessageIndex].date}</p>
//           </div>
//         ) : (
//           <p>메세지가 없습니다.</p>
//         )}
//       </div>
//       <div className="message-navigation">
//         <button onClick={handlePrevMessage} disabled={currentMessageIndex === 0}>이전 메세지</button>
//         <button onClick={handleNextMessage} disabled={currentMessageIndex === messageList.length - 1}>다음 메세지</button>
//         {currentMessage && currentMessage.type === 'v' && (
//           <button onClick={() => playVideoMessage(messageList[currentMessageIndex].url)}>영상 재생</button>
//         )}
//         {currentMessage && currentMessage.type === 'a' && (
//           <button onClick={() => playAudioMessage(messageList[currentMessageIndex].url)}>음성 재생</button>
//         )}
//       </div>
//     </div>
//   );
// }

// export default VideoMessage;


///////////////////////////////////

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VideoMessage() {
  const [messageList, setMessageList] = useState([]);
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
  const [currentMessage, setCurrentMessage] = useState(null);
  const [currentUrl, setCurrentUrl] = useState([]);
  const userEmail = 'test2@google.com'; // 사용자 이메일

  useEffect(() => { // 전체 메세지 리스트
    const fetchMessageList = async () => {
      try {
        const res = await axios.get('video', {
          params: { userEmail: userEmail },
        });
        setMessageList(res.data.response);
      } catch (error) {
        console.error(error);
      }
    };

    fetchMessageList();
  }, []);

  useEffect(() => { // 개별 메세지
    const fetchIndividualMessage = async (videoId) => {
      try {
        const res = await axios.get('video/message', {
        params: { videoId: videoId },
        responseType: 'blob',
        });
        // console.log(res.data)
        setCurrentMessage(res.data);
    
        if (res.data.type === 'v') {
          playVideoMessage(res.data);
        } else if (res.data.type === 'a') {
          playAudioMessage(res.data);
        }
      } catch (error) {
        console.error(error);
      }
    };

    if (messageList.length > 0) {
      const firstVideoId = messageList[0].videoId;
      fetchIndividualMessage(firstVideoId);
    }
  }, [messageList]);

  const fetchStreamingData = async (url) => {
    try {
      const res = await fetch(url);
      const arrayBuffer = await res.arrayBuffer();
      return arrayBuffer;
    } catch (error) {
      console.error(error);
      return null;
    }
  };

  const playAudioMessage = async (audioUrl) => {
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
  };

  const playVideoMessage = async (videoUrl) => {
    try {
      const arrayBuffer = await fetchStreamingData(videoUrl);
      if (!arrayBuffer) return;
  
      const video = document.getElementById('video-player');
      video.src = videoUrl;
      video.controls = true;
      video.autoplay = false;
      // console.log()
    } catch (error) {
      console.error(error);
    }
  };

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
  if (messageList[currentMessageIndex]) {
    if (messageList[currentMessageIndex].type === 'v') {
      messageType = '영상';
    } else if (messageList[currentMessageIndex].type === 'a') {
      messageType = '음성';
    }
  }

  return (
    <div className="video-message-container">
      <div className="message-content">
        {currentMessage ? (
          <div className="message">
            <p>{messageList[currentMessageIndex].sendUserEmail}님의 {messageType}메세지</p>
            {messageList[currentMessageIndex].type === 'v' ? (
              <video src="video/message?videoId=4" width="800px" height="400px" controls></video>
            ) : (
                <video src="video/message?videoId=4" width="800px" height="400px" controls></video>
            )}
            <p>보낸 날짜 : {messageList[currentMessageIndex].date}</p>
          </div>
        ) : (
          <p>메세지가 없습니다.</p>
        )}
      </div>
      <div className="message-navigation">
        {/* 이전 메세지 버튼 */}
        <button onClick={handlePrevMessage} disabled={currentMessageIndex === 0}>이전 메세지</button>
        {/* 다음 메세지 버튼 */}
        <button onClick={handleNextMessage} disabled={currentMessageIndex === messageList.length - 1}>다음 메세지</button>
        {/* {currentMessage && messageList[currentMessageIndex].type === 'v' && (
        <button onClick={() => playVideoMessage(currentUrl)}>영상 재생</button>
        )} */}
        {/* 음성 재생 버튼 */}
        {/* {currentMessage && messageList[currentMessageIndex].type === 'a' && (
          <button onClick={() => playAudioMessage(currentUrl)}>음성 재생</button>
        )} */}
      </div>
    </div>
  );
}

export default VideoMessage;

