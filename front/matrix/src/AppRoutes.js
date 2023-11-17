import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login.js';

export const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Login />} />
      </Routes>
    </Router>
  );
};
