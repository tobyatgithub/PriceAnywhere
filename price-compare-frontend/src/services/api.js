import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getPriceRecords = () => api.get('/price_records');
export const createPriceRecord = (data) => api.post('/price_records', data);
export const updatePriceRecord = (id, data) => api.put(`/price_records/${id}`, data);
export const deletePriceRecord = (id) => api.delete(`/price_records/${id}`);

export default api;