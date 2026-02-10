import { useState } from "react";

export default function GroupDetail() {
  const [message, setMessage] = useState("");

  return (
    <div className="page">
      <div className="group-container">
        {/* Header */}
        <h2 className="group-title">Zen Gardeners</h2>
        <p className="group-goal">
          Goal: Growing rooftop veggies together.
        </p>

        {/* Meta info */}
        <div className="group-meta">
          <span className="badge active">Active</span>
          <span>Members: 14 / 20</span>
        </div>

        {/* Discussion */}
        <div className="discussion">
          <h4>General Discussion</h4>

          <div className="message bubble">
            Hey tribe! Should we meet this Saturday or Sunday? 🌱
          </div>
        </div>

        {/* Chat input */}
        <div className="chat-bar">
          <input
            type="text"
            placeholder="Message the tribe..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button>➤</button>
        </div>
      </div>
    </div>
  );
}
