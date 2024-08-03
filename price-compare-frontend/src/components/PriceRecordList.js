import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getPriceRecords, deletePriceRecord } from '../services/api';

const PriceRecordList = () => {
  const [records, setRecords] = useState([]);
  const [sortField, setSortField] = useState('');
  const [sortDirection, setSortDirection] = useState('asc');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      setLoading(true);
      const response = await getPriceRecords();
      setRecords(response.data);
      setError(null);
    } catch (err) {
      console.error('Fetch error:', err);
      setError(`Failed to fetch records. ${err.response ? err.response.data.detail : err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleSort = (field) => {
    const direction = field === sortField && sortDirection === 'asc' ? 'desc' : 'asc';
    setSortField(field);
    setSortDirection(direction);

    const sortedRecords = [...records].sort((a, b) => {
      if (a[field] < b[field]) return direction === 'asc' ? -1 : 1;
      if (a[field] > b[field]) return direction === 'asc' ? 1 : -1;
      return 0;
    });

    setRecords(sortedRecords);
  };

  const handleDelete = async (id) => {
    try {
      await deletePriceRecord(id);
      fetchRecords(); // Refresh the list after deletion
    } catch (err) {
      setError('Failed to delete record. Please try again later.');
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white">
        <thead className="bg-gray-100">
          <tr>
            {['Product ID', 'Product Name', 'Price', 'Unit', 'Store', 'Date', 'Actions'].map((header) => (
              <th 
                key={header} 
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                onClick={() => handleSort(header.toLowerCase().replace(' ', '_'))}
              >
                {header}
                {sortField === header.toLowerCase().replace(' ', '_') && (
                  <span className="ml-1">{sortDirection === 'asc' ? '▲' : '▼'}</span>
                )}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {records.map((record) => (
            <tr key={record.id}>
              <td className="px-6 py-4 whitespace-nowrap">{record.product_id}</td>
              <td className="px-6 py-4 whitespace-nowrap">{record.product_name}</td>
              <td className="px-6 py-4 whitespace-nowrap">${record.price.toFixed(2)}</td>
              <td className="px-6 py-4 whitespace-nowrap">{record.unit}</td>
              <td className="px-6 py-4 whitespace-nowrap">{record.store}</td>
              <td className="px-6 py-4 whitespace-nowrap">{record.date}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <Link to={`/edit/${record.id}`} className="text-indigo-600 hover:text-indigo-900 mr-4">Edit</Link>
                <button onClick={() => handleDelete(record.id)} className="text-red-600 hover:text-red-900">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PriceRecordList;