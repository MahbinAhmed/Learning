const prompt = require("prompt-sync")();
let age = prompt("Enter your age:- ");
age = Number.parseInt(age);
let drive = false;

// if(age<=0 || age>120){
//     console.log("Invalid age!");
// }
// else if(age<10){
//     console.log("Don't even think of driving!");
// }
// else if(age<18){
//     console.log("You can drive after being 18.");
// }
// else{
//     console.log("You are eligible for driving.");
//     drive = true;
// }

// console.log("You can ", drive==true? "drive.":"not drive.");

// HOMEWORK
switch (age){
    case 10:
        console.log("You cannot drive!");
        break;
    case 18:
        console.log("You are eligible for driving.");
};