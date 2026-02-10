import { useState, useEffect } from "react";

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

export default function Profile() {
  const storedProfile = JSON.parse(localStorage.getItem("profile")) || {};

  const [name, setName] = useState(storedProfile.name || "");
  const [bio, setBio] = useState(storedProfile.bio || "");
  const [activities, setActivities] = useState(storedProfile.activities || []);
  const [activityNote, setActivityNote] = useState(
    storedProfile.activityNote || ""
  );

  const toggleActivity = (activity) => {
    setActivities((prev) =>
      prev.includes(activity)
        ? prev.filter((a) => a !== activity)
        : [...prev, activity]
    );
  };

  const handleSave = () => {
    localStorage.setItem(
      "profile",
      JSON.stringify({
        ...storedProfile,
        name,
        bio,
        activities,
        activityNote,
      })
    );
    alert("Profile updated ✅");
  };

  return (
    <div className="page">
      <h2>My Profile</h2>

      <div className="card">
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="text"
          placeholder="Short bio"
          value={bio}
          onChange={(e) => setBio(e.target.value)}
        />

        <p className="section-title">Edit Activities</p>

        <div className="activities-list">
          {ACTIVITY_OPTIONS.map((activity) => (
            <label key={activity} className="activity-row">
              <input
                type="checkbox"
                checked={activities.includes(activity)}
                onChange={() => toggleActivity(activity)}
              />
              <span>{activity}</span>
            </label>
          ))}
        </div>

        <textarea
          rows="3"
          placeholder="Edit activity notes (timings, pace, extra activities...)"
          value={activityNote}
          onChange={(e) => setActivityNote(e.target.value)}
        />

        <button onClick={handleSave} className="primary-btn">
          Save Changes
        </button>
      </div>
    </div>
  );
}
