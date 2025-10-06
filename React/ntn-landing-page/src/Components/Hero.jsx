// components/Hero.jsx
import React from 'react';
import './Hero.css';

 const Hero = () => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>NTN Studios</h1>
        <p className="mission">To empower African businesses with bold and meaningful designs that reflect their identity.</p>
        <a href="#services" className="explore-btn">Explore Services</a>
      </div>
    </section>
  );
}

export default Hero