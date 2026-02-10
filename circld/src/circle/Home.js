import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Home() {
  const navigate = useNavigate();

  const [myGroups, setMyGroups] = useState([]);
  const [polls, setPolls] = useState([]);

  useEffect(() => {
    // TEMP mock — later from backend
    setMyGroups([
      { id: 1, name: "Evening Walkers", members: 12 },
      { id: 2, name: "Dance Circle", members: 8 },
      { id: 3, name: "Book Club", members: 5 },
    ]);

    setPolls([
      {
        id: 1,
        question: "Which day works best for the meetup?",
        options: [
          { text: "Saturday", votes: 2 },
          { text: "Sunday", votes: 3 },
        ],
        voted: false,
      },
    ]);
  }, []);

  const vote = (pollId, index) => {
    setPolls(
      polls.map((p) =>
        p.id === pollId && !p.voted
          ? {
              ...p,
              voted: true,
              options: p.options.map((o, i) =>
                i === index ? { ...o, votes: o.votes + 1 } : o
              ),
            }
          : p
      )
    );
  };

  return (
    <div className="app-layout">
      <aside className="sidebar">
        <h2>Circld</h2>
        <nav>
          <button onClick={() => navigate("/groups")}>Groups</button>
          <button onClick={() => navigate("/events")}>Events</button>
          <button onClick={() => navigate("/communities")}>Communities</button>
          <button onClick={() => navigate("/profile")}>Profile</button>
        </nav>
      </aside>

      <main className="main">
        <h1>Welcome back 👋</h1>
        <p className="muted">Here’s what’s happening around you</p>

        {/* MY GROUPS */}
     {/* MY GROUPS */}
<section>
  <h2>My Groups</h2>
  <div className="group-row">
    {myGroups.map((g) => (
      <div
        key={g.id}
        className="card group-card inactive" // Added 'inactive' class
        /* onClick={() => navigate(`/groups/${g.id}`)} */ // Removed this line
      >
        <h3>{g.name}</h3>
        <p>{g.members} members</p>
      </div>
    ))}
    
    {/* Keep this one active as it's a call to action */}
    <div
      className="card group-card add"
      onClick={() => navigate("/groups")}
    >
      + Join more
    </div>
  </div>
</section>

        {/* QUICK ACTIONS */}
        <section>
          <h2>Quick Actions</h2>
          <div className="quick-actions">
            <button onClick={() => navigate("/groups")}>Find Groups</button>
            <button onClick={() => navigate("/create-group")}>
              Create Group
            </button>
            <button onClick={() => navigate("/events")}>
              Explore Events
            </button>
          </div>
        </section>

        {/* POLLS */}
        <section>
          <h2>Active Polls</h2>
          <div className="grid">
            {polls.map((poll) => (
              <div className="card" key={poll.id}>
                <h3>{poll.question}</h3>
                {poll.options.map((o, i) => (
                  <button
                    key={i}
                    className="poll-option"
                    disabled={poll.voted}
                    onClick={() => vote(poll.id, i)}
                  >
                    {o.text}
                    <span>{o.votes}</span>
                  </button>
                ))}
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
