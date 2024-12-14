export interface Movie {
  id: string;
  original_title: string;
  english_title: string;
  year: number;
  filmweb_rating: number;
  imdb_rating: number;
  src: string;
  genres: { id: string, name: string }[];
}
