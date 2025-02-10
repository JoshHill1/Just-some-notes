import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../App.css'

function Statistics() {
  const [stats, setStats] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/statistics/')
      .then(res => res.json())
      .then(data => setStats(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div className='pg-content'>
      {stats.length > 0 ? (
        stats.map((item, index) => (
          <div key={index} className='pg-card'>
            <h2>{item.header}</h2>
            <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
              {item.content}
            </pre>
            {item.image1 && (
              <img
                src={`http://127.0.0.1:8000${item.image1}`}
                alt={`Statistics Image 1-${index}`}
                style={{ maxWidth: '300px', marginRight: '1rem' }}
              />
            )}
            {item.image2 && (
              <img
                src={`http://127.0.0.1:8000${item.image2}`}
                alt={`Statistics Image 2-${index}`}
                style={{ maxWidth: '300px' }}
              />
            )}
          </div>
        ))
      ) : (
        <p>Loading...</p>
      )}
      <br />
      <Link to="/">Back to Home</Link>
    </div>
  );
}

export default Statistics;
