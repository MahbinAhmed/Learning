const prompt = require("prompt-sync")();

// While Loop
let n = prompt("Enter the value of n:- ");
n = Number.parseInt(n);
let i=0;
while(i<n){
    console.log(i);
    i++;
}

// Do While Loop
// let n = prompt("Enter the value of n:- ");
// n = Number.parseInt(n);
// let i=0;
// do{
//     console.log(i);
//     i++;
// }while(i<n)