import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function Psychology() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/psychology/')
      .then((res) => res.json())
      .then((json) => setData(json))
      .catch((err) => console.error('Error fetching API:', err));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Psychology</h2>
      <p>{data ? data.message : "Loading..."}</p>
      <Link to="/">Back to Home</Link>
    </div>
  );
}

export default Psychology;
