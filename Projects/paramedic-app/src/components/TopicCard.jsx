// src/components/TopicCard.jsx
import { Link } from 'react-router-dom';

function TopicCard({ topic }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "10px",
      padding: "1rem",
      marginBottom: "1rem",
      backgroundColor: "#f9f9f9"
    }}>
      <h2>{topic.title}</h2>
      <p>{topic.description}</p>
      <Link to={`/topics/${topic.id}`}>
        <button style={{
          marginTop: "1rem",
          padding: "0.5rem 1rem",
          borderRadius: "5px",
          backgroundColor: "#007bff",
          color: "#fff",
          border: "none",
          cursor: "pointer"
        }}>
          Learn More
        </button>
      </Link>

      {topic.quiz && topic.quiz.length > 0 && (
        <Link to={`/topics/${topic.id}/quiz`}>
          <button style={{
            marginTop: "1rem",
            marginLeft: "1rem",
            padding: "0.5rem 1rem",
            borderRadius: "5px",
            backgroundColor: "#007bff",
            color: "#fff",
            border: "none",
            cursor: "pointer"
          }}>
            Start Quiz
          </button>
        </Link>
      )}

    </div>
  );
}

export default TopicCard;
