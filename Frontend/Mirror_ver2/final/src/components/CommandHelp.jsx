import React, { useState, useEffect } from 'react';

function CommandHelp(props) {
    const [commandList, setCommandList] = useState([
        '유튜브', '메세지', '날씨', '일정', '할 일',
    ])
  return (
    <div className="command-help-parent-container">
      <div className="command-help-container">
        <h4>CommandList</h4>
        <ul className="command-list">
          {commandList.map((command, index) => (
            <li key={index}>{command}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default CommandHelp;