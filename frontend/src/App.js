import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false); // New state for loading

  const analyzeText = async () => {
    if (!text.trim()) return; // Prevent empty submissions
    setLoading(true); // Set loading to true
    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error('Error analyzing text:', error);
    } finally {
      setLoading(false); // Set loading to false after the request
      setText(''); // Clear the input field
    }
  };

  return (
    <div className="App">
      <h1>Healthy Planet Configurator</h1>
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          value={text}
          placeholder="Enter text to analyze..."
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              analyzeText();
            }
          }}
        />
        <button onClick={analyzeText} disabled={loading}>
          {loading ? 'Loading...' : 'Analyze'}
        </button>
      </div>

      {data && (
        <table>
          <thead>
            <tr>
              <th>Input</th>
              <th>ID</th>
              <th>Property</th>
              <th>Operator</th>
              <th>Selector</th>
              <th>Selector Description</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(data).map(([key, value]) => (
              <tr key={key}>
                <td>{value[0]}</td>
                <td>{value[1]}</td>
                <td>{value[2]}</td>
                <td>{value[3]}</td>
                <td>{value[4]}</td>
                <td>{value[5]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
