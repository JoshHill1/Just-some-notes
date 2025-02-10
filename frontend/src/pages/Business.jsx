import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../App.css'

function Business() {
  const [businessData, setBusinessData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/business/')
      .then(res => res.json())
      .then(data => setBusinessData(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div className='pg-content'>
      {businessData.length > 0 ? (
        businessData.map((item, index) => (
          <div key={index} className='pg-card'>
            <h2>{item.header}</h2>
            <p className='sub-txt'>{item.sub_text}</p>
            <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
              {item.content}
            </pre>
            {item.image1 && (
              <img
                src={`${item.image1}`}
                alt={`Business Image 1-${index}`}
                style={{ maxWidth: '40%', maxHeight: '50vh', marginRight: '1rem', marginTop: '1rem' }}
              />
            )}
            {item.image2 && (
              <img
                src={`${item.image2}`}
                alt={`Business Image 2-${index}`}
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

export default Business;
