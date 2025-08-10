import { useState } from "react";

function JournalForm({ addEntry }) {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    const entry = {
      id: Date.now(),
      text,
      date: new Date().toLocaleDateString(),
    };

    addEntry(entry);
    setText("");
  };

  return (
    <form onSubmit={handleSubmit} className="journal-form">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Write your thoughts..."
        rows={4}
      />
      <button type="submit">Save Entry</button>
    </form>
  );
}

export default JournalForm;
