// DOM element selection

const buttons = document.querySelectorAll('button');
const userChoiceDisplay = document.querySelector('#user-choice');
const computerChoiceDisplay = document.getElementById('computer-choice');
const resultDisplay = document.querySelector('#result');

// The three possible choices

const choices = ["rock", "paper", "scissors"];

// Listen for events
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const userChoice = button.dataset.choice;
        const computerChoice = getComputerChoice();
        const result = getResult(userChoice, computerChoice);

        // Update the UI
        userChoiceDisplay.textContent = `You Chose: ${userChoice}`;
        computerChoiceDisplay.textContent = `Computer Chose: ${computerChoice}`;
        resultDisplay.textContent = `Result: ${result}`;
    });
});

// Get Computer choice

function getComputerChoice() {
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
}

// Get Result

function getResult(user, computer) {
    if (user === computer) {
        return "It's a draw!";
    } else if (
        (user === "rock" && computer === "scissors") ||
        (user === "paper" && computer === "rock") ||
        (user === "scissors" && computer === "paper")
    ) {
        return "You win!🎉";
    } else {
        return "You lose!😢";
    }
}