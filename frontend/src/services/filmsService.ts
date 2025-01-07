import axios from 'axios';
import { baseUrl } from '../config/baseUrl';

export const getFilms = async (pageNumber?: number) => {
  return await axios.get(`${baseUrl}/films`, {
    params: {
      page: pageNumber ?? 1,
    },
  });
};

