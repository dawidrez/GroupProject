/* eslint-disable indent */
import React, { useEffect, useState } from 'react';
import {  Flex, Input, Spin, Pagination } from 'antd';
import { Genre, Movie } from '../../models/Movies.model';
import { Controller, useForm } from 'react-hook-form';
import { MoviesList } from './MoviesList';
import { getFilmsData } from '../../utils/movieService.utils';
import { Genres } from '../genres/Genres';

export const Movies = () => {
  const [moviesList, setMoviesList] = useState<Movie[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [moviesTotalCount, setMoviesTotalCount] = useState<number>(0);
  const [genre, setGenre] = useState<string>('');

  const { control, watch } = useForm();

  const search: string = watch('search');

  useEffect(() => {
    console.log('here');
    console.log(genre);
    setIsLoading(true);
    getFilmsData(1, genre)
      .then(({ items, totalItems }) => {
        setMoviesList(items);
        setMoviesTotalCount(totalItems);
      })
      .finally(() => setIsLoading(false));
  }, [genre]);

  useEffect(() => {
    if (search) {
      setMoviesList(() => moviesList.filter((movie) => movie.original_title.toLowerCase().includes(search.toLowerCase())));
    }
  }, [search]);

  const onPageChange = (pageNumber: number) => {
    getFilmsData(pageNumber, genre.name)
    .then(({ items, totalItems }) => {
      setMoviesList(items);
      setMoviesTotalCount(totalItems);
    },
    )
    .catch((e) => console.error(e))
    .finally(() => setIsLoading(false));
  };

  return (
    <Flex vertical align='center' gap={20} style={{ position: 'relative', height: 'calc(100vh - 40px)', justifyContent: 'space-between', padding: 20}}>
      <Flex align='center' justify='center' style={
        {
          position: 'sticky',
          zIndex: 2,
          top: 0,
          backgroundColor: 'whitesmoke',
          height: '70px',
          width: '100%',
        }
      }>
        <Controller
          name="search"
          control={control}
          render={({ field }) => (
            <Input.Search
              {...field}
              placeholder="Search for films"
              style={{ maxWidth: 400 }}
              onChange={(e) => field.onChange(e.target.value)}/>
          )}/>
        <Genres setGenre={setGenre} genre={genre} />
      </Flex>
      {
        isLoading ? <Spin size='large'/> :
        <MoviesList movies={moviesList}/>
      }
      <Pagination total={moviesTotalCount} defaultCurrent={1} onChange={onPageChange} pageSize={9} showSizeChanger={false}/>
    </Flex>
  );
};
