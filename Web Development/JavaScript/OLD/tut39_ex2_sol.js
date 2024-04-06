const prompt = require("prompt-sync")();

/*1 = Rock
2 = Paper
3 = Scissor*/

let com_point = 0;
let user_point = 0;
let user_choice;

for(let i = 0;i<10;i++){
    console.log(`Round no. ${i+1}`);
    
    // Computer's turn
    let com_choice = Math.floor(Math.random()*(3-1+1))+1;

    user_choice = prompt("Choose between R, P or S:- ");
    if(com_choice==1){
        if(user_choice=="R" || user_choice=="r"){
            console.log("Round drawn.")
            console.log(`Your choice: Rock | Computer's choice: Rock`);
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="P" || user_choice=="p"){
            console.log("You won!")
            console.log(`Your choice: Paper | Computer's choice: Rock`);
            user_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="S" || user_choice=="s"){
            console.log("Computer won!")
            console.log(`Your choice: Scissor | Computer's choice: Rock`);
            com_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else{
            console.log("Enter a valid input!");
            i--;
        }
    }
    else if(com_choice==2){
        if(user_choice=="R" || user_choice=="r"){
            console.log("Computer won!")
            console.log(`Your choice: Rock | Computer's choice: Paper`);
            com_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="P" || user_choice=="p"){
            console.log("Round drawn.")
            console.log(`Your choice: Paper | Computer's choice: Paper`);
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="S" || user_choice=="s"){
            console.log("You won!")
            console.log(`Your choice: Scissor | Computer's choice: Paper`);
            user_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else{
            console.log("Enter a valid input!");
            i--;
        }
    }
    else if(com_choice==3){
        if(user_choice=="R" || user_choice=="r"){
            console.log("You won!")
            console.log(`Your choice: Rock | Computer's choice: Scissor`);
            user_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="P" || user_choice=="p"){
            console.log("Computer won!")
            console.log(`Your choice: Paper | Computer's choice: Scissor`);
            com_point+=1;
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else if(user_choice=="S" || user_choice=="s"){
            console.log("Round draw.")
            console.log(`Your choice: Scissor | Computer's choice: Scissor`);
            console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
        }
        else{
            console.log("Enter a valid input!");
            i--;
        }
    }
    console.log("\n");
}
console.log("\n\n");
if(user_point>com_point){
    console.log("Congratulations! You've won the game!")
    console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
}
else if(user_point<com_point){
    console.log("Computer won the game!")
    console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
}
else{
    console.log("Match drawn!")
    console.log(`Your point: ${user_point} | Computer's point: ${com_point}`);
}