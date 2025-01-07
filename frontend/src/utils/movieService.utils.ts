import { getFilms } from '../services/filmsService';

export const getFilmsData = async (pageNumber: number = 1, genre: string) => {
  return getFilms(pageNumber, genre)
    .then((res) => {
      return {
        items: res.data.items,
        totalItems: res.data.pagination.total_items,
        pagination: res.data.pagination,
      };
    })
    .catch((e) => {
      console.error(e);
      throw e;
    });
};
