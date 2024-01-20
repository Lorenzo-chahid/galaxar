import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CalendarPage from "./components/CalendarPage";
import GalaxyPage from "./components/GalaxyPage"; // Assurez-vous que ce composant existe

function App() {
  return (
    <Router>
      <div className="App">
        {/* Inclure NavBar ici si elle doit être présente sur toutes les pages */}
        <Routes>
          <Route path="/" element={<CalendarPage />} />
          <Route path="/galaxy" element={<GalaxyPage />} />
          {/* Vous pouvez ajouter plus de routes ici */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
