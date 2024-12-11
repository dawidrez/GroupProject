import React, { useEffect, useState } from 'react';
import { Card, Flex, Image, Input, Rate, Typography } from 'antd';
import { movies } from '../../../movies';
import { Movie } from '../../models/Movies.model';
import { Controller, useForm } from 'react-hook-form';

export const MoviesList = () => {
  const [moviesList, setMoviesList] = useState<Movie[]>(movies);
  const { control, watch } = useForm();

  const search: string = watch('search');

  useEffect(() => {
    if (search) {
      setMoviesList(() => movies.filter((movie) => movie.englishName.toLowerCase().includes(search.toLowerCase())));
    }
  }, [search]);

  return (
    <Flex vertical align='center' gap={20} style={{ position: 'relative'}}>
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
      </Flex>
      <Flex style={{ maxWidth: '60%'}} vertical gap={30} >
        {
          moviesList.map((movie) => {
            return (
              <Card key={movie.originalName}>
                <Flex
                  align='center'
                  gap={20}
                  key={movie.originalName}>
                  <Image
                    src='https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_640.jpg'
                    height={150}/>
                  <Flex vertical align='flex-start' style={{ height: '100%'}}>
                    <Typography.Title level={3}>
                      {movie.englishName}
                    </Typography.Title>
                    <Flex vertical gap={10}>
                      <Typography>Filmbeb rate</Typography>
                      <Rate count={10} value={movie.ratingFilmweb} disabled allowHalf/>
                      <Typography>Imb rate</Typography>
                      <Rate count={10} value={movie.ratingImdb} disabled allowHalf/>
                      <Typography>Filmbeb rate</Typography>
                      <Rate count={10} value={movie.ratingImdb} disabled allowHalf/>
                    </Flex>
                  </Flex>
                </Flex>
              </Card>
            );
          })
        }
      </Flex>
    </Flex>
  );
};
