// Header Across all pages
import React from 'react';
import '../App.css'

const Header = () => {
    return (
        <>
            <div>
                <header className="logo">
                    <div className="">
                        <h1 className="">NTN Landing Page</h1>
                        <nav>
                            <ul className="">
                                <li><a href="#home" className="">Home</a></li>
                                <li><a href="#about" className="">About</a></li>
                                <li><a href="#services" className="">Services</a></li>
                                <li><a href="#contact" className="">Contact</a></li>
                            </ul>
                        </nav>
                    </div>
                </header>
            </div>
        </>
    )
}

export default Header;