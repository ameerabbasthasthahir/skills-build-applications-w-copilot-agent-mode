import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [entries, setEntries] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setEntries(results);
        console.log('Fetched leaderboard:', results);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {entries.map((entry, idx) => (
          <li key={entry.id || idx}>{entry.user?.name || entry.user} - Score: {entry.score} (Rank: {entry.rank})</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
