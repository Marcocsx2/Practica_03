import React from 'react';
import './assets/css/App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Registrar from './components/Registro/Registrar';
import Prestamo from './components/Prestamos/Prestamo';
import Error from './components/layout/Error';

function App() {
  return (
    <>
      <Router>
        <Switch>
          <Route exact path="/" component={Registrar} />
          <Route exact path="/prestamos" component={Prestamo} />
          <Route path="*" component={Error} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
