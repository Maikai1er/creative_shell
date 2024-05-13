import React, { useState, useEffect } from 'react';

function HeritageList() {
  const [heritages, setHeritages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    loadMoreItems(); // При загрузке компонента загрузить первые элементы
    window.addEventListener('scroll', handleScroll); // Добавляем прослушиватель события scroll
    return () => window.removeEventListener('scroll', handleScroll); // Убираем прослушиватель при размонтировании компонента
  }, []); // Пустой массив зависимостей означает, что эффект выполнится только при монтировании компонента

  const loadMoreItems = () => {
    if (isLoading) return; // Если уже загружаем данные, то не делаем новый запрос
    setIsLoading(true); // Устанавливаем флаг загрузки

    fetch('http://localhost:8000/load-more-heritages/') // Делаем запрос к вашему API
      .then(response => response.json())
      .then(data => {
        setHeritages(prevHeritages => [...prevHeritages, ...data]); // Обновляем state с полученными данными
      })
      .catch(error => console.error('Error loading more heritages:', error))
      .finally(() => {
        setIsLoading(false); // Сбрасываем флаг загрузки
      });
  };

  const handleScroll = () => {
    const scrollPosition = window.scrollY + window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;

    if (scrollPosition >= documentHeight * 0.9) {
      loadMoreItems(); // Загружаем дополнительные элементы при прокрутке страницы до 90% от общей высоты
    }
  };

  return (
    <div>
      <h1>Heritages</h1>
      <ul>
        {heritages.map((heritage, index) => (
            <li key={index}>
                <p>Name: {heritage.name}</p>
                <p>Location: {heritage.location}</p>
                <p>Year WHS: {heritage.year_whs}</p>
                <p>Year Endangered: {heritage.year_endangered}</p>
                <img src="/static/website-stopper.jpg" alt="Heritage"/>
            </li>
        ))}
      </ul>
        {isLoading ? (
            <p>Loading...</p>
      ) : null}
    </div>
  );
}

export default HeritageList;