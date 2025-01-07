import React from 'react';
import { useEffect, useState } from 'react';
import { getGenres } from '../../services/filmsService';
import { Genre } from '../../models/Movies.model';
import { Select } from 'antd';

export const Genres = ({ genre, setGenre }: {genre: Genre, setGenre: React.Dispatch<React.SetStateAction<string | undefined>>}) => {

  const [genres, setGenres] = useState<Genre[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    getGenres()
      .then(res => {
        setGenres(res.data.items);
        setIsLoading(false);
      })
      .catch(err => console.error(err))
      .finally(() => setIsLoading(false));
  }, []);

  return (
    <Select loading={isLoading} style={{ minWidth: 150 }} defaultValue={genre} onChange={(genre) => setGenre(genre.name)} allowClear onClear={() => setGenre('')}>
      {
        genres.map((genre, i) => {
          return <Select.Option key={i} value={genre.name}>{genre.name}</Select.Option>;
        })
      }
    </Select>
  );
};
