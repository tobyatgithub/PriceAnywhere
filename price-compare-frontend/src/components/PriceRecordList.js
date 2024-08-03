import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const PriceRecordList = () => {
  // 模拟数据
  const initialRecords = [
    { id: 1, product_id: 'P001', product_name: 'Milk', price: 2.99, unit: 'liter', store: 'SuperMart', date: '2024-08-01' },
    { id: 2, product_id: 'P002', product_name: 'Bread', price: 1.99, unit: 'loaf', store: 'BakersBest', date: '2024-08-02' },
    { id: 3, product_id: 'P003', product_name: 'Eggs', price: 3.49, unit: 'dozen', store: 'FarmFresh', date: '2024-08-03' },
  ];

  const [records, setRecords] = useState(initialRecords);
  const [sortField, setSortField] = useState('');
  const [sortDirection, setSortDirection] = useState('asc');

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

  const handleDelete = (id) => {
    // 这里将来会添加 API 调用
    console.log('Deleting record with id:', id);
  };

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