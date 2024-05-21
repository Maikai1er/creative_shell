import React from 'react';

function Header() {
  return (
    <div className="flex justify-center">
      <header>
        <h1 className="text-5xl md:text-8xl">
          <span className="ml-10 md:ml-20 lg:ml-50">Creative</span>
          <br />
          <span className="mr-10 md:mr-20 lg:mr-50">Shell</span>
          <br />
          <span className="ml-10 md:ml-20 lg:ml-50">Project</span>
        </h1>
      </header>
    </div>
  );
}

export default Header;
