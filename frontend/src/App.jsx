import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Statistics from './pages/Stats';
import PublicSpeaking from './pages/PublicSpeaking';
import Business from './pages/Business';
import Psychology from './pages/Psychology';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/statistics" element={<Statistics />} />
        <Route path="/public-speaking" element={<PublicSpeaking />} />
        <Route path="/business" element={<Business />} />
        <Route path="/psychology" element={<Psychology />} />
      </Routes>
    </Router>
  );
}

export default App;
