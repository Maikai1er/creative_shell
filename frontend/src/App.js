import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import Header from './Header';
import About from './About';
import MenuButton from './MenuButton';
import HeritageList from './HeritageList';

function App() {
    return (
        <div>
            <Header />
            <MenuButton />
            <main>
                <Routes>
                    <Route path="/" element={<><About /><HeritageList /></>} />
                    <Route path="/contacts" element={<div>Contacts Page</div>} />
                </Routes>
            </main>
        </div>
    );
}

export default App;