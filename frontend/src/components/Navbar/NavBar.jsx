import React from "react";
import { Link } from "react-router-dom";
import "./navbar.css";

function NavBar() {
  return (
    <div className="navbar">
      <Link to="/">Home</Link>
      <Link to="/galaxy">Galaxy</Link>
      <Link to="/calendar">Agenda</Link>
      <div className="navbar-right">
        <Link to="/settings">Settings</Link>
      </div>
    </div>
  );
}

export default NavBar;
