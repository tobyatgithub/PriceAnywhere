import React from 'react';
import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <nav className="bg-blue-500 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-white text-2xl font-bold">Price Compare</Link>
        <div>
          <Link to="/" className="text-white mr-4">Home</Link>
          <Link to="/add" className="text-white mr-4">Add Record</Link>
          <Link to="/compare" className="text-white">Compare</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;