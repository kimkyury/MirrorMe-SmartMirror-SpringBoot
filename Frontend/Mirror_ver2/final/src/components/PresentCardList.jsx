import React, { useState, useEffect } from 'react';
import PresentCard from './PresentCard';

function PresentCardList(props) {
  const [presentList, setPresentList] = useState([
    { name: 'Perfume', image: '' },
    { name: 'Necklace', image: '' },
    { name: 'Chicken', image: '' },
    { name: 'IcecreamCake', image: '' },
    { name: 'Money', image: '' },
  ]);

  const [randomPresentList, setRandomPresentList] = useState([]);

  useEffect(() => {
    const getRandomIndexes = () => {
      const indexes = [];
      while (indexes.length < 3) {
        const randomIndex = Math.floor(Math.random() * presentList.length);
        if (
          !indexes.includes(randomIndex) &&
          !randomPresentList.includes(randomIndex)
        ) {
          indexes.push(randomIndex);
        }
      }
      return indexes;
    };

    const indexes = getRandomIndexes();
    setRandomPresentList(indexes);
  }, [presentList]);

  return (
    <div>
      <h2 style={{ color: 'white' }}>이런 선물은 어때요?</h2>
      {randomPresentList.map((presentIndex, index) => (
        <PresentCard
          key={index}
          name={presentList[presentIndex].name}
          image={presentList[presentIndex].image}
        />
      ))}
    </div>
  );
}

export default PresentCardList;