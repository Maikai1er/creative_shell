import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import './Header.css';

function Header() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const variantsLeft = {
    hidden: { opacity: 0, x: -100 },
    visible: { opacity: 1, x: 0, transition: { duration: 0.6, ease: "easeOut" } },
  };

  const variantsRight = {
    hidden: { opacity: 0, x: 100 },
    visible: { opacity: 1, x: 0, transition: { duration: 0.6, ease: "easeOut" } },
  };

  return (
    <header className="header">
      <div className="header-content">
        <h1 className="header-title">
          <motion.span
            className="header-word creative"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsLeft}
          >
            Creative
          </motion.span>
          <motion.span
            className="header-word shell"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsRight}
          >
            Shell
          </motion.span>
          <motion.span
            className="header-word project"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsLeft}
          >
            Project
          </motion.span>
        </h1>
      </div>
    </header>
  );
}

export default Header;