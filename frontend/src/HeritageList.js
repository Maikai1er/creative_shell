import React, { useState, useEffect } from 'react';
import './HeritageList.css';

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
    <div className="heritages">
      <h1>Исчезнувшее культурное наследие</h1>
      <ul>
        {heritages.map((heritage, index) => (
          <li key={index} className="heritage-item">
            <div className="heritage-card">
              <div className="heritage-info">
                <h2>{heritage.name}</h2>
                <span className="heritage-year">{heritage.year}</span>
                <p><strong>Местоположение:</strong> {heritage.location}</p>
                <p><strong>Причина:</strong> {heritage.reason}</p>
              </div>
              {heritage.image_path && (
                <div className="heritage-image">
                  <img src={`/static/images/${heritage.image_path}`} alt={heritage.name} />
                </div>
              )}
            </div>
          </li>
        ))}
      </ul>
      {isLoading && <p className="loading-message">Загрузка дополнительных объектов...</p>}
    </div>
  );
};

export default HeritageList;
