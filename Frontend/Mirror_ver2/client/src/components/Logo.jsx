import React from 'react';
import '../css/Logo.css';

function Logo(props) {
  // 위치 조정 필요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  return (
    <div className="logo-container">
      <img
        src="/Logo/MirrorMeLogo.png"
        alt="Logo"
        className="fade-image"
      />
    </div>
  );
}

export default Logo;