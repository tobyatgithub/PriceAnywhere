import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getPriceRecords = () => api.get('/price_records/');  // 注意这里添加了末尾的斜杠
export const createPriceRecord = (data) => api.post('/price_records/', data);
export const updatePriceRecord = (id, data) => api.put(`/price_records/${id}/`, data);
export const deletePriceRecord = (id) => api.delete(`/price_records/${id}/`);

// 添加错误拦截器
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response ? error.response.data : error.message);
    return Promise.reject(error);
  }
);

export default api;