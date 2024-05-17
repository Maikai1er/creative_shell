import React from 'react';

function About() {
  return (
    <div className="bg-orange-custom text-white text-lg md:text-xl lg:text-2xl p-6">
      <div className="p-6">
        <h2 className="font-bold mb-4">ABOUT US</h2>
        <p className="mb-4">
          CREATIVE SHELL: An international donation standard for preservation of cultural heritage.
        </p>
        <p className="mb-4">
          Creative Shell is creating a mobile app that allows people to donate to cultural heritage sites on the go, simply and transparently.
        </p>
        <ul className="list-disc ml-6 mb-4">
          <li>Users collect digital cultural artefacts, discover novel travel destinations, or explore the wonders of the world in a metaverse in exchange for their donation.</li>
          <li>Cultural institutions get much-needed financial support for the heritage they manage and protect, while reducing their carbon footprint or dependency on government support.</li>
          <li>Industry professionals have a structured digital library for research and education.</li>
        </ul>
        <p className="mb-4">Preserve history with a tap!</p>
      </div>
      <div className="p-6">
        <p className="mb-4">
          Creative Shell is an international team with an extraordinary set of skills and expertise, built over two decades, spanning across culture, education, venture, technology, and urban development. We have been a pioneer in multimedia and digital twins in culture tech since 2004.
        </p>
        <p className="mt-4">
          We tap into a network of professionals in 20+ industries around the world, be that 500 Fortune execs or CERN researchers, internationally acclaimed auction houses, museums and Biennales, World Bank or UNESCO professionals, fintech, blockchain, robotics or metaverse innovators, educational policy-makers and more.
        </p>
      </div>
    </div>
  );
}

export default About;
