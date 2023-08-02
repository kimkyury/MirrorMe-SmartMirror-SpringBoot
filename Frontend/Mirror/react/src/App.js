// App.js
import logo from './logo.svg';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import React from 'react';
import './App.css';

// import SocketTest from './SocketTest';

import First from './First';
import Second from './Second';
import Last from './Last';

function App() {
  return (
    <Router>
      <div>
        {/* 모션제어 연결 후 변경 예정 */}
        <header>
          공통으로 들어갈 점 세개
          {/* <SocketTest></SocketTest> */}
        </header>
        <nav>
          <ul>
            <li><Link to="/">First</Link></li>
            <li><Link to="/second">Second</Link></li>
            <li><Link to="/last">Last</Link></li>
          </ul>
        </nav>
        <main>
          <Routes>
            <Route path="/" element={<First />} />
            <Route path="/second" element={<Second />} />
            <Route path="/last" element={<Last />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
