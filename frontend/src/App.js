import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainContainer from "./containers/MainContainer";
import HomePage from "./components/Home/Home";
import CalendarPage from "./components/CalendarPage/CalendarPage";
import GalaxyPage from "./components/GalaxyPage/GalaxyPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainContainer />}>
          <Route index element={<HomePage />} />
          <Route path="calendar" element={<CalendarPage />} />
          <Route path="galaxy" element={<GalaxyPage />} />
          {/* More routes can be added here */}
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
