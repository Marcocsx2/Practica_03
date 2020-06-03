import React from 'react';
import { Link } from 'react-router-dom';
import '../../assets/css/Footer.css';

const Footer = () => {
    return (
        <>
            <div className="footer bg-footer">
                &copy; {new Date().getFullYear()} Copyright: <Link to="/" className="footer-link"> Biblioteca </Link>
            </div>
        </>
    );
}

export default Footer;