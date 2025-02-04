// frontend/src/Page1.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function Page1() {
  const [pageData, setPageData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/page1/')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((data) => setPageData(data))
      .catch((error) => console.error("Error fetching API:", error));
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
              alt="Page 1 Image 1"
              style={{ maxWidth: '300px', marginRight: '1rem' }}
            />
          )}
          {pageData.image2 && (
            <img
              src={`http://127.0.0.1:8000${pageData.image2}`}
              alt="Page 1 Image 2"
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

export default Page1;
