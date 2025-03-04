import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../App.css'

function TestCommit() {
  const [test_commitData, setTestCommitData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/test-commit/')
      .then(res => res.json())
      .then(data => setTestCommitData(data))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      {test_commitData.length > 0 ? (
        test_commitData.map((item, index) => (
          <div key={index} className='pg-card'>
            <h2>{item.header}</h2>
            <p className='sub-txt'>{item.anything}</p>
            <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
              {item.content}
            </pre>
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

export default TestCommit;
