const quotes = [
  "You are enough.",
  "Every day is a fresh start.",
  "You are loved.",
  "Peace begins with you.",
  "You are doing the best you can.",
];

function QuoteBox() {
  const quote = quotes[new Date().getDate() % quotes.length];

  return (
    <div className="quote-box">
      <h3>🌞 Daily Affirmation</h3>
      <p>{quote}</p>
    </div>
  );
}

export default QuoteBox;