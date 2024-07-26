import React from 'react';
import { motion } from 'framer-motion';
import './About.css';

const About = () => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        delayChildren: 0.3,
        staggerChildren: 0.2
      }
    }
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1
    }
  };

  return (
    <motion.div
      className="about-container"
      initial="hidden"
      animate="visible"
      variants={containerVariants}
    >
      <div className="about-content">
        <motion.h2 className="about-title" variants={itemVariants}>
          ABOUT US
        </motion.h2>

        <motion.div className="about-description" variants={itemVariants}>
          <p className="about-subtitle">
            CREATIVE SHELL: An international donation standard for preservation of cultural heritage.
          </p>
          <p>
            Creative Shell is creating a mobile app that allows people to donate to cultural heritage sites on the go, simply and transparently.
          </p>
        </motion.div>

        <motion.ul className="about-list" variants={itemVariants}>
          <li>Users collect digital cultural artefacts, discover novel travel destinations, or explore the wonders of the world in a metaverse in exchange for their donation.</li>
          <li>Cultural institutions get much-needed financial support for the heritage they manage and protect, while reducing their carbon footprint or dependency on government support.</li>
          <li>Industry professionals have a structured digital library for research and education.</li>
        </motion.ul>

        <motion.p className="about-slogan" variants={itemVariants}>
          Preserve history with a tap!
        </motion.p>

        <motion.div className="about-details" variants={itemVariants}>
          <p>
            Creative Shell is an international team with an extraordinary set of skills and expertise, built over two decades, spanning across culture, education, venture, technology, and urban development. We have been a pioneer in multimedia and digital twins in culture tech since 2004.
          </p>
          <p>
            We tap into a network of professionals in 20+ industries around the world, be that 500 Fortune execs or CERN researchers, internationally acclaimed auction houses, museums and Biennales, World Bank or UNESCO professionals, fintech, blockchain, robotics or metaverse innovators, educational policy-makers and more.
          </p>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default About;