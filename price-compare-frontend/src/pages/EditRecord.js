import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PriceRecordForm from '../components/PriceRecordForm';
import api from '../services/api';

const EditRecord = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [record, setRecord] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecord = async () => {
      try {
        const response = await api.get(`/price_records/${id}`);
        setRecord(response.data);
      } catch (err) {
        setError('Failed to fetch record. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchRecord();
  }, [id]);

  const handleSubmit = () => {
    navigate('/'); // Redirect to home page after successful edit
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Edit Price Record</h1>
      {record && <PriceRecordForm initialData={record} onSubmit={handleSubmit} />}
    </div>
  );
};

export default EditRecord;