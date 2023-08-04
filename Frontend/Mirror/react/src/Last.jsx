import React from 'react';

import NavBar from './NavBar';
import Emotions from './components/Emotions';


function Last(props) {
  return (
    <div className="App">
      <div>
        <NavBar></NavBar>
      </div>
      <div>
        {/* 배치 형태에 따라서 Emotions 내의 각 div들을 component화 해야할 수도 있음  */}
        <Emotions></Emotions>
      </div>
    </div>
  );
}

export default Last;