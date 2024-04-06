const prompt = require("prompt-sync")();
// Question-1
// let age = prompt("Enter your age:- ");
// age = Number.parseInt(age);
// if(age>10 && age<20){
//     console.log("Age lies between 10 and 20.");
// }
// else{
//     console.log("Age doesn't lie between 10 and 20.");

// }

// Question-2
// let age = prompt("Enter your age:- ");
// age = Number.parseInt(age);
// switch (age) {
    //     case 10:
//         console.log("You cannot drive!");
//         break;
//     case 18:
//         console.log("You are eligible for driving.");
//     default:
//         console.log("Best of luck!");
// };
// Question-3
// let num = prompt("Enter a number:- ");
// num = Number.parseInt(num);
// if(num%2==0 && num%3==0){
//     console.log("Number is divisible by 2 and 3.");
// }
// else{
//     console.log("Number is not divisible by 2 and 3.");
// }

// Question-4
// let num = prompt("Enter a number:- ");
// num = Number.parseInt(num);
// if(num%2==0 || num%3==0){
//     console.log("Number is divisible either by 2 or by 3.");
// }
// else{
//     console.log("Number is not divisible either by 2 or by 3.");
// }

// Question-5
let age = prompt("Enter your age:- ");
age = Number.parseInt(age);
console.log("You can ", age>=18? "drive.":"not drive.");