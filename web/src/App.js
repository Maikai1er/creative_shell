import React from 'react';
import Header from './Header';
import HeritageList from './HeritageList';
import About from "./About";

function App() {
  return (
    <div>
        <Header />
        <main>
            <About />
            <HeritageList />
        </main>
    </div>
  );
}

export default App;
