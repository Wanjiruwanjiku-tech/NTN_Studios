import { useState } from "react";

function JournalCard({ entry, deleteEntry, editEntry }) {
  const [isEditing, setIsEditing] = useState(false);
  const [newText, setNewText] = useState(entry.text);

  const handleEdit = () => {
    if (isEditing && newText !== entry.text) {
      editEntry(entry.id, newText);
    }
    setIsEditing(!isEditing);
  };

  return (
    <div className="journal-card">
      <div className="card-content">
        <p className="date">{entry.date}</p>
        {isEditing ? (
          <textarea value={newText} onChange={(e) => setNewText(e.target.value)} />
        ) : (
          <p>{entry.text}</p>
        )}
      </div>
      <div className="card-actions">
        <button onClick={handleEdit}>{isEditing ? "Save" : "Edit"}</button>
        <button onClick={() => deleteEntry(entry.id)}>Delete</button>
      </div>
    </div>
  );
}

export default JournalCard;
