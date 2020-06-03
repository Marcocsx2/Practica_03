import React from 'react';
import Header from '../layout/Header';
import Footer from '../layout/Footer';

import '../../assets/css/Prestamo.css'

const Prestamo = () => {
    return (
        <>
            <Header />
            <div className="container table-container table-responsive">
                <div className="table-responsive">
                    <table class="table table-striped table-bordered text-center">
                        <thead>
                            <tr>
                                <th>Ejemplar</th>
                                <th>Libro</th>
                                <th>Cliente</th>
                                <th>Incio</th>
                                <th>Fin</th>
                                <th>Finalizar</th>
                                <th>Eliminar</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>001</td>
                                <td>Libro Php</td>
                                <td>Marco</td>
                                <td>2020-06-02</td>
                                <td>2020-06-05</td>
                                <td><button className="btn btn-success">Finalizar</button></td>
                                <td><button className="btn btn-danger">Eliminar</button></td>  
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <Footer />
        </>
    );
}

export default Prestamo;