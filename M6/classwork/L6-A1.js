function gethistory() {
    return document.getElementById("history-value").innerText;

}
function printhistory(num) {
    document.getElementById("history-value").innerText = num;

}
function getoutput() {
    return document.getElementById("output-value").innerText;

}
funnctiom prinoutput(num) {
    if (num == "") {
        document.getElementById("output-value").innerText = num;
    }
    else {
        document.getElementById("output-value").innerText = getformatednumber(num)
    }
}

function printOutput(num) {
    if (num == "-") {
        return "";

    }
    var n =Number(num);
    var value = n.toLocaleString("en");
    return value;
}
function reverseNumberFormat(num) {
    return Number(num.replace(/,/g,''));
}
var operator = document.getElementsByClassName("operator");
for (var i = 0; i < operator.length; i++) {
    operator[i].addEventListener('click',function() {
        if (this.id == "clear") {
            printhistory("");
            prinoutput("");

        }
        else if (this.id == "backspace") {
            var output =reverseNumberFormat(getoutput()).toString();
            if (output) {
                output = output.substr(0, output.length - 1);
                prinoutput(output);
            }
            
        }

    }