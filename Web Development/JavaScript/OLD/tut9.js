// For Loop
// Factorial
// const prompt = require("prompt-sync")();
// let num = Number.parseInt(prompt("Enter a number:- "));
// let answer = num;
// for(let i=(answer-1); i>1;i--){
//     answer = answer*i;
// }

// console.log("Factorial of "+num+" is "+answer);

// For In Loop
const obj={
    Rohan : 50,
    John : 30,
    Alex : 32,
    Ricky : 34
}

for(let a in obj){
    console.log("Number of "+a+" is "+obj[a]);
}

// For Of Loop
for(let a of "Hello"){
    console.log(a);
}