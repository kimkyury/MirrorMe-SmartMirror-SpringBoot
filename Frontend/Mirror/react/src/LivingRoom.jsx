import React from 'react';
import FavoriteNews from './components/FavoriteNews';
import Character from './components/Character';

function LivingRoom(props) {
  return (
    <div>
      <div className="bordered">
        <FavoriteNews></FavoriteNews>
      </div>
      <div className="bordered">
        <Character></Character>
      </div>
    </div>
  );
}

export default LivingRoom;