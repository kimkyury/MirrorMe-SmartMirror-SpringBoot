import React from 'react';

function Notice(props) {
  const tts = props.tts;

  return (
    <div>
      <h1>{tts}</h1>
    </div>
  );
}

export default Notice;