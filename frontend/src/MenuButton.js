import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import PartnershipForm from './PartnershipForm';
import './MenuButton.css'

function MenuButton() {
    const [isMenuVisible, setIsMenuVisible] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuVisible(!isMenuVisible);
    };

    const handleClickOutsideMenu = (event) => {
        const menu = document.querySelector('.Menu');
        const menuButton = document.querySelector('.MenuButton');

        if (menu && menuButton && !menu.contains(event.target) && !menuButton.contains(event.target)) {
            setIsMenuVisible(false);
        }
    };

    useEffect(() => {
        document.addEventListener('click', handleClickOutsideMenu);

        return () => {
            document.removeEventListener('click', handleClickOutsideMenu);
        };
    }, []);

    return (
        <div>
            <button
                className={`MenuButton ${isMenuVisible ? 'hidden' : ''}`}
                onClick={toggleMenu}
            >
                Menu
            </button>
            <div className={`Menu ${isMenuVisible ? 'active' : ''}`}>
                <ul>
                    <li><Link to='/' onClick={() => setIsMenuVisible(false)}>Home</Link></li>
                    <li><button onClick={() => { setIsModalOpen(true); setIsMenuVisible(false); }}>Partnership</button></li>
                    <li><Link to='/contacts' onClick={() => setIsMenuVisible(false)}>Contact</Link></li>
                </ul>
            </div>
            <PartnershipForm isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
        </div>
    );
}

export default MenuButton;