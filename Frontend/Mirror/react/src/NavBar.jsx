import React from 'react';
import './css/NavBar.css';

import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';

function NavBar(props) {
  return (
    <div className="nav-bar">
      <div className="first"><NavLink to="/" activeClassName="active-link">First</NavLink></div>
      <div className="second"><NavLink to="/second" activeClassName="active-link">Second</NavLink></div>
      <div className="last"><NavLink to="/last" activeClassName="active-link">Last</NavLink></div>
    </div>
  );
}

export default NavBar;