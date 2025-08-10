import { useEffect, useState } from "react";
import JournalForm from "./components/JournalForm";
import JournalList from "./components/JournalList";
import QuoteBox from "./components/QuoteBox";
import "./styles/App.css";

function App() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("journalEntries")) || [];
    setEntries(saved);
  }, []);

  useEffect(() => {
    localStorage.setItem("journalEntries", JSON.stringify(entries));
  }, [entries]);

  const addEntry = (entry) => {
    setEntries([entry, ...entries]);
  };

  const deleteEntry = (id) => {
    setEntries(entries.filter((entry) => entry.id !== id));
  };

  const editEntry = (id, newText) => {
    setEntries(
      entries.map((entry) =>
        entry.id === id ? { ...entry, text: newText } : entry
      )
    );
  };

  return (
    <>
      <div className="app-container">
        <h1>Mental Health Journal</h1>
        <QuoteBox />
        <JournalForm addEntry={addEntry} />
        <JournalList
          entries={entries}
          deleteEntry={deleteEntry}
          editEntry={editEntry}
        />
      </div>
      <div className="helper-cards-grid">
        <div className="helper-card">
          <p>
            Real Meaning and Happiness comes from being of service. <blockquote>Dr. Jim Doty</blockquote>
          </p>
        </div>
        <div className="helper-card">
          <p>
            You got one wild and precious life, so go live it in a way that makes you proud <blockquote>Mel Robbins</blockquote>
          </p>
        </div>
        <div className="helper-card">
          <p>
            When nobody else celebrates you, Learn to celebrate yourself. <blockquote>Jay Shetty</blockquote>
          </p>
        </div>
      </div>
    </>
  );
}

export default App;
