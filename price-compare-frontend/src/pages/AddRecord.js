import React from 'react';
import PriceRecordForm from '../components/PriceRecordForm';

const AddRecord = () => {
  const handleSubmit = (formData) => {
    // 这里我们将来会添加 API 调用
    console.log('Submitting form data:', formData);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Add New Price Record</h1>
      <PriceRecordForm onSubmit={handleSubmit} />
    </div>
  );
};

export default AddRecord;