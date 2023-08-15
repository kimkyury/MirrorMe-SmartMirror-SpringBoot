import React, { useRef, useState, useEffect } from 'react';
import { Snackbar, Button } from '@mui/material';
import { CSSTransition } from 'react-transition-group';

import axios from 'axios';

import VideoMessage from './VideoMessage'
import TodayWeather from './TodayWeather';
import Tasks from './Tasks';
import Schedules from './Schedules';
import Notice from './Notice';

import '../css/Snackbars.css';

function Snackbars(props) {
  const [openVideoMessageSnackbar, setOpenVideoMessageSnackbar] = useState(false);
  const [openWeatherSnackbar, setOpenWeatherSnackbar] = useState(false);
  const [showWeekWeather, setShowWeekWeather] = useState(false);
  const [openTasksSnackbar, setOpenTasksSnackbar] = useState(false);
  const [openSchedulesSnackbar, setOpenSchedulesSnackbar] = useState(false);
  const [openNoticeSnackbar, setOpenNoticeSnackbar] = useState(false);
  const ref = useRef(null)

  
  const commandMessage = props.commandMessage;
  // 목록 : "WEATHER", "LEFT", "RIGHT","EXIT", "TTS"
  const tts = props.tts;
  const ttsType = props.ttsType;
  
  const userAccessToken = props.userAccessToken;
  const userRefreshToken = props.userRefreshToken;

  const handleSnackbarClose = () => {
    setOpenNoticeSnackbar(false);
    setOpenWeatherSnackbar(false);
    setOpenSchedulesSnackbar(false);
    setOpenTasksSnackbar(false);
    setShowWeekWeather(false);
  };


  useEffect(() => {
    if (commandMessage === "WEATHER") {
      setOpenWeatherSnackbar(true);
    } else if (commandMessage === "EXIT") {
      handleSnackbarClose();
    }

    // 날씨화면이 나와있는 상태에서 주간날씨 화면 보여주기
    if (openWeatherSnackbar) {
      if (!showWeekWeather && commandMessage === "LEFT") {
        setShowWeekWeather(true);
      }
      if (showWeekWeather && commandMessage === "RIGHT") {
        setShowWeekWeather(false);
      }
    }
  }, [commandMessage]);

  // const handleVideoMessage = () => {
  //   if (commandMessage == "MESSAGESHOW") {
  //     setopenNoticeSnackbar(true);
  //     setOpenVideoMessageSnackbar(true);
  //   }
  // }

  // const handleWeather = () => {
  //   if (commandMessage == "WEATHER") {
  //     setopenNoticeSnackbar(true);
  //     setOpenWeatherSnackbar(true);
  //   }
  // };

  const handleTasks = () => {
    setOpenTasksSnackbar(true);
  };

  const handleSchedules = () => {
    setOpenSchedulesSnackbar(true);
  };

  const handleWeatherButtonClick = () => {

    setOpenWeatherSnackbar(true)
  }

  // const handleWeekWeatherClick = () => {
  //   setOpenNoticeSnackbar(true);
  //   setShowWeekWeather(true);
  // };


  return (
    <div>
      {/* <Button onClick={handleVideoMessageButtonClick} variant="contained" color="inherit">메세지</Button> */}
      <Button onClick={handleWeatherButtonClick} variant="contained" color="inherit">날씨</Button>
      <Button onClick={handleTasks} variant="contained" color="inherit">할일</Button>
      <Button onClick={handleSchedules} variant="contained"  color="inherit">일정</Button>
      
      {/* Notice Snackbar */}
      {/* <div className="notice">
        <CSSTransition
          in={openNoticeSnackbar}
          timeout={300}
          classNames="slide"
          unmountOnExit
        >
          <Snackbar
            anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
            open={openNoticeSnackbar}
            autoHideDuration={10000}
            onClose={handleSnackbarClose}
            message=
            {<Notice 
              tts={tts}
            />}
            style={{ marginTop: '200px' }}
          />
        </CSSTransition>
      </div> */}

      <div className="snackbar">
        {/* VideoMessage Snackbar */}
        {/* <CSSTransition
          in={openVideoMessageSnackbar}
          timeout={300}
          classNames="slide"
          unmountOnExit
          nodeRef={ref}
        >
          <Snackbar
            anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
            open={openVideoMessageSnackbar}
            autoHideDuration={10000}
            onClose={handleSnackbarClose}
            message={<VideoMessage 
                      userEmail={userEmail}
                      />}
            style={{ marginTop: '200px' }}
          />
        </CSSTransition> */}

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
            onClose={handleSnackbarClose}
            message={
              <div>
                <TodayWeather
                  showWeekWeather={showWeekWeather}
                />
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
            onClose={handleSnackbarClose}
            message=
            {<Tasks 
              userAccessToken={userAccessToken}
              userRefreshToken={userRefreshToken}
            />}
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
            onClose={handleSnackbarClose}
            message=
              {<Schedules 
                userAccessToken={userAccessToken}
                userRefreshToken={userRefreshToken}
              />}
            style={{ marginTop: '200px' }}
          />
        </CSSTransition>
      </div>
    </div>
  );
}

export default Snackbars;
