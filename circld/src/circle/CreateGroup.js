import { useNavigate } from "react-router-dom";
import { useState } from "react";

const CATEGORIES = ["Sports", "Dance", "Walking", "Reading", "Gym", "Social"];

export default function CreateGroup() {
  const navigate = useNavigate();
  
  // These are the "missing" definitions from your error log
  const [groupName, setGroupName] = useState("");
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");
  const [isPrivate, setIsPrivate] = useState(false);

  const handleCreate = (e) => {
    e.preventDefault();
    console.log("Group Created:", { groupName, category, description, isPrivate });
    navigate("/home");
  };

  return (
    /* 'page center' ensures it uses the full screen, not just one side */
    <div className="page center"> 
      <div className="create-group-wrapper">
        <form className="card" onSubmit={handleCreate} style={{ width: '100%', maxWidth: '500px' }}>
          <h2>Create a New Circle</h2>
          <p className="muted">Start a group and invite people nearby.</p>

          <input
            type="text"
            placeholder="Group Name"
            value={groupName}
            onChange={(e) => setGroupName(e.target.value)}
            required
          />

          <div className="activities-section">
            <p className="section-title">Category</p>
            <div className="activities-grid">
              {CATEGORIES.map((cat) => (
                <label key={cat} className={`activity-item ${category === cat ? "selected" : ""}`}>
                  <input
                    type="radio"
                    name="category"
                    value={cat}
                    onChange={(e) => setCategory(e.target.value)}
                    style={{ display: 'none' }}
                  />
                  <span>{cat}</span>
                </label>
              ))}
            </div>
          </div>

          <textarea
            placeholder="Description..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />

          <div className="button-group">
            <button type="button" className="secondary" onClick={() => navigate("/home")}>
              Cancel
            </button>
            <button type="submit">Create Group</button>
          </div>
        </form>
      </div>
    </div>
  );
}