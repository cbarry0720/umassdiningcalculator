import logo from './logo.svg';
import Locations from './views/Locations';
import Results from './views/Results';
import './App.css';
import Banner from './components/Banner';
import {BrowserRouter, Routes, Route, Link} from "react-router-dom";
import FoodSelector from './views/FoodSelector';
import { useState } from "react";

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route index path="/" element={<Locations/>} />
          <Route path="/foods" element={<FoodSelector/>}/>
          <Route path="/results" element={<Results/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
