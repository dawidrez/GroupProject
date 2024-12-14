/* eslint-disable indent */
import React, { useEffect, useState } from 'react';
import { Card, Flex, Image, Input, Rate, Typography, Spin } from 'antd';
import { Movie } from '../../models/Movies.model';
import { Controller, useForm } from 'react-hook-form';
import { getFilms } from '../../services/filmsService';

export const MoviesList = () => {
  const [moviesList, setMoviesList] = useState<Movie[]>([]);
  const [allMovies, setAllMovies] = useState<Movie[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const { control, watch } = useForm();

  const search: string = watch('search');

  useEffect(() => {
    setIsLoading(true);
    getFilms()
      .then((res) => {
        setMoviesList(res.data);
        setAllMovies(res.data);
      },
      )
      .catch((e) => console.error(e))
      .finally(() => setIsLoading(false));
  }, []);

  useEffect(() => {
    if (search) {
      setMoviesList(() => moviesList.filter((movie) => movie.original_title.toLowerCase().includes(search.toLowerCase())));
    } else {
      setMoviesList(allMovies);
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
      {
        isLoading ? <Spin size='large'/> :
        <Flex style={{ maxWidth: '60%'}} vertical gap={30}>
          {
              moviesList.map((movie, i) => {
                return (
                  <Card key={i}>
                    <Flex
                      align='center'
                      gap={20}
                      key={movie.id}>
                      <Image
                        src={`${movie.src}`}
                        height={250}/>
                      <Flex vertical align='flex-start' style={{ height: '100%'}}>
                        <Flex gap={5} vertical style={{ paddingBottom: 10 }}>
                          <Typography.Title level={3} style={{ margin: 0 }}>
                            {movie.original_title}
                          </Typography.Title>
                          <Flex gap={20}>
                            <Typography.Text strong>{movie.year}</Typography.Text>
                            {
                              movie.genres.map((genre) => <Typography.Text strong key={genre.id}>{genre.name}</Typography.Text>)
                            }
                          </Flex>
                        </Flex>
                        <Flex vertical gap={10}>
                          <Typography>Filmbeb rate</Typography>
                          <Rate count={10} value={movie.filmweb_rating} disabled allowHalf/>
                          <Typography>Imb rate</Typography>
                          <Rate count={10} value={movie.filmweb_rating} disabled allowHalf/>
                          <Typography>Filmbeb rate</Typography>
                          <Rate count={10} value={movie.filmweb_rating} disabled allowHalf/>
                        </Flex>
                      </Flex>
                    </Flex>
                  </Card>
                );
              })
            }
        </Flex>
      }
    </Flex>
  );
};
