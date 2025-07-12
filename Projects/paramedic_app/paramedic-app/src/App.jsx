import { Routes, Route } from 'react-router-dom';
import topics from './data/topics.json';
import TopicCard from './components/TopicCard';
import TopicDetail from './components/TopicDetail'; // to be created
import Navbar from './components/Navbar'; 

function App() {
  return (
    <>
      <Navbar />
      <div style={{ padding: "2rem" }}>
        
        <h1>Paramedic Learning App</h1>

        <Routes>
          <Route
            path="/"
            element={
              <>
                <p>Topics loaded: {topics.length}</p>
                {topics.map((topic) => (
                  <TopicCard key={topic.id} topic={topic} />
                ))}
              </>
            }
          />
          <Route path="/topics/:id" element={<TopicDetail />} />
        </Routes>
      </div>
      
    </>
  );
}

export default App;
