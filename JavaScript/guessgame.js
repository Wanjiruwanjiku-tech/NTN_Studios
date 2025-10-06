// script.js

// 1. Generate a random number between 1 and 10
const randomNumber = Math.floor(Math.random() * 10) + 1;

// 2. Access the DOM elements
const userGuessInput = document.querySelector('#userGuess');
const submitButton = document.querySelector('#submitGuess');
const message = document.querySelector('#message');

// 3. Add event listener to the button
submitButton.addEventListener('click', function () {
  const guess = Number(userGuessInput.value); // get user input and convert to number

  // 4. Control flow to compare guess
  if (!guess) {
    message.textContent = "⛔ Please enter a number!";
  } else if (guess < 1 || guess > 10) {
    message.textContent = "🚫 Number must be between 1 and 10.";
  } else if (guess === randomNumber) {
    message.textContent = "🎉 Correct! You guessed it!";
    submitButton.disabled = true; // optional: disable after win
  } else if (guess < randomNumber) {
    message.textContent = "📉 Too low! Try again.\n Daily Affrimation is\nYou are Worthy of Love";
  } else if (guess > randomNumber) {
    message.textContent = "📈 Too high! Try again.";
  }
});