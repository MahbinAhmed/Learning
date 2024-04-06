const prompt = require("prompt-sync")();
let round_left = 3; //Total round
let comp_score = user_score = 0; //Computer's and User's score
let comp_choice;
let user_choice;

console.log(user_score);
while(round_left>0){
    comp_choice = ["snake", "water", "gun"][Math.floor(Math.random()*3)]; //Computer's choice
    user_choice = prompt("Enter s for Snake, w for Water & g for Gun:- ");
    switch (comp_choice) {
        case "snake":
            if(user_choice=="s"){
                console.log("Computer Choice:- Snake | Your choice:- Snake");
                console.log("Round Tied!");
            }
            else if(user_choice=="w"){
                comp_score += 1;
                console.log("Computer Choice:- Snake | Your choice:- Water");
                console.log("Computer Won!")
            }
            else{
                user_score += 1;
                console.log("Computer Choice:- Snake | Your choice:- Gun");
                console.log("You Won!")
            }
            break;
    
        case "water":
            if(user_choice=="s"){
                user_score += 1;
                console.log("Computer Choice:- Water | Your choice:- Snake");
                console.log("You Won!");
            }
            else if(user_choice=="w"){
                console.log("Computer Choice:- Water | Your choice:- Water");
                console.log("Round Tied!")
            }
            else{
                comp_score += 1;
                console.log("Computer Choice:- Water | Your choice:- Gun");
                console.log("Computer Won!")
            }
            break;

        case "gun":
            if(user_choice=="s"){
                comp_score += 1;
                console.log("Computer Choice:- Gun | Your choice:- Snake");
                console.log("Computer Won!");
            }
            else if(user_choice=="w"){
                user_score += 1;
                console.log("Computer Choice:- Gun | Your choice:- Water");
                console.log("You Won!")
            }
            else{
                console.log("Computer Choice:- Gun | Your choice:- Gun");
                console.log("Round Tied!")
            }
            break;
        
        default:
            console.log("Unknown Error Occured!");
            break;
        }
    console.log(`Round ${4-round_left} completed.\n`);
    round_left--;
}

console.log("\n\n<----------Match Completed---------->");
if(user_score==comp_score){
    console.log("Match Tied!");
}
else{
    console.log(`${user_score>comp_score? "You":"Computer"} won the game!`);
}
console.log(`Your score ${user_score} || Computer score ${comp_score}`);
console.log("<----------------------------------->")