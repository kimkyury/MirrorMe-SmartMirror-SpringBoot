import React, { useState } from 'react';
import { Snackbar, Button } from '@mui/material';
import { CSSTransition } from 'react-transition-group';

import VideoMessage from './VideoMessage'
import TodayWeather from './TodayWeather';
import WeekWeather from './WeekWeather';
import Tasks from './Tasks';
import Schedules from './Schedules';

function Snackbars(props) {
  const [openVideoMessageSnackbar, setOpenVideoMessageSnackbar] = useState(false)
  const [openWeatherSnackbar, setOpenWeatherSnackbar] = useState(false);
  const [showWeekWeather, setShowWeekWeather] = useState(false);
  const [openTasksSnackbar, setOpenTasksSnackbar] = useState(false);
  const [openSchedulesSnackbar, setOpenSchedulesSnackbar] = useState(false);

  const handleVideoMessageButtonClick = () => {
    setOpenVideoMessageSnackbar(!openVideoMessageSnackbar);
  }

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
    setOpenVideoMessageSnackbar(false);
    setOpenWeatherSnackbar(false);
    setOpenSchedulesSnackbar(false);
    setOpenTasksSnackbar(false);
    setShowWeekWeather(false);
  };

  return (
    <div>
      <Button onClick={handleVideoMessageButtonClick} variant="contained" color="inherit">메세지</Button>
      <Button onClick={handleWeatherButtonClick} variant="contained" color="inherit">날씨</Button>
      <Button onClick={handleTasksButtonClick} variant="contained" color="inherit">할일</Button>
      <Button onClick={handleSchedulesButtonClick} variant="contained"  color="inherit">일정</Button>

      {/* VideoMessage Snackbar */}
      <CSSTransition
        in={openVideoMessageSnackbar}
        timeout={300}
        classNames="slide"
        unmountOnExit
      >
        <Snackbar
          anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
          open={openVideoMessageSnackbar}
          autoHideDuration={10000}
          onClose={handleVideoMessageButtonClick}
          message={<VideoMessage />}
          style={{ marginTop: '200px' }}
        />
      </CSSTransition>

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
