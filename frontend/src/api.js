import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const getChatResponse = async (query) => {
    const response = await axios.post(`${API_URL}/chat`, { query });
    return response.data;
};