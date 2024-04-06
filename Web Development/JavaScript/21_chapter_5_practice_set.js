const prompt = require("prompt-sync")();

// Question-1
let arr = [2,34,4,5,30,110,21,50,450,520];
// let user_inp = Number.parseInt(prompt("Enter a number:- "));
// arr.unshift(user_inp);
// console.log(arr);

// Question-2
// let user_inp;
// do{
//     user_inp = Number.parseInt(prompt("Enter a number:- "));
//     arr.push(user_inp);
// }while(user_inp!=0);
// console.log(arr);

// Question-3
// let new_arr = arr.filter((a)=>{
//     return a%10==0;
// })
// console.log(new_arr);

// Question-4
// let new_arr2 = arr.map((a)=>{
//     return a*a;
// })
// console.log(new_arr2)

// Question-5
let array = [1,2,3,4,5,6,7,8,9,10];
let factorial = array.reduce((a,b)=>{
    return a*b;
})
console.log(factorial);