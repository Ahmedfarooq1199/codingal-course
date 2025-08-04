function clearScreen() {
    const screen = document.getElementById("result").value="";

   
}
function setScreenValue(value) {
    document.getElementById("result").value += value;
}
function calculateResult() {
    const resultElement = document.getElementById("result");
    const expression = resultElement.value.trim();
    if (expression === "") {
        resultElement.value = "Please enter a valid expression";
        return;
    }
    try {
        resultElement.value = eval(expression);
    } catch (error) {
        resultElement.value = 'Invalid expression'
    }
}