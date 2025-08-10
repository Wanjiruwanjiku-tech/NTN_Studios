import JournalCard from "./JournalCard";

function JournalList({ entries, deleteEntry, editEntry }) {
  return (
    <div className="journal-list">
      {entries.map((entry) => (
        <JournalCard
          key={entry.id}
          entry={entry}
          deleteEntry={deleteEntry}
          editEntry={editEntry}
        />
      ))}
    </div>
  );
}

export default JournalList;
