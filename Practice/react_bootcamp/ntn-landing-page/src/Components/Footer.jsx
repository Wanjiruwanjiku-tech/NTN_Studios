import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-columns">
        <div>
          <h4>NTN Studios</h4>
          <p>Bold. Cultural. African.</p>
        </div>
        <div>
          <h4>Quick Links</h4>
          <ul>
            <li><a href="#services">Services</a></li>
            <li><a href="#">Cart</a></li>
            <li><a href="#">About</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <p>Email: hello@ntnstudios.africa</p>
          <p>Phone: +254 712 345 678</p>
        </div>
        <div>
          <h4>Newsletter</h4>
          <input type="email" placeholder="Your email" />
          <button>Subscribe</button>
        </div>
      </div>
      <p className="copyright">&copy; 2025 NTN Studios. All rights reserved.</p>
    </footer>
  );
}

export default Footer;