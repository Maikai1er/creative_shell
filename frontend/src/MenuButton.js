import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';
import PartnershipForm from './PartnershipForm';

function MenuButton() {
    const [isMenuVisible, setIsMenuVisible] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false); // Добавляем состояние для отображения модального окна

    const toggleMenu = () => {
        setIsMenuVisible(!isMenuVisible);
    };

    const handleClickOutsideMenu = (event) => {
        const menu = document.querySelector('.menu');
        const menuButton = document.querySelector('.menu-button');

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
        <Router>
            <div className="relative text-center">
                <button
                    className="menu-button fixed top-5 right-5 flex items-center justify-center bg-orange-500 text-white border-none p-4 rounded-full h-20 w-20 z-50 transition-transform duration-300 hover:bg-orange-700"
                    onClick={toggleMenu}
                >
                    Menu
                </button>
                <div
                    className={`menu fixed top-0 right-0 w-64 h-full bg-gray-100 shadow-md transition-transform duration-300 z-40 ${
                        isMenuVisible ? 'transform translate-x-0' : 'transform translate-x-full'
                    }`}
                >
                    <ul className="list-none p-6">
                        <li className="text-lg py-4 hover:bg-gray-200 cursor-pointer"><Link to="/">Home</Link></li>
                        <li className="text-lg py-4 hover:bg-gray-200 cursor-pointer" onClick={openModal}>Partnership</li>
                        <li className="text-lg py-4 hover:bg-gray-200 cursor-pointer">Contacts</li>
                    </ul>
                </div>
                {isModalOpen && <PartnershipForm isOpen={true} onClose={closeModal} />} {/* Отображаем модальное окно, если isModalOpen === true */}
            </div>
        </Router>
    );
}

export default MenuButton;
