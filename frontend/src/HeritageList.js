import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import './HeritageList.css';

const HeritageItem = ({ heritage, index }) => {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.unobserve(entry.target);
        }
      },
      { threshold: 0.1 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      if (ref.current) {
        observer.unobserve(ref.current);
      }
    };
  }, []);

  const variants = {
    hidden: { opacity: 0, x: -50 },
    visible: { opacity: 1, x: 0 }
  };

  return (
    <motion.li
      ref={ref}
      className='heritage-item'
      initial='hidden'
      animate={isVisible ? 'visible' : 'hidden'}
      variants={variants}
      transition={{ duration: 0.5, delay: index * 0.1 }}
    >
      <div className='heritage-card'>
        <div className='heritage-info'>
          <h2>{heritage.name}</h2>
          <span className='heritage-year'>{heritage.year}</span>
          <p><strong>Location:</strong> {heritage.location}</p>
          <p><strong>Reason:</strong> {heritage.reason}</p>
        </div>
        {heritage.image_path && (
          <div className='heritage-image'>
            <img src={`/static/images/${heritage.image_path}`} alt={heritage.name} />
          </div>
        )}
      </div>
    </motion.li>
  );
};


function HeritageList() {
  const [heritages, setHeritages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [titleVisible, setTitleVisible] = useState(false);
  const titleRef = useRef(null);

  useEffect(() => {
    loadMoreItems();
    window.addEventListener('scroll', handleScroll);

    const titleObserver = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setTitleVisible(true);
          titleObserver.unobserve(entry.target);
        }
      },
      { threshold: 0.1 }
    );

    if (titleRef.current) {
      titleObserver.observe(titleRef.current);
    }

    return () => {
      window.removeEventListener('scroll', handleScroll);
      if (titleRef.current) {
        titleObserver.unobserve(titleRef.current);
      }
    };
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

  const titleVariants = {
    hidden: { opacity: 0, y: -50 },
    visible: { opacity: 1, y: 0 }
  };

  return (
    <div className='heritages'>
      <motion.h1
        ref={titleRef}
        initial='hidden'
        animate={titleVisible ? 'visible' : 'hidden'}
        variants={titleVariants}
        transition={{ duration: 0.5 }}
      >
        WORLD HERITAGE IN DANGER
      </motion.h1>
      <ul>
        {heritages.map((heritage, index) => (
          <HeritageItem key={index} heritage={heritage} index={index} />
        ))}
      </ul>
      {isLoading && <p className='loading-message'>Loading additional content...</p>}
    </div>
  );
}

export default HeritageList;
