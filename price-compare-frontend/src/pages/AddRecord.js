import React from 'react';
import { useNavigate } from 'react-router-dom';
import PriceRecordForm from '../components/PriceRecordForm';

const AddRecord = () => {
  const navigate = useNavigate();

  const handleSubmit = (result) => {
    console.log('New record created:', result);
    navigate('/');
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Add New Price Record</h1>
      <PriceRecordForm onSubmit={handleSubmit} />
    </div>
  );
};

export default AddRecord;