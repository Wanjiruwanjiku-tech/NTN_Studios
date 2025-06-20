// Get a refrence to an html element with the id "calculatorShow"
// and assign it to the variable calculatorShow

const calculatorShow = document.getElementById("calculatorShow");
// toDisplay function takes a parameter input then appends it to the value in calculatorShow
// using +=
function toDisplay(input) {
    calculatorShow.value += input;
}

// the try block tries to evaluate the expression in calculatorShow
// eval()takes a string and evaluates it as JavaScript code
// !!WARNING!! Using eval can be dangerous if the input is not controlled
function calculate() {
    try {
        calculatorShow.value = eval(calculatorShow.value);
    } catch (error) {
        calculatorShow.value = "Error";
    }

}

// clearDisplay function sets the value of calculatorShow to an empty string
function clearDisplay() {
    calculatorShow.value = "";
}