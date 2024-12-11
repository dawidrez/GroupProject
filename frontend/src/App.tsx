import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { MoviesList } from './components/movies/MoviesList';

const App = () => {
  return (
    <Routes>
      <Route path="/"
        element={<MoviesList />} />
    </Routes>
  );
};

export default App;

