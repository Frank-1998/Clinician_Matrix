import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import PatientDashboardPage from './pages/PatientDashboard';
import SkillsPage from './pages/SkillsPage';
import NurseProfile from './pages/NurseProfile';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ManagerProfile from './pages/ManagerProfile';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "login",
    element: <LoginPage/>,
  },
  {
    path: "signup",
    element: <SignupPage/>,
  },
  {
    path: "dashboard",
    element: <PatientDashboardPage/>,
  },
  {
    path: "skills",
    element: <SkillsPage/>,
  },
  {
    path: "mprofile",
    element: <ManagerProfile/>,
  },
  {
    path: "nprofile",
    element: <NurseProfile/>,
  },
]);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
