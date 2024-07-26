import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import PartnershipForm from './PartnershipForm';

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

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
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
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/partnership" onClick={openModal}>Partnership</Link></li>
                    <li><Link to="/contacts">Contact</Link></li>
                </ul>
            </div>
            {isModalOpen && <PartnershipForm onClose={closeModal} />}
        </div>
    );
}

export default MenuButton;