import React, { useState, useEffect } from 'react';
import { Button, LinearProgress } from '@mui/material';

import '../css/Modals.css';
import VideoMessage from './VideoMessage';

function ModalBottons(props) {
  const [isQRModalOpen, setIsQRModalOpen] = useState(false);
  const [isMessageModalOpen, setIsMessageModalOpen] = useState(false);
  const [isYoutubeModalOpen, setIsYoutubeModalOpen] = useState(false);
  const [isSendMessageModalOpen, setIsSendMessageModalOpen] = useState(false);
  const [readyTime, setReadyTime] = useState(3);
  const [recordingTime, setRecordingTime] = useState(15);
  const [recordingVisible, setRecordingVisible] = useState(true);
  const [isMessageSent, setIsMessageSent] = useState(false);

  const commandMessage = props.commandMessage;
  // 목록 : "YOUTUBE", "MESSAGESENDSTART", "MESSAGESENDEND", "LEFT", "RIGHT", "EXIT"
  const youtubeKey = props.youtubeKey;

  const messageReceiver = props.messageReceiver;

  useEffect(() => {
    if (commandMessage === "YOUTUBE") {
      setIsYoutubeModalOpen(true);
    } else if (commandMessage === "MESSAGESENDSTART") {
      setIsSendMessageModalOpen(true);
    } else if (commandMessage === "RIGHT") {
      setIsYoutubeModalOpen(false);
    }
    if (isSendMessageModalOpen && commandMessage === "MESSAGESENDEND") {
      setIsSendMessageModalOpen(false);
    }
  }, [commandMessage]);


  useEffect(() => {
    const blinkTimer = setInterval(() => {
      const recCircle = document.querySelector('.rec-circle');
      if (recCircle) {
        recCircle.style.transition = 'opacity 0.3s ease-in-out';
        recCircle.style.opacity = recCircle.style.opacity === '0' ? '1' : '0';
      }
    }, 1000);

    return () => clearInterval(blinkTimer);
  }, []);

  useEffect(() => {
    let readyTimer;
    if (isSendMessageModalOpen && readyTime > 0) {
      readyTimer = setInterval(() => {
        setReadyTime(prevTime => prevTime - 1);
      }, 1000);
    } else if (readyTime === 0) {
      clearInterval(readyTimer);
    }
    return () => clearInterval(readyTimer);
  }, [isSendMessageModalOpen, readyTime]);

  useEffect(() => {
    let recordingTimer;
    if (isSendMessageModalOpen && readyTime === 0 && recordingTime > 0) {
      recordingTimer = setInterval(() => {
        setRecordingTime(prevTime => {
          if (prevTime <= 0.1) {
            setRecordingVisible(false);
          }
          return prevTime - 0.1;
        });
      }, 100);
    } else if (recordingTime <= 0) {
      clearInterval(recordingTimer);
      setIsMessageSent(true); // 녹화시간이 다 되었을 때 메세지 전송 완료 표시
    }
    return () => clearInterval(recordingTimer);
  }, [isSendMessageModalOpen, readyTime, recordingTime]);

  useEffect(() => {
    if (isMessageSent) {
      const closeTimeout = setTimeout(() => {
        setIsSendMessageModalOpen(false); // 일정 시간 후 모달창 닫기
        setRecordingTime(15);
        setReadyTime(3);
      }, 3000); // 3초 후에 모달창 닫기
      return () => clearTimeout(closeTimeout);
    }
  }, [isMessageSent]);

  // const toggleQRModal = () => {
  //   if (!isSendMessageModalOpen) {
  //     setIsQRModalOpen(prevState => !prevState);
  //     setIsMessageModalOpen(false);
  //     setIsYoutubeModalOpen(false);
  //   }
  // };

  const toggleMessageModal = () => {
    if (!isSendMessageModalOpen) {
      // setIsQRModalOpen(false);
      setIsMessageModalOpen(prevState => !prevState);
      setIsYoutubeModalOpen(false);
    }
  };

  const toggleYoutubeModal = () => {
    if (!isSendMessageModalOpen) {
      // setIsQRModalOpen(false);
      setIsMessageModalOpen(false);
      setIsYoutubeModalOpen(prevState => !prevState);
    }
  };

  const toggleSendMessageModal = () => {
    // setIsQRModalOpen(false);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(false);
    setIsSendMessageModalOpen(prevState => !prevState);
    setRecordingTime(15);
    setReadyTime(3);
    setRecordingVisible(true);
    setIsMessageSent(false); // 모달이 열릴 때마다 메세지 전송 상태 초기화
  };

  return (
    <div>
      {/* <Button className="btn" onClick={toggleQRModal}>QR</Button> */}
      <Button className="btn" onClick={toggleMessageModal}>메세지</Button>
      <Button className="btn" onClick={toggleYoutubeModal}>유튜브</Button>
      <Button className="btn" onClick={toggleSendMessageModal}>영상보내기</Button>

      {/* QR Modal */}
      {/* {isQRModalOpen && (
        <div className="modal"> */}
          {/* Add QR modal content here */}
          {/* <h2>QR 모달</h2>
          <p>QR 코드를 여기에 표시합니다.</p>
        </div>
      )} */}

      {/* Message Modal */}
      {isMessageModalOpen && (
        <div className="modal">
          {/* Add Message modal content here */}
          {/* <h2>메세지 모달</h2> */}
          <VideoMessage />
        </div>
      )}

      {/* Youtube Modal */}
      {isYoutubeModalOpen && (
        <div className="modal">
          {/* Add Youtube modal content here */}
          <iframe
            width="800"
            height="400"
            src={`https://www.youtube.com/embed/${youtubeKey}?autoplay=1`}  // 유튜브 자동재생
            title="YouTube video player"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe><br />
        </div>
      )}

      {/* SendMessage Modal */}
      {isSendMessageModalOpen && (
        <div className="send">
          {isMessageSent ? (
            <div className="sendAlert">
              <h2 className="sendAlertText">{messageReceiver}님께 영상 메세지를 전송하였습니다.</h2>
            </div>
          ) : (
            <div>
              <div className="send-header">
                <h2>{messageReceiver}님께 보내는 영상메세지</h2> {/* 메세지 수신자 수정 필요 */}
                {readyTime === 0 && (
                  <div className='rec-icon'>
                    <div className="rec-circle"></div>
                    <p className="rec-text">REC</p>
                  </div>
                )}
              </div>
              <div className="send-body">
                {readyTime > 0 ? (
                  <div className="ready-times">
                    <div>
                      <div className="loader"></div>
                      <h2 className="ready">{readyTime}</h2>
                    </div>
                    <p>테두리 안에서 메세지를 녹화하세요</p>
                  </div>
                ) : (
                  <div>
                    {/* <h2>남은 녹화시간</h2> */}
                    <div className="h1-container">
                      {/* <h1>{recordingTime}</h1> */}
                    </div>
                    <LinearProgress // Progress bar
                      variant="determinate"
                      value={((15 - recordingTime) / 15) * 100}
                      style={{ backgroundColor: 'grey', borderRadius: '4px' }}
                    />
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default ModalBottons;