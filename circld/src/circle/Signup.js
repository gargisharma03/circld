import { useNavigate } from "react-router-dom";
import { useState } from "react";


const ACTIVITY_OPTIONS = [
  "Evening Walks",
  "Dancing",
  "Yoga",
  "Cycling",
  "Gym",
  "Sports",
  "Volunteering",
  "Book Clubs",
];

export default function Signup() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [activities, setActivities] = useState([]);
  const [activityNote, setActivityNote] = useState("");

  const toggleActivity = (activity) => {
    setActivities((prev) =>
      prev.includes(activity)
        ? prev.filter((a) => a !== activity)
        : [...prev, activity]
    );
  };

// Inside Signup.js handleSignup function:
const handleSignup = (e) => {
  e.preventDefault();
  
  localStorage.setItem("profile", JSON.stringify({
    name, email, activities, activityNote
  }));

  // CHANGE THIS LINE:
  navigate("/preferences"); 
};

  return (
    <div className="page center">
      <form className="card" onSubmit={handleSignup}>
        <h2>Set Up Profile</h2>

        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {/* ACTIVITIES */}
        <div className="activities-section">
          <p className="section-title">Preferred Activities</p>

          <div className="activities-grid">
            {ACTIVITY_OPTIONS.map((activity) => (
              <label key={activity} className="activity-item">
                <input
                  type="checkbox"
                  checked={activities.includes(activity)}
                  onChange={() => toggleActivity(activity)}
                />
                <span>{activity}</span>
              </label>
            ))}
          </div>
        </div>

        <textarea
          rows="3"
          placeholder="Write more about your activities (timings, pace, custom activities...)"
          value={activityNote}
          onChange={(e) => setActivityNote(e.target.value)}
        />

        <button type="submit">Create Account</button>
      </form>
    </div>
  );
}
