import React, { useState, useEffect } from 'react';
import { createPriceRecord, updatePriceRecord } from '../services/api';

const PriceRecordForm = ({ initialData, onSubmit }) => {
  const [formData, setFormData] = useState({
    product_id: '',
    product_name: '',
    price: '',
    unit: '',
    store: '',
    date: new Date().toISOString().split('T')[0]
  });

  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (initialData) {
      setFormData(initialData);
    }
  }, [initialData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  const validateForm = () => {
    let tempErrors = {};
    if (!formData.product_id) tempErrors.product_id = "Product ID is required";
    if (!formData.product_name) tempErrors.product_name = "Product name is required";
    if (!formData.price) tempErrors.price = "Price is required";
    else if (isNaN(formData.price)) tempErrors.price = "Price must be a number";
    if (!formData.unit) tempErrors.unit = "Unit is required";
    if (!formData.store) tempErrors.store = "Store is required";
    setErrors(tempErrors);
    return Object.keys(tempErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (validateForm()) {
      try {
        let result;
        if (initialData && initialData._id) {
          // If we have an initial _id, we're updating
          result = await updatePriceRecord(initialData._id, formData);
        } else {
          // If we don't have an initial _id, we're creating
          result = await createPriceRecord(formData);
        }
        onSubmit(result);
      } catch (error) {
        console.error('Error submitting form:', error);
        setErrors({ submit: 'Failed to submit the form. Please try again.' });
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="product_id" className="block text-sm font-medium text-gray-700">Product ID</label>
        <input
          type="text"
          name="product_id"
          id="product_id"
          value={formData.product_id}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
        {errors.product_id && <p className="mt-1 text-sm text-red-600">{errors.product_id}</p>}
      </div>

      <div>
        <label htmlFor="product_name" className="block text-sm font-medium text-gray-700">Product Name</label>
        <input
          type="text"
          name="product_name"
          id="product_name"
          value={formData.product_name}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
        {errors.product_name && <p className="mt-1 text-sm text-red-600">{errors.product_name}</p>}
      </div>

      <div>
        <label htmlFor="price" className="block text-sm font-medium text-gray-700">Price</label>
        <input
          type="number"
          name="price"
          id="price"
          value={formData.price}
          onChange={handleChange}
          step="0.01"
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
        {errors.price && <p className="mt-1 text-sm text-red-600">{errors.price}</p>}
      </div>

      <div>
        <label htmlFor="unit" className="block text-sm font-medium text-gray-700">Unit</label>
        <input
          type="text"
          name="unit"
          id="unit"
          value={formData.unit}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
        {errors.unit && <p className="mt-1 text-sm text-red-600">{errors.unit}</p>}
      </div>

      <div>
        <label htmlFor="store" className="block text-sm font-medium text-gray-700">Store</label>
        <input
          type="text"
          name="store"
          id="store"
          value={formData.store}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
        {errors.store && <p className="mt-1 text-sm text-red-600">{errors.store}</p>}
      </div>

      <div>
        <label htmlFor="date" className="block text-sm font-medium text-gray-700">Date</label>
        <input
          type="date"
          name="date"
          id="date"
          value={formData.date}
          onChange={handleChange}
          className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        />
      </div>

      <div>
        <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Submit
        </button>
      </div>
    </form>
  );
};

export default PriceRecordForm;