import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function ToDoList(props) {
  const [schedule, setSchedule] = useState("");

  useEffect(() => {
    const accessToken = 'ya29.a0AbVbY6Pb7osab39m486LDiX1GSXzMuJTFH3RnXeQfe_pVjZDa-kog1X7olqnE6bkm7L8oAFS-KNwSO62RtyTz2kxPn9zyvFTSt70XM0ZNfjPsDEPhYtMjYSk1H_4yvs77dpVmnVMIJNIOqKecP4hl0O_z_RdaCgYKAYwSARMSFQFWKvPlkq4dLzwToy7XMYHfccyilA0163';

    axios.get("http://192.168.30.158:8080/schedule/today", {
      params: { accessToken : accessToken },
    }).then((res) => {
      console.log(res.data);
    })
    .catch((error) => {
      console.log(error);
    });
  },[]);

  return (
    <>
      <h3>오늘의 일정</h3>
    </>
  );
}

export default ToDoList;