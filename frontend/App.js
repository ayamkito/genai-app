import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  const analyzeText = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError(null); // Clear previous errors
    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      if (!response.ok) {
        throw new Error('Failed to analyze text');
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <input
        type="text"
        value={text}
        placeholder="Enter text to analyze..."
        aria-label="Text to analyze"
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            analyzeText();
          }
        }}
      />
      <button onClick={analyzeText} disabled={loading || !text.trim()}>
        {loading ? <span className="spinner"></span> : 'Analyze'}
      </button>
      {error && <div className="error">{error}</div>}
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}

export default App;
