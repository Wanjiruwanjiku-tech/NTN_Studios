import { useState } from 'react';

function Quiz({ questions }) {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selected, setSelected] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);

  const handleSelect = (option) => {
    setSelected(option);
  };

  const handleNext = () => {
    if (selected === questions[currentQuestion].answer) {
      setScore(score + 1);
    }

    setSelected(null);

    if (currentQuestion + 1 < questions.length) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      setShowResult(true);
    }
  };

  if (showResult) {
    return (
      <div style={{ marginTop: "2rem", padding: "1rem", border: "2px solid #007bff", borderRadius: "10px", backgroundColor: "#f1f8ff" }}>
        <h3>Quiz Complete!</h3>
        <p>Your score: <strong>{score} / {questions.length}</strong></p>
        <p>{score === questions.length ? 'Perfect!' : 'Great job, keep learning!'}</p>
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div style={{ marginTop: "2rem", padding: "1rem", border: "2px solid #007bff", borderRadius: "10px", backgroundColor: "#f1f8ff" }}>
      <h3>Quiz</h3>
      <p><strong>Q{currentQuestion + 1}:</strong> {question.question}</p>
      {question.options.map((option, idx) => (
        <div key={idx} style={{ marginBottom: "0.5rem" }}>
          <label>
            <input
              type="radio"
              name="quiz"
              value={option}
              checked={selected === option}
              onChange={() => handleSelect(option)}
              style={{ marginRight: "0.5rem" }}
            />{" "}
            {option}
          </label>
        </div>
      ))}
      <button 
        onClick={handleNext} 
        disabled={!selected} 
        style={{
          marginTop: "1rem",
          padding: "0.5rem 1rem",
          backgroundColor: "#28a745",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        {currentQuestion + 1 < questions.length ? "Next" : "Submit"}
      </button>
    </div>
  );
}

export default Quiz;