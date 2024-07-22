import { motion } from 'framer-motion';
import React, { useEffect, useState } from 'react';

function Header() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const variantsLeft = {
    hidden: { opacity: 0, x: -200 },
    visible: { opacity: 2, x: 0, transition: { duration: 0.4 } },
  };

  const variantsRight = {
    hidden: { opacity: 0, x: 200 },
    visible: { opacity: 2, x: 0, transition: { duration: 0.4 } },
  };

  return (
    <div className="flex justify-center items-center">
      <header>
        <h1 className="text-5xl md:text-8xl text-center">
          <motion.span
            className="block ml-10 md:ml-20 lg:ml-50"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsLeft}
          >
            Creative
          </motion.span>
          <motion.span
            className="block mr-10 md:mr-20 lg:mr-50"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsRight}
          >
            Shell
          </motion.span>
          <motion.span
            className="block ml-10 md:ml-20 lg:ml-50"
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={variantsLeft}
          >
            Project
          </motion.span>
        </h1>
      </header>
    </div>
  );
}

export default Header;
