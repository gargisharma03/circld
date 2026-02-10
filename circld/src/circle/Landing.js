import { useNavigate } from "react-router-dom";

export default function Landing() {
  const navigate = useNavigate();

  return (
    <div className="page center">
      <div className="hero-content">
        <h1>Circld</h1>
        <p>Find people. Plan things. Do stuff.</p>
        
        <div className="button-group">
          {/* Add the onClick handlers here */}
          <button 
            className="btn-login" 
            onClick={() => navigate("/login")}
          >
            Log In
          </button> 
          <button 
            className="btn-signup secondary" 
            onClick={() => navigate("/signup")}
          >
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
}