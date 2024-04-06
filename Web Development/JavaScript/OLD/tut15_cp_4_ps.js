const prompt = require("prompt-sync")();

// Question-1
let str = "har\""
// console.log(str.length);

// Question-2
let sentence = "A quick brown fox jumps over the lazy dogs";
// console.log(sentence.startsWith("A"));
// console.log(sentence.endsWith("brown"));
// console.log(sentence.includes("fox"));

// Question-3
// let given_string = prompt("Enter a string:- ");
// console.log(given_string.toLowerCase());

// Question-4
let str2 = "Please give Tk 1000";
let amount = str2.slice("Please give Tk ".length);
// console.log(amount);
// console.log(typeof amount);
// amount = Number.parseInt(amount);
// console.log(typeof amount);

// Question-5
let text = "Hello";
text[3] = "k";
console.log(text);