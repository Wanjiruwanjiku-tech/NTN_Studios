// src/components/TopicCard.jsx
function TopicCard({ topic }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "12px",
      padding: "1rem",
      marginBottom: "1rem"
    }}>
      <h2>{topic.title}</h2>
      <p>{topic.description}</p>
    </div>
  );
}

export default TopicCard;
