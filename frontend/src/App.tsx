
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login1 from "./Login1.tsx"
import Signup from "./Signup.tsx"

const App: React.FC = () => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login1 />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </Router>
  );
  
}

export default App
