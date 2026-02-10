import { useState } from "react";

export default function Events() {
  const capacity = 5;
  const [going, setGoing] = useState(3);
  const [interested, setInterested] = useState(1);
  const [chat, setChat] = useState([]);
  const [message, setMessage] = useState("");

  const [poll, setPoll] = useState({ sat: 2, sun: 1 });
  const [placePoll, setPlacePoll] = useState({ cafeA: 1, cafeB: 2 });

  const sendMessage = () => {
    if (!message) return;
    setChat([...chat, message]);
    setMessage("");
  };

  return (
    <div className="page">
      <div className="card">
        <h2>Weekend Meetup</h2>
        <p>Plan and finalize details for the upcoming meet.</p>
        <p>
          Capacity: {going}/{capacity}
        </p>
      </div>

      <div className="grid" style={{ marginTop: "16px" }}>
        <div className="card">
          <h3>Decision Poll</h3>
          <p>Saturday vs Sunday</p>
          <button onClick={() => setPoll({ ...poll, sat: poll.sat + 1 })}>
            Saturday ({poll.sat})
          </button>
          <button onClick={() => setPoll({ ...poll, sun: poll.sun + 1 })}>
            Sunday ({poll.sun})
          </button>
        </div>

        <div className="card">
          <h3>Which Cafe?</h3>
          <button
            onClick={() =>
              setPlacePoll({ ...placePoll, cafeA: placePoll.cafeA + 1 })
            }
          >
            Brew Corner ({placePoll.cafeA})
          </button>
          <button
            onClick={() =>
              setPlacePoll({ ...placePoll, cafeB: placePoll.cafeB + 1 })
            }
          >
            Bean House ({placePoll.cafeB})
          </button>
        </div>
      </div>

      <div className="grid" style={{ marginTop: "16px" }}>
        <div className="card">
          <h3>Places</h3>
          <p>Brew Corner</p>
          <p>⭐ 4.5 · Community Verified</p>

          <p style={{ marginTop: "10px" }}>Bean House</p>
          <p>⭐ 4.2 · Community Verified</p>
        </div>

        <div className="card">
          <h3>RSVP</h3>

          {going < capacity ? (
            <>
              <button onClick={() => setGoing(going + 1)}>Going</button>
              <button onClick={() => setInterested(interested + 1)}>
                Interested ({interested})
              </button>
            </>
          ) : (
            <button disabled>Waitlist</button>
          )}
        </div>
      </div>

      <div className="card" style={{ marginTop: "16px" }}>
        <h3>Live Meet Chat</h3>

        <div style={{ marginBottom: "10px" }}>
          {chat.length === 0 && <p>No messages yet.</p>}
          {chat.map((msg, i) => (
            <p key={i}>{msg}</p>
          ))}
        </div>

        <input
          placeholder="Type a message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}
