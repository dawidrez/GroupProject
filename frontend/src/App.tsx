import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Test } from './components/Test';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Test />} />
    </Routes>
  );
};

export default App;
