import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VideoMessagePlus(props) {
  const videoId = props.videoId;

  return (
    <div className="video-message-container">
      <div className="message-content">
        <video id="video-player" controls autoPlay style={{ width: '800px', height: '400px' }}>
          <source src={`video/message?videoId=${videoId}`} type="video/mp4" />
        </video>
      </div>
    </div>
  );
}

export default VideoMessagePlus;
