import logo from './logo.svg';
import './App.css';

import Weather from './components/Weather'
import CurrentDate from './components/CurrentDate'

function App() {
  return (
    <div>
      <Weather></Weather>
      <CurrentDate></CurrentDate>
    </div>
  );
}

export default App;
