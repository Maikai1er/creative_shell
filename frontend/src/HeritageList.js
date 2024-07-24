import React, { useState, useEffect } from 'react';
import './HeritageList.css'

function HeritageList() {
  const [heritages, setHeritages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadMoreItems();
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const loadMoreItems = () => {
    if (isLoading) return;
    setIsLoading(true);

    fetch('http://localhost:8000/load-more-heritages/')
      .then(response => response.json())
      .then(data => {
        setHeritages(prevHeritages => [...prevHeritages, ...data]);
      })
      .catch(error => console.error('Error loading more heritages:', error))
      .finally(() => {
        setIsLoading(false);
      });
  };

  const handleScroll = () => {
    const scrollPosition = window.scrollY + window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;

    if (scrollPosition >= documentHeight * 0.9) {
      loadMoreItems();
    }
  };

  return (
    <div className='heritages'>
      <h1>Disappeared Heritages</h1>
      <ul>
        {heritages.map((heritage, index) => (
            <li key={index}>
                <p>
                    Name: {heritage.name}<br />
                    Location: {heritage.location}<br />
                    Year: {heritage.year}<br />
                    Reason: {heritage.reason}<br />
                </p>
                {heritage.image_path && (
                    <img src={`/static/images/${heritage.image_path}`} alt={heritage.name}/>

                )}
            </li>
        ))}
      </ul>
    </div>
  );
}

export default HeritageList;
