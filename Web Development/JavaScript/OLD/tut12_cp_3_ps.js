const prompt = require("prompt-sync")();

// Question-1
const marks = {
    John : 30,
    Alex : 40,
    Rohan : 39,
    Harry : 45
}
// for(let i=0;i<Object.keys(marks).length;i++){
//     console.log(Object.keys(marks)[i]+"'s mark = "+Object.values(marks)[i]);
// }

// Question-2

// for(let std in marks){
//     console.log(std+"'s mark = "+marks[std]);
// }

// Question-3
let correct_number = 10;
let input;
// while(true){
    // input = Number.parseInt(prompt("Enter a number:- "));
    // if(input==correct_number){
    //     console.log("Entered the corrent number!")
    //     break;
    // }
    // else{
    //     console.log("Try again!");
    //     continue;
    // }
// }

// Question-4
const mean = (a,b,c,d)=>{
    return (a+b+c+d)/4;
}

console.log(mean(10,20,30,40));