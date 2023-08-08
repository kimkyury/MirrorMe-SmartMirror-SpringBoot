// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// function VideoMessage() {
//   const [messageList, setMessageList] = useState([]);
//   const [currentMessageIndex, setCurrentMessageIndex] = useState(0);
//   const [currentMessage, setCurrentMessage] = useState(null);
//   const userEmail = 'test2@google.com'; // 사용자 이메일

//   useEffect(() => {
//     // 전체 메세지 리스트 받아오는 함수
//     const fetchMessageList = async () => {
//       try {
//         const res = await axios.get('video', {
//           params: { userEmail: userEmail },
//         });
//         setMessageList(res.data.response); // 전체 메세지 리스트 업데이트
//       } catch (error) {
//         console.error(error);
//       }
//     };

//     fetchMessageList();
//   }, []);

//   useEffect(() => {
//     // 개별 메세지 받아오는 함수
//     const fetchIndividualMessage = async (videoId) => {
//       try {
//         const res = await axios.get('video/message', {
//           params: { videoId: videoId }
//         });
//         setCurrentMessage(res.data);
//       } catch (error) {
//         console.error(error);
//       }
//     };
    
//     if (messageList.length > 0) {
//       const firstVideoId = messageList[0].videoId; // 첫 번째 비디오의 videoId 가져오기
//       fetchIndividualMessage(firstVideoId);
//     }
//   }, [messageList]);

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

//   const fetchStreamingData = async (videoId) => {
//     try {
//       const response = await fetch(`video/message?videoId=${videoId}`);
//       const arrayBuffer = await response.arrayBuffer();
//       return arrayBuffer;
//     } catch (error) {
//       console.error('Error fetching streaming data:', error);
//       return null;
//     }
//   };

//   const playAudioMessage = async (videoId) => {
//     try {
//       const arrayBuffer = await fetchStreamingData(videoId);
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

//   const playVideoMessage = async () => {
//     try {
//       const response = await fetch(`/video/message?videoId=${messageList[currentMessageIndex].videoId}`);
//       const reader = response.body.getReader();

//       const readableStream = new ReadableStream({
//         start(controller) {
//           function push() {
//             reader.read().then(({ done, value }) => {
//               if (done) {
//                 controller.close();
//                 return;
//               }
//               controller.enqueue(value);
//               push();
//             });
//           }

//           push();
//         }
//       });

//       const video = document.getElementById('video-player');
//       const mediaSource = new MediaSource();
//       video.src = URL.createObjectURL(mediaSource);

//       const sourceBuffer = mediaSource.addSourceBuffer('video/mp4; codecs="avc1.42E01E, mp4a.40.2"');

//       readableStream.pipeTo(sourceBuffer.writable, { preventClose: true });
//     } catch (error) {
//       console.error('Error fetching or playing video:', error);
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
//               <video id="video-player" controls autoPlay>
//               </video>
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
//           <button onClick={playVideoMessage}>영상 재생</button>
//         )}
//         {currentMessage && currentMessage.type === 'a' && (
//           <button onClick={() => playAudioMessage(messageList[currentMessageIndex].videoId)}>음성 재생</button>
//         )}
//       </div>
//     </div>
//   );
// }

// export default VideoMessage;

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
        setCurrentMessage(res.data);
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

  const fetchStreamingData = async (videoId) => {
    try {
      const response = await fetch(`video/message?videoId=${videoId}`);
      const arrayBuffer = await response.arrayBuffer();
      return arrayBuffer;
    } catch (error) {
      console.error(error);
      return null;
    }
  };

  const playAudioMessage = async (videoId) => {
    try {
      const arrayBuffer = await fetchStreamingData(videoId);
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

  const playVideoMessage = async () => {
    try {
      const res = await fetch(`/video/message?videoId=${messageList[currentMessageIndex].videoId}`);
      const reader = res.body.getReader();

      console.log(res)

      const readableStream = new ReadableStream({
        start(controller) {
          function push() {
            reader.read().then(({ done, value }) => {
              if (done) {
                controller.close();
                return;
              }
              controller.enqueue(value);
              push();
            });
          }

          push();
        }
      });

      const video = document.getElementById('video-player');
      const mediaSource = new MediaSource();
      video.src = URL.createObjectURL(mediaSource);

      const sourceBuffer = mediaSource.addSourceBuffer('video/mp4; codecs="avc1.42E01E, mp4a.40.2"');

      readableStream.pipeTo(sourceBuffer.writable, { preventClose: true });
    } catch (error) {
      console.error('Error fetching or playing video:', error);
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
            {currentMessage.type === 'v' ? (
              <video id="video-player" controls autoPlay>
              </video>
            ) : (
              <p>{currentMessage.content}</p>
            )}
            <p>보낸 날짜 : {messageList[currentMessageIndex].date}</p>
          </div>
        ) : (
          <p>메세지가 없습니다.</p>
        )}
      </div>
      <div className="message-navigation">
        <button onClick={handlePrevMessage} disabled={currentMessageIndex === 0}>이전 메세지</button>
        <button onClick={handleNextMessage} disabled={currentMessageIndex === messageList.length - 1}>다음 메세지</button>
        {currentMessage && currentMessage.type === 'v' && (
          <button onClick={playVideoMessage}>영상 재생</button>
        )}
        {currentMessage && currentMessage.type === 'a' && (
          <button onClick={() => playAudioMessage(messageList[currentMessageIndex].videoId)}>음성 재생</button>
        )}
      </div>
    </div>
  );
}

export default VideoMessage;
