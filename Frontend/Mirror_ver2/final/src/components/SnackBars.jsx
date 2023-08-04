import React, { useState } from 'react';
import { Snackbar, Button } from '@mui/material';
import { CSSTransition } from 'react-transition-group';

import TodayWeather from './TodayWeather';

function Snackbars(props) {
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleButtonClick = () => {
    setOpenSnackbar(true);
  };

  const handleSnackbarClose = () => {
    setOpenSnackbar(false);
  };

  return (
    <div>
      <Button onClick={handleButtonClick} variant="contained" color="primary">날씨</Button>
      <CSSTransition
        in={openSnackbar}
        timeout={300}
        classNames="slide"
        unmountOnExit
      >
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
          open={openSnackbar}
          autoHideDuration={3000}
          onClose={handleSnackbarClose}
          message={<TodayWeather />}
          style={{ marginTop: '80px' }} // 추후 조정
        />
      </CSSTransition>
    </div>
  );
}

export default Snackbars;
