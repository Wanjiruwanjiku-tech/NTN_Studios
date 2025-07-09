import topics from './data/topics.json';
import TopicCard from './components/TopicCard';

function App() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>Paramedic Learning App</h1>
      {topics.map(topic => (
        <TopicCard key={topic.id} topic={topic} />
      ))}
    </div>
  );
}

export default App;