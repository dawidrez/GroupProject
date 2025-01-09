import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Movies } from './components/movies/Movies';

const App = () => {
  return (
    <Routes>
      <Route path="/"
        element={<Movies />} />
    </Routes>
  );
};

export default App;

