import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';  // newimport App from './App.jsx';
import App from './App.jsx';

ReactDOM.render((
      // new
  <Router>
    <App/>
  </Router>
),document.getElementById('root'))