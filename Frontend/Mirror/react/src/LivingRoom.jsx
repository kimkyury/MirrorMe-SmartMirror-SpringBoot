import React from 'react';
import './LivingRoom.css'

const LivingRoom = ({ onClose }) => {
  return (
    <div className="modal-overlay">
      <div className="living-room-modal">
        <h3>Welcome to the Living Room</h3>
        <p>Some content here...</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default LivingRoom;