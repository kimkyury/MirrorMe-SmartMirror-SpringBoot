// App.js
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import './App.css';

// import SocketTest from './SocketTest';

import First from './First';
import Second from './Second';
import Last from './Last';

import VideoMessage from './VideoMessage';

function App() {
  // socket 통신으로 데이터를 받아온 뒤 특정 모션에 해당하는 값을 이용하여 영상 송출 예정
  const [isVideoMessageVisible, setVideoMessageVisible] = useState(false);

  // 모달 열기 함수
  const openVideoModal = () => {
    setVideoMessageVisible(true);
  };

  // 모달 닫기 함수
  const closeVideoModal = () => {
    setVideoMessageVisible(false);
  };

  return (
    <div>
      <Router>
        <div>
          {/* 모션제어 연결 후 변경 예정 */}
          <header>
            {/* <SocketTest></SocketTest> */}
            <h2>임시로 만든 video 버튼</h2> {/* 실제로는 메세지 도착 시 또는 특정 모션 인식으로 등장 */}
            {isVideoMessageVisible && <VideoMessage isVisible={true} onClose={closeVideoModal} />}
            <button onClick={openVideoModal}>Open Video Modal</button>
          </header>
          <main>
            <Routes>
              div
              <Route path="/" element={<First />} />
              <Route path="/second" element={<Second />} />
              <Route path="/last" element={<Last />} />
            </Routes>
          </main>
        </div>
      </Router>
    </div>
  );
}

export default App;
