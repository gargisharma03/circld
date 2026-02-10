import { useNavigate } from "react-router-dom";
import { useState } from "react";

const MBTI_TYPES = [
  "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
  "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"
];

export default function Preferences() {
  const navigate = useNavigate();
  
  const [mbti, setMbti] = useState("");
  const [genderPref, setGenderPref] = useState("All");

  const handleFinish = (e) => {
    e.preventDefault();

    // Get the existing data from the previous page
    const existingProfile = JSON.parse(localStorage.getItem("profile") || "{}");

    // Merge in the new preferences
    const updatedProfile = {
      ...existingProfile,
      mbti,
      genderPref
    };

    localStorage.setItem("profile", JSON.stringify(updatedProfile));

    // Now navigate to home
    navigate("/home");
  };

  return (
    <div className="page center">
      <form className="card" onSubmit={handleFinish}>
        <h2>Final Details</h2>
        <p className="muted" style={{marginBottom: '20px'}}>Help us tailor your community experience.</p>

        {/* MBTI SELECTION */}
        <div className="activities-section">
          <p className="section-title">Your MBTI Type</p>
          <div className="activities-grid">
            {MBTI_TYPES.map((type) => (
              <label key={type} className={`activity-item ${mbti === type ? "selected" : ""}`}>
                <input
                  type="radio"
                  name="mbti"
                  value={type}
                  checked={mbti === type}
                  onChange={(e) => setMbti(e.target.value)}
                  style={{ display: 'none' }}
                />
                <span>{type}</span>
              </label>
            ))}
          </div>
        </div>

        {/* GENDER PREFERENCE */}
        <div className="activities-section" style={{ marginTop: '20px' }}>
          <p className="section-title">Community Preference</p>
          <div className="button-group" style={{ marginTop: '10px' }}>
            {["All", "Women-only", "Men-only"].map((pref) => (
              <button
                key={pref}
                type="button"
                className={genderPref === pref ? "" : "secondary"}
                onClick={() => setGenderPref(pref)}
                style={{ flex: 1, fontSize: '0.85rem' }}
              >
                {pref}
              </button>
            ))}
          </div>
        </div>

        <button type="submit" className="primary-btn" style={{marginTop: '30px'}}>
          Go to Dashboard
        </button>
      </form>
    </div>
  );
}