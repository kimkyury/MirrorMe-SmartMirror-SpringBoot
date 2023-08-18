import React from 'react';
import '../css/Logo.css';

function Logo(props) {
  // 위치 조정 필요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  // -> 조정은 완료 but 실제 거울 보면서 추가 조정 필요할수도?
  return (
    <div className="logo-container">
      <img
        src={`${process.env.PUBLIC_URL}/images/Logo/MirrorMeLogo.PNG`}
        alt="Logo"
        className="fade-image"
      />
    </div>
  );
}

export default Logo;