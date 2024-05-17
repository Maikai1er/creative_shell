import React, { useState } from 'react';
import Modal from 'react-modal';

function PartnershipForm({ isOpen, onClose }) {
  const [formData, setFormData] = useState({
    name: '',
    contact: '',
    about: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('Отправка данных:', formData);
      onClose();
    } catch (error) {
      console.error('Ошибка отправки данных:', error);
    }
  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      ariaHideApp={false}
      className="fixed inset-0 flex justify-center items-center bg-gray-900 bg-opacity-50"
      overlayClassName="fixed inset-0 bg-transparent"
    >
      <div className="bg-white p-8 rounded-lg max-w-md mx-auto">
        <button className="absolute top-4 right-4 text-gray-500 hover:text-gray-700" onClick={onClose}>X</button>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Имя"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500"
          />
          <input
              type="text"
              name="contact"
              value={formData.contact}
              onChange={handleChange}
              placeholder="Контакт"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500"
          />
          <textarea
              name="about"
              value={formData.about}
              onChange={handleChange}
              placeholder="О себе"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500"
          />
          <button type="submit" className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-700">Отправить
          </button>
        </form>
      </div>
    </Modal>
  );
}

export default PartnershipForm;
