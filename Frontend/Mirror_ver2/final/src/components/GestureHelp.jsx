import React, { useState, useEffect } from 'react';
import '../css/GestureHelp.css';

function GestureHelp(props) {
  const [gestureList, setGestureList] = useState([
    {gesture: '왼쪽 슬라이드', action: '왼쪽으로 이동'},
    {gesture: '오른쪽 슬라이드', action: '오른쪽으로 이동'},
    {gesture: '주먹 쥐기', action: '닫기'},
  ]);
  const [commandList, setCommandList] = useState([
    '유튜브', '메세지', '날씨',
  ])
  return (
    <div className="gesture-help-parent-container">
      <div className="gesture-help-container">
        <h4>CommandList</h4>
        <ul className="gesture-list">
          {gestureList.map((gesture, index) => (
            <li key={index}>{gesture.gesture} : {gesture.action}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default GestureHelp;