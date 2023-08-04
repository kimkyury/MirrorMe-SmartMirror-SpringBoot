import React, { useState } from 'react';
import { Button } from '@mui/material';

import '../css/Modals.css';

function ModalBottons(props) {
  const [isQRModalOpen, setIsQRModalOpen] = useState(false);
  const [isMessageModalOpen, setIsMessageModalOpen] = useState(false);
  const [isYoutubeModalOpen, setIsYoutubeModalOpen] = useState(false);

  const openQRModal = () => {
    setIsQRModalOpen(true);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(false);
  };

  const openMessageModal = () => {
    setIsQRModalOpen(false);
    setIsMessageModalOpen(true);
    setIsYoutubeModalOpen(false);
  };

  const openYoutubeModal = () => {
    setIsQRModalOpen(false);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(true);
  };

  const closeModal = () => {
    setIsQRModalOpen(false);
    setIsMessageModalOpen(false);
    setIsYoutubeModalOpen(false);
  };

  return (
    <div>
      <Button className="btn" onClick={openQRModal}>QR</Button>
      <Button className="btn" onClick={openMessageModal}>메세지</Button>
      <Button className="btn" onClick={openYoutubeModal}>유튜브</Button>

      {/* QR Modal */}
      {isQRModalOpen && (
        <div className="modal">
          {/* Add QR modal content here */}
          <h2>QR 모달</h2>
          <p>QR 코드를 여기에 표시합니다.</p>
          <button onClick={closeModal}>닫기</button>
        </div>
      )}

      {/* Message Modal */}
      {isMessageModalOpen && (
        <div className="modal">
          {/* Add Message modal content here */}
          <h2>메세지 모달</h2>
          <p>메세지를 여기에 표시합니다.</p>
          <button onClick={closeModal}>닫기</button>
        </div>
      )}

      {/* Youtube Modal */}
      {isYoutubeModalOpen && (
        <div className="modal">
          {/* Add Youtube modal content here */}
          <h2>유튜브 모달</h2>
          <p>유튜브 동영상을 여기에 표시합니다.</p>
          <button onClick={closeModal}>닫기</button>
        </div>
      )}
    </div>
  );
}

export default ModalBottons;
