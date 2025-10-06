import { useParams, Link } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import topics from '../data/topics.json';
import Quiz from './Quiz';

function TopicDetail() {
  const { id } = useParams();
  const topic = topics.find(t => t.id === id);

  if (!topic) return <p>Topic not found.</p>;

 return (
  <div style={{ padding: "1rem" }}>
    <h2>{topic.title}</h2>
    <ReactMarkdown>{topic.content}</ReactMarkdown>

    {topic.quiz && topic.quiz.length > 0 && (
      <Quiz questions={topic.quiz} />
    )}

    <Link to="/">
      <button style={{
        marginTop: "2rem",
        padding: "0.5rem 1rem",
        backgroundColor: "#28a745",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer"
      }}>
        ← Back to Home
      </button>
    </Link>
  </div>
);
}

export default TopicDetail;
