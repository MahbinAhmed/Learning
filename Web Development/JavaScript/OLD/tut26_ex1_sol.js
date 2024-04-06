const prompt = require("prompt-sync")();

// Random number between 1 to 100
let rand_num = Math.floor(Math.random()*(100-1+1))+1;
// console.log(rand_num);

let point = 100;
let corrent_guess = false;
let user_inp;

while(point>0){
    console.log(`${point} ${point>1? "attempts":"attempt"} left.`)
    user_inp = Number.parseInt(prompt("Enter a positive integer:- "));
    if(user_inp==rand_num){
        corrent_guess=true;
        console.log("\nYou've entered the correct number!")
        break;
    }
    else if(user_inp<rand_num){
        point--;
        console.log("Enter a greater number.\n");
        continue;
    }
    else if(user_inp>rand_num){
        point--;
        console.log("Enter a lesser number.\n");

    }
    else{
        point--;
        console.log("Enter a valid input.");
    }

}

if(corrent_guess==false){
    console.log("You are run out of attempts!");
}
else{
    console.log(`Your score is ${point}`);
}