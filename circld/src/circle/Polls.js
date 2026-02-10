import { useState } from "react";

export default function Polls() {
  const [polls, setPolls] = useState([
    {
      id: 1,
      question: "Which day works best for the meetup?",
      options: [
        { text: "Saturday", votes: 2 },
        { text: "Sunday", votes: 3 }
      ],
      voted: false
    },
    {
      id: 2,
      question: "Which cafe should we choose?",
      options: [
        { text: "Cafe Mocha", votes: 1 },
        { text: "Green Bean", votes: 4 },
        { text: "Brew Lab", votes: 2 }
      ],
      voted: false
    }
  ]);

  const vote = (pollId, index) => {
    setPolls(
      polls.map((poll) =>
        poll.id === pollId && !poll.voted
          ? {
              ...poll,
              voted: true,
              options: poll.options.map((opt, i) =>
                i === index
                  ? { ...opt, votes: opt.votes + 1 }
                  : opt
              )
            }
          : poll
      )
    );
  };

  return (
    <div className="page">
      <h2>Polls</h2>

      <div className="grid">
        {polls.map((poll) => (
          <div className="card" key={poll.id}>
            <h3>{poll.question}</h3>

            {poll.options.map((option, index) => (
              <button
                key={index}
                className="poll-option"
                disabled={poll.voted}
                onClick={() => vote(poll.id, index)}
              >
                {option.text}
                <span>{option.votes}</span>
              </button>
            ))}

            {poll.voted && <p className="voted-text">You voted</p>}
          </div>
        ))}
      </div>
    </div>
  );
}
