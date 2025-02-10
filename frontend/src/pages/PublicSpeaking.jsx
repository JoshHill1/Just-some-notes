import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../App.css'

function PublicSpeaking() {
  const [speakingData, setPublicSpeakingData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/public-speaking/')
      .then(res => res.json())
      .then(data => setPublicSpeakingData(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      {speakingData.length > 0 ? (
        speakingData.map((item, index) => (
          <div key={index} className='pg-card'>
            <h2>{item.header}</h2>
            <p className='sub-txt'>{item.sub_text}</p>
            <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
              {item.content}
            </pre>
            {item.image1 && (
              <img
                src={`${item.image1}`}
                alt={`Public Speaking Image 1-${index}`}
                style={{ maxWidth: '40%', maxHeight: '50vh', marginRight: '1rem', marginTop: '1rem' }}
              />
            )}
            {item.image2 && (
              <img
                src={`${item.image2}`}
                alt={`Public Speaking Image 2-${index}`}
                style={{ maxWidth: '40%', maxHeight: '50vh' }}
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

export default PublicSpeaking;
