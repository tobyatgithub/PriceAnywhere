import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PriceRecordForm from '../components/PriceRecordForm';
import { getPriceRecord } from '../services/api';

const EditRecord = () => {
  const { price_record_id } = useParams();
  const navigate = useNavigate();
  const [record, setRecord] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecord = async () => {
      if (!price_record_id) {
        setError('No record ID provided');
        setLoading(false);
        return;
      }
      try {
        const response = await getPriceRecord(price_record_id);
        setRecord(response.data);
      } catch (err) {
        console.error('Fetch error:', err);
        setError(`Failed to fetch record. ${err.response ? err.response.data.detail : err.message}`);
      } finally {
        setLoading(false);
      }
    };

    fetchRecord();
  }, [price_record_id]);

  const handleSubmit = (result) => {
    console.log('Record updated:', result);
    navigate('/');
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