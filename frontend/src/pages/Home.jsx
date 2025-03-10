import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css'

function Home() {
  return (
    <div className='home-p' style={{ padding: '2rem' }}>
      <h1>Welcome to the Homepage</h1>
      <nav>
        <ul>
          <li><Link to="/statistics">Statistics</Link></li>
          <li><Link to="/public-speaking">Public Speaking</Link></li>
          <li><Link to="/business">Business</Link></li>
          <li><Link to="/psychology">Psychology</Link></li>
          <li><Link to="/test-commit">Test Commit</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
