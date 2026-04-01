import React from 'react';
import './App.css';

function App() {
  const [data, setData] = React.useState(null);

  React.useEffect(() => {
    fetch('/api/health/')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Frontend Application</h1>
        <p>Welcome to your frontend app!</p>
        {data && (
          <div>
            <p>Backend Status: {data.status}</p>
            <p>Time: {data.timestamp}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
