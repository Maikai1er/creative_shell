import React, { useState } from 'react';
import Modal from 'react-modal';
import { motion } from 'framer-motion';
import { X } from 'lucide-react';
import './PartnershipForm.css';

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
      const response = await fetch(`${process.env.REACT_APP_API_HOST}/receive_contact_data/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      if (!response.ok) {
        throw new Error('Ошибка при отправке данных');
      }
      console.log('Данные успешно отправлены');
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
      className='modal'
      overlayClassName='overlay'
    >
      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.9, opacity: 0 }}
        className='modal-content'
      >
        <div className='modal-header'>
          <h2>Contact us</h2>
          <button onClick={onClose} className='close-button'>
            <X size={24} />
          </button>
        </div>
        <form onSubmit={handleSubmit}>
          <div className='form-group'>
            <label htmlFor='name'>Name</label>
            <input
              id='name'
              type='text'
              name='name'
              value={formData.name}
              onChange={handleChange}
              required
              placeholder='Enter your name'
            />
          </div>
          <div className='form-group'>
            <label htmlFor='contact'>Contact</label>
            <input
              id='contact'
              type='text'
              name='contact'
              value={formData.contact}
              onChange={handleChange}
              required
              placeholder='Email or phone'
            />
          </div>
          <div className='form-group'>
            <label htmlFor='about'>About</label>
            <textarea
              id='about'
              name='about'
              value={formData.about}
              onChange={handleChange}
              required
              rows='4'
              placeholder='Tell about yourself and the appeal reson'
            />
          </div>
          <button type='submit' className='submit-button'>
            Send
          </button>
        </form>
      </motion.div>
    </Modal>
  );
}

export default PartnershipForm;