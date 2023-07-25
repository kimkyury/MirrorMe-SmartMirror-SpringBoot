import logo from './logo.svg';
import './App.css';

// import Container from 'react-bootstrap/Container';
// import Row from 'react-bootstrap/Row';
// import Col from 'react-bootstrap/Col';

import Weather from './components/Weather';
import CurrentDate from './components/CurrentDate';
import ToDoList from './components/ToDoList';
import VideoMessage from './components/VideoMessage';
import FavoriteNews from './components/FavoriteNews';
import Character from './components/Character';

function App() {
  return (
    <div className="App">
      <Weather className="Weather"></Weather>
      <CurrentDate className="CurrentDate"></CurrentDate>
      <ToDoList></ToDoList>
      <VideoMessage></VideoMessage>
      <FavoriteNews></FavoriteNews>
      <Character></Character>
    </div>
  );
}

export default App;
