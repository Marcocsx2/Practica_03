import React from 'react';
import '../../assets/css/Header.css'

const Header = () => {
    return (
        <>
            <nav className="navbar navbar-expand-sm navbar-dark bg-info">
                <a className="navbar-brand" href="/">Biblioteca</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse navb" id="navbarNav">
                    <ul className="navbar-nav nav-ul">
                        <li className="nav-item nav-li">
                            <a className="nav-link nav-a" href="/" exact>Nuevo Prestamo</a>
                        </li>
                        <li className="nav-item nav-li">
                            <a className="nav-link nav-a" href="/prestamos" exact>Lista de Prestamos</a>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    );
}

export default Header;