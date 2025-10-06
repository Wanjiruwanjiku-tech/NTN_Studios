// Character Profile Generator that creates a small script that randomly generates a character profile.
// Learning Objectives:
// 1. How to store data in varibles, arrays and objects.
// 2. How to use Math.random() to generate random elements
// 3. How to organize and print out meaningful output to the console.

const names = [
    "Wanjiru",
    "Ajooni",
    "Bahati",
    "Chinedu",
    "Fatima",
    "Hiroshi",
    "Leila",
    "Nia"
];

const tribes =[
    "Maasai",
    "Punjabi",
    "Swahili",
    "Igbo",
    "Hausa",
    "Japanese",
    "Arab",
    "Zulu"
];

const powers = [
    "Super strength",
    "Telepathy",
    "Invisibility",
    "Flight",
    "Time travel",
    "Shape-shifting",
    "Healing",
    "Elemental control"
];

// We have array as a placeholder that can be filled with any data when the function is called.

function getRandomCharacterProfile(array) {
    // Math.random() generates a random number between 0 (inclusive) and 1 (exclusive). ie decimal
    // Math.floor() rounds down to the nearest whole number.
    // To get a random index for an array, we multiply Math.random() by the length
    const randomIndex = Math.floor(Math.random() * array.length);
    return array[randomIndex];
};

// Now we can use the getRandomCharacterProfile function to generate a character profile
const characterProfile = {
    name: getRandomCharacterProfile(names),
    tribe: getRandomCharacterProfile(tribes),
    power: getRandomCharacterProfile(powers),
    age: Math.floor(Math.random() * 100) + 18, // Random age between 18 and 100
};

// Print the character profile to the console
console.log("New Character Profile");
console.log(`Name: ${characterProfile.name}`);
console.log(`Tribe: ${characterProfile.tribe}`);
console.log(`Power: ${characterProfile.power}`);
console.log(`Age: ${characterProfile.age}`);