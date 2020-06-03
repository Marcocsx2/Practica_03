import React from 'react';
import Header from '../layout/Header';
import Footer from '../layout/Footer';

import '../../assets/css/Registrar.css'

const Registrar = () => {
    return (
        <>
            <Header />
            <div className="container">
                <div className="row justify-content-center ">
                    <header className="form-header col-8 ">
                        <form action="/action_page.php" class="was-validated">
                            <div class="form-group">
                                <label for="libro">Libro:</label>
                                <select class="custom-select" id="libro">
                                    <option value="1">Libro de PHP</option>
                                </select>
                                <div class="valid-feedback">Completado</div>
                                <div class="invalid-feedback">EL campo es requerido.</div>
                            </div>
                            <div class="form-group">
                                <label for="codigo">Codigo:</label>
                                <input type="number" class="form-control" id="codigo" placeholder="Codigo del usuario" name="codigo" required />
                                <div class="valid-feedback">Completado</div>
                                <div class="invalid-feedback">EL campo es requerido.</div>
                            </div>
                            <div class="form-group">
                                <label for="fc_inicio">Fecha de prestamo:</label>
                                <input type="date" class="form-control" id="fc_inicio" name="fc_inicio" required />
                                <div class="valid-feedback">Completado</div>
                                <div class="invalid-feedback">EL campo es requerido.</div>
                            </div>
                            <div class="form-group">
                                <label for="fc_fin">Fecha de devolución:</label>
                                <input type="date" class="form-control" id="fc_fin" name="fc_fin" required />
                                <div class="valid-feedback">Completado</div>
                                <div class="invalid-feedback">EL campo es requerido.</div>
                            </div>
                            <button type="submit" class="btn btn-success">Realizar Prestamo</button>
                        </form>
                    </header>
                </div>
            </div>
            < Footer />
        </>
    );
}

export default Registrar;