import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function PublicSpeaking() {
  const [pageData, setPageData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/public-speaking/')
      .then(res => res.json())
      .then(data => setPageData(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      {pageData ? (
        <>
                    <h2>{pageData.header}</h2>
          <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
            {pageData.content}
          </pre>
          {pageData.image1 && (
            <img
              src={`http://127.0.0.1:8000${pageData.image1}`}
              alt="Public Speaking Image 1"
              style={{ maxWidth: '300px', marginRight: '1rem' }}
            />
          )}
          {pageData.image2 && (
            <img
              src={`http://127.0.0.1:8000${pageData.image2}`}
              alt="Public Speaking Image 2"
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

export default PublicSpeaking;
