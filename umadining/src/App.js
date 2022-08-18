import Locations from './views/Locations';
import Results from './views/Results';
import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import FoodSelector from './views/FoodSelector';

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
