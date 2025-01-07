import axios from 'axios';
import { baseUrl } from '../config/baseUrl';

export const getFilms = async (pageNumber?: number, genre?: string) => {
  return await axios.get(`${baseUrl}/films`, {
    params: {
      page: pageNumber ?? 1,
      genre: genre ?? '',
    },
  });
};

export const getGenres = async () => {
  return await axios.get(`${baseUrl}/genres`);
};
