import React from "react";
import NavBar from "../components/NavBar/NavBar";
import { Outlet } from "react-router-dom";

const MainContainer = () => {
  return (
    <div>
      <NavBar />
      <Outlet /> {/* This will render the current route's component */}
    </div>
  );
};

export default MainContainer;
