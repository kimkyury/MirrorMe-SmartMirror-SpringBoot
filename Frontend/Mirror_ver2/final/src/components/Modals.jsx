import React, { useState } from 'react';
import { Button } from '@mui/material';

import '../css/Modals.css';
import VideoMessage from './VideoMessage';

function ModalBottons(props) {
  const [isQRModalOpen, setIsQRModalOpen] = useState(false);
  const [isMessageModalOpen, setIsMessageModalOpen] = useState(false);
  const [isYoutubeModalOpen, setIsYoutubeModalOpen] = useState(false);

  const toggleQRModal = () => {
    setIsQRModalOpen(prevState => !prevState);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(false);
  };

  const toggleMessageModal = () => {
    setIsQRModalOpen(false);
    setIsMessageModalOpen(prevState => !prevState);
    setIsYoutubeModalOpen(false);
  };

  const toggleYoutubeModal = () => {
    setIsQRModalOpen(false);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(prevState => !prevState);
  };

  return (
    <div>
      <Button className="btn" onClick={toggleQRModal}>QR</Button>
      <Button className="btn" onClick={toggleMessageModal}>메세지</Button>
      <Button className="btn" onClick={toggleYoutubeModal}>유튜브</Button>

      {/* QR Modal */}
      {isQRModalOpen && (
        <div className="modal">
          {/* Add QR modal content here */}
          <h2>QR 모달</h2>
          <p>QR 코드를 여기에 표시합니다.</p>
        </div>
      )}

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
          <h2>유튜브 모달</h2>
          <iframe
            width="800"
            height="400"
            src="https://www.youtube.com/embed/LqME1y6Mlyg"
            title="YouTube video player"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe><br />
        </div>
      )}
    </div>
  );
}

export default ModalBottons;
