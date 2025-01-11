import React from 'react';
import { Card, Flex, Image, Rate, Row, Typography } from 'antd';
import { Movie } from '../../models/Movies.model';

export const MoviesList = ({ movies }: { movies: Movie[] }) => {
  return (
    <Row style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20 }}>
      {
        movies.map((movie, i) => {
          return (
            <Card key={i}>
              <Flex
                align='center'
                gap={20}
                key={movie.id}>
                <Image
                  preview={false}
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
                    <Flex gap={20}>
                      <Rate count={10} value={movie.filmweb_rating} disabled allowHalf/>
                      {
                        movie.filmweb_rating ? movie.filmweb_rating : null
                      }
                    </Flex>
                    <Typography>Imb rate</Typography>
                    <Flex gap={20}>
                      <Rate count={10} value={movie.imdb_rating} disabled allowHalf/>
                      {
                        movie.imdb_rating ? movie.imdb_rating : null
                      }
                    </Flex>
                    <Typography>Metacritics rate</Typography>
                    <Flex gap={20}>
                      <Rate count={10} value={movie.metacritic_rating} disabled allowHalf/>
                      {
                        movie.metacritic_rating ? movie.imdb_rating : null
                      }
                    </Flex>
                  </Flex>
                </Flex>
              </Flex>
            </Card>
          );
        })
      }
    </Row>
  );
};
