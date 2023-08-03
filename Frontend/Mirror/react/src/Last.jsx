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
        <Emotions></Emotions>
      </div>
    </div>
  );
}

export default Last;