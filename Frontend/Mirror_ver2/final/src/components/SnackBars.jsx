import React, { useState } from 'react';
import { Snackbar, Button } from '@mui/material';
import { CSSTransition } from 'react-transition-group';

import TodayWeather from './TodayWeather';
import WeekWeather from './WeekWeather';
import Tasks from './Tasks';
import Schedules from './Schedules';

function Snackbars(props) {
  const [openWeatherSnackbar, setOpenWeatherSnackbar] = useState(false);
  const [openTasksSnackbar, setOpenTasksSnackbar] = useState(false);
  const [openSchedulesSnackbar, setOpenSchedulesSnackbar] = useState(false);
  const [showWeekWeather, setShowWeekWeather] = useState(false);

  const handleWeatherButtonClick = () => {
    setOpenWeatherSnackbar(!openWeatherSnackbar);
  };

  const handleTasksButtonClick = () => {
    setOpenTasksSnackbar(!openTasksSnackbar);
  };

  const handleSchedulesButtonClick = () => {
    setOpenSchedulesSnackbar(!openSchedulesSnackbar);
  };

  const handleWeekWeatherClick = () => {
    setShowWeekWeather(true);
  };

  const handleSnackbarClose = () => {
    setOpenWeatherSnackbar(false);
    setOpenSchedulesSnackbar(false);
    setOpenTasksSnackbar(false);
    setShowWeekWeather(false);
  };

  return (
    <div>
      <Button onClick={handleWeatherButtonClick} variant="contained" color="inherit">날씨</Button>
      <Button onClick={handleTasksButtonClick} variant="contained" color="inherit">할일</Button>
      <Button onClick={handleSchedulesButtonClick} variant="contained"  color="inherit">일정</Button>

      {/* Weather Snackbar */}
      <CSSTransition
        in={openWeatherSnackbar}
        timeout={300}
        classNames="slide"
        unmountOnExit
      >
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
          open={openWeatherSnackbar}
          autoHideDuration={10000}
          onClose={handleWeatherButtonClick}
          message={
            <div>
              <TodayWeather />
              {showWeekWeather && <WeekWeather />}
              {showWeekWeather ? null : (
                <Button onClick={handleWeekWeatherClick} variant="contained" color="primary">
                  더 보기
                </Button>
              )}
            </div>
          }
          style={{ marginTop: '200px' }}
        />
      </CSSTransition>

      {/* Tasks Snackbar */}
      <CSSTransition
        in={openTasksSnackbar}
        timeout={300}
        classNames="slide"
        unmountOnExit
      >
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
          open={openTasksSnackbar}
          autoHideDuration={10000}
          onClose={handleTasksButtonClick}
          message={<Tasks />}
          style={{ marginTop: '200px' }}
        />
      </CSSTransition>

      {/* Schedules Snackbar */}
      <CSSTransition
        in={openSchedulesSnackbar}
        timeout={300}
        classNames="slide"
        unmountOnExit
      >
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
          open={openSchedulesSnackbar}
          autoHideDuration={10000}
          onClose={handleSchedulesButtonClick}
          message={<Schedules />}
          style={{ marginTop: '200px' }}
        />
      </CSSTransition>
    </div>
  );
}

export default Snackbars;
