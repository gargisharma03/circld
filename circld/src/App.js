import "./App.css"; // 👈 THIS WAS MISSING

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./circle/Landing";
import Login from "./circle/Login";
import Signup from "./circle/Signup";
import Home from "./circle/Home";
import Groups from "./circle/GroupDetail";
import Events from "./circle/Events";
import Communities from "./circle/Communities";
import Profile from "./circle/Profile";
import Preferences from "./circle/Preferences";
import CreateGroup from "./circle/CreateGroup";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/create-group" element={<CreateGroup />} />
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<Home />} />
        <Route path="/groups" element={<Groups />} />
        <Route path="/events" element={<Events />} />
        <Route path="/communities" element={<Communities />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/preferences" element={<Preferences />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
