import React from 'react';
import { createBrowserRouter, RouterProvider, Outlet } from 'react-router-dom';
import Home from './pages/Home';
import Statistics from './pages/Stats';
import PublicSpeaking from './pages/PublicSpeaking';
import Business from './pages/Business';
import Psychology from './pages/Psychology';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/statistics",
    element: <Statistics />, 
  },
  {
    path: "/public-speaking",
    element: <PublicSpeaking />,
  },
  {
    path: "/business",
    element: <Business />,
  },
  {
    path: "/psychology",
    element: <Psychology />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
