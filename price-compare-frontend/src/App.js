import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import AddRecord from './pages/AddRecord';
import EditRecord from './pages/EditRecord';
import Comparison from './pages/Comparison';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add" element={<AddRecord />} />
          <Route path="/edit/:id" element={<EditRecord />} />
          <Route path="/compare" element={<Comparison />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;