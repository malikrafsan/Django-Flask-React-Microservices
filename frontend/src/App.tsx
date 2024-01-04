import "./App.css";
import "./helpers/axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Login } from "./pages/login";
import { Home } from "./pages/home";
import { Navigation } from "./components/navigation";
import { Logout } from "./pages/logout";
import { Register } from "./pages/register";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

function App() {
  return (
    <BrowserRouter>
      <Navigation></Navigation>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
