jsx
// App.js
import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0); // initial count = 0

  const handleClick = () => {
    setCount(count + 1); // increment count
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h2>React Button Click Counter</h2>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Click Me!</button>
    </div>
  );
}

export default App;

