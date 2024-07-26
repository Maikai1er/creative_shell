import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import './Header.css';

function Header() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const variants = {
    hidden: { opacity: 0, y: -20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: "easeOut" } },
  };

  return (
    <header className="header">
      <div className="header-content">
        <motion.h1
          className="header-title"
          initial="hidden"
          animate={isVisible ? 'visible' : 'hidden'}
          variants={variants}
        >
          <span className="header-word">Creative</span>
          <span className="header-word">Shell</span>
          <span className="header-word">Project</span>
        </motion.h1>
      </div>
    </header>
  );
}

export default Header;