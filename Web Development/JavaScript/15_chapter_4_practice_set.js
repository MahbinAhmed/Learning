const prompt = require("prompt-sync")();
// Question-1
// console.log("har\"".length);

// Question-2
let sentence = "A quick brown fox jumps over the lazy dogs";
// console.log(sentence.includes("fox"));
// console.log(sentence.startsWith("q",2));
// console.log(sentence.endsWith("dogs"));

// Question-3
// let user_inp = prompt("Enter a string:- ");
// console.log(user_inp.toLowerCase());

// Question-4
// let string = "Please give Rs 1000";
// console.log(string.slice(-4));

// Question-5
let user_inp = prompt("Enter a string:- ");
// user_inp[3] = "x";
console.log(user_inp[3]);
user_inp = user_inp.replace(user_inp[3], "x");
console.log(user_inp);