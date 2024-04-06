const prompt = require("prompt-sync")();

// Question-1
// let age = prompt("Enter your age:- ");
// age = Number.parseInt(age);
// if(age>=10 && age<=20){
//     // alert("Your age lies between 10 and 20.");
//     console.log("Your age lies between 10 and 20");
// }
// else{
//     // alert("Your age isn't lie between 10 and 20");
//     console.log("Your age isn't lie between 10 and 20");
// }

// Question-2
// let age = prompt("Enter your age:- ");
// age = Number.parseInt(age);
// switch (age){
//     case 10:
//         console.log("Your age is 10");
//         break;
//     case 20:
//         console.log("Your age is 20");
//         break;
//     case 30:
//         console.log("Your age is 30");
//         break;
//     default:
//         console.log("You're a human.")
// }

// Question-3
// let num = prompt("Enter a number:- ");
// num = Number.parseInt(num);
// if(num%2==0 && num%3==0){
//     console.log("Your number is divisible by 2 and 3");
// }
// else{
//     console.log("Your number isn't divisible by 2 and 3");
// }

// Question-4
// let num = prompt("Enter a number:- ");
// num = Number.parseInt(num);
// if(num%2==0 || num%3==0){
//     console.log("Your number is either divisible by 2 or 3");
// }
// else{
//     console.log("Your number is neither divisible by 2 nor 3");
// }

// Question-5
let age = Number.parseInt(prompt("Enter your age:- "));
let text = age>=18? "You can drive":"You can't drive";
console.log(text);