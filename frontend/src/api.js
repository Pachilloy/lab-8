import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'
})

export const fetchBooks = () => api.get('/books')
export const fetchBook = (id) => api.get(`/books/${id}`)
export const createBook = (payload) => api.post('/books', payload)
export const updateBook = (id, payload) => api.put(`/books/${id}`, payload)
export const deleteBook = (id) => api.delete(`/books/${id}`)
export const fetchStats = () => api.get('/stats')

export default api
