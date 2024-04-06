const prompt = require("prompt-sync")();
let num = Math.floor(Math.random()*100)+1 //Generating random number
let total_attempt = 0;
let score = 100;
let user_inp;

do{
    user_inp = Number.parseInt(prompt("Enter your guess:- ")); //Taking input from the user
    if(user_inp<num){
        total_attempt += 1;
        score = 100 - total_attempt;
        console.log("Enter a greater number!");
    }
    else if(user_inp==num){
        total_attempt += 1;
        score = 100 - total_attempt;
        console.log("\nCongratulations! You've entered the correct number!");
        break;
    }
    else{
        total_attempt += 1;
        score = 100 - total_attempt;
        console.log("Enter a lesser number!");
    }
}while(user_inp!=num && total_attempt<100);

console.log("\n\n-------------------------")
console.log(`The correct number is ${num}`);
console.log(`You've took ${total_attempt} ${total_attempt>1? "attempts":"attempt"}`);
console.log(`Your score is ${score}`);
console.log("-------------------------\n")