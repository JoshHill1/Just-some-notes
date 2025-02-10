import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function Statistics() {
  const [pageData, setPageData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/statistics/')
      .then(res => res.json())
      .then(data => setPageData(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      {pageData ? (
        <>
          <h2>{pageData.header}</h2>
          <p>{pageData.content}</p>
          {pageData.image1 && (
            <img
              src={`http://127.0.0.1:8000${pageData.image1}`}
              alt="Statistics Image 1"
              style={{ maxWidth: '300px', marginRight: '1rem' }}
            />
          )}
          {pageData.image2 && (
            <img
              src={`http://127.0.0.1:8000${pageData.image2}`}
              alt="Statistics Image 2"
              style={{ maxWidth: '300px' }}
            />
          )}
        </>
      ) : (
        <p>Loading...</p>
      )}
      <br />
      <Link to="/">Back to Home</Link>
    </div>
  );
}

export default Statistics;
