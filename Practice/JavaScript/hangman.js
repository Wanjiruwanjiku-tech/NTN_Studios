// Hangmans Game
// This is a simple implementation of the Hangman game in JavaScript.
// 1. The computer contains the words to guess in an array.
// 2. The player guesses a letter for the selected word, if selected letter is in the generated word, the computer will display the letter in the correct position.

// DOM elements
const userGuess = document.querySelector('#guess');
const submitButton = document.querySelector('#submit');
const message = document.querySelector('#message');
const wordDisplay = document.querySelector('#word');

// Logic Generating a Random word
const wordsContainer = ["Zootopia", "Wakanda", "Matrix", "Inception", "Matata"];

// Generate a random index
const randomWord = Math.floor(Math.random() * wordsContainer.length);
// Get the word represented by the random index
const myWord = wordsContainer[randomWord];
const word = myWord.toLowerCase();
// Split word into letters
const wordArray = word.split('');
let displayWord = Array(wordArray.length).fill('_').join(' ');

// Show to Player
wordDisplay.textContent = displayWord;

// HANDLE USER INPUT
// Regex for lowercase letters only
const lowerCaseLetters = /^[a-z]$/;
// Event listener for the submit button
submitButton.addEventListener('click', () => {
    const guess = userGuess.value.toLowerCase();

    if (!lowerCaseLetters.test(guess)) {
        message.textContent = 'Please enter a valid lowercase letter.';
        message.style.color = 'crimson';
        // Clear the input field after submission
        userGuess.value = '';
        userGuess.focus();
        return;
    } 

    let found = false;

    // reveal matching letters
    for (let i = 0; i < wordArray.length; i++) {
        if (wordArray[i] === guess) {
            displayWord = displayWord.split(' ');
            displayWord[i] = guess;
            displayWord = displayWord.join(' ');
            found = true;
        }
    }

    // Update the displayed word
    wordDisplay.textContent = displayWord;

    // Check if the word is fully guessed
    if (found) {
        message.textContent = `Congratulations! "${word}" Is Correct!`;
        message.style.color = 'green';
    } else {
        message.textContent = 'Incorrect guess. Try again!';
        message.style.color = 'crimson';
    }

    // Clear the input field after submission
    userGuess.value = '';
    userGuess.focus();
})
