import React from 'react';
import PriceRecordList from '../components/PriceRecordList';

const Home = () => {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Price Records</h1>
      <PriceRecordList />
    </div>
  );
};

export default Home;