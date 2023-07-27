import React from 'react';
import { useState } from 'react';


function FavoriteNews(props) {
  const [news, setNews] = useState([
    '관심 뉴스 1',
    '관심 뉴스 2',
    '관심 뉴스 3',
  ]);
  return (
    <div>
      <h3>관심 뉴스</h3>
      { news.map((item, index) => {
        return <li>{ item }</li>
      })}
    </div>
  );
}

export default FavoriteNews;