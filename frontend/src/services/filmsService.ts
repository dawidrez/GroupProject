import axios from 'axios';
import { baseUrl } from '../config/baseUrl';

export const getFilms = async () => {
  return await axios.get(`${baseUrl}/films`);
};
