import { useNavigate } from "react-router-dom";

export default function Communities() {
  const navigate = useNavigate();

  const communities = [
    {
      name: "Movies & Shows",
      description: "Watch parties, reviews, recommendations"
    },
    {
      name: "Fitness",
      description: "Workouts, runs, wellness routines"
    },
    {
      name: "Tech & Coding",
      description: "Projects, learning, discussions"
    },
    {
      name: "Travel",
      description: "Trips, planning, experiences"
    },
    {
      name: "Books",
      description: "Reading circles and discussions"
    }
  ];

  return (
    <div className="page">
      <h2>Communities</h2>
      <p>Browse and explore based on what you’re interested in.</p>

      <div className="grid">
        {communities.map((item, index) => (
          <div className="card" key={index}>
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <button onClick={() => navigate("/groups")}>
              View Groups
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
