import React from 'react';

function CurrentDate(props) {
  const now = new Date();
  
  const year = now.getFullYear();
  const month = now.getMonth() + 1;
  const date = now.getDate();
  const week = ['일', '월', '화', '수', '목', '금', '토'];
  const dayOfWeek = week[now.getDay()]

  const hour = now.getHours();
  const hour24 = hour > 12 ? hour - 12  : hour
  const minute = now.getMinutes();

  const ampm = hour >= 12 ? 'PM' : 'AM';

  return (
    <div>
      <p>
        { year }년 { month }월 { date }일 { dayOfWeek }요일
      </p>
      <p>
        { ampm } { hour24 } : { minute }
      </p>
    </div>
  );
}

export default CurrentDate;