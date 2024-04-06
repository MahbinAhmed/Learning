const prompt = require("prompt-sync")();

// Question-1
// const marks = {
//     Rohan:30,
//     Harry:39,
//     Alex:49,
//     John:40,
//     Henry:45
// }

// for(let i=0; i<Object.keys(marks).length; i++){
//     console.log("The marks of ", Object.keys(marks)[i], " is ", Object.values(marks)[i]);
// }

// Question-2
// const marks = {
//     Rohan:30,
//     Harry:39,
//     Alex:49,
//     John:40,
//     Henry:45
//  }

// for(let a in marks){
//     console.log("The marks of ", a, " is ", marks[a]);
// }

// Question-3
// let num = 50;
// let user_inp;
// do{
//     user_inp = Number.parseInt(prompt("Enter the number:- "));
//     if(user_inp==num){
//         break;
//     }
//     else{
//         console.log("try again");
//     }
// }while(user_inp!=num)

// Question-4
const mean = (a, b, c, d, e) =>{
    return (a+b+c+d+e)/5
}

console.log(mean(50,51,52,53,54));