const prompt = require("prompt-sync")();

// Question-1
// let arr = [234,34,34,32];
// let user_inp = Number.parseInt(prompt("Enter a number:- "));
// arr.push(user_inp);
// console.log(arr);

// Question-2
// let user_inp;
// while(user_inp!=0){
//     user_inp = Number.parseInt(prompt("Enter a number:- "));
//     arr.push(user_inp);
// }

// console.log(arr);

// Question-3
// let arr = [4,52,6,90,120,340,670,30];
// let new_arr = arr.filter((value)=>{
//     return value%10==0;
// })

// console.log(new_arr);

// Question-4
// let sq_arr = arr.map((value)=>{return value*value});
// console.log(sq_arr);

// Question-5
let arr = [1,2,3,4,5];
let mul = arr.reduce((h1, h2)=>{
    return h1*h2;
})

console.log(mul);