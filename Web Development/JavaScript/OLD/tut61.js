const prompt = require("prompt-sync")();

// try {
//     // hello;
//     throw new SyntaxError("This systax is not right");
// } catch (error) {
//     console.log(error);
//     console.log(error.name);
//     console.log(error.message);
// }

let age = Number.parseInt(prompt("Enter your age:- "));
try {
    if(age>150){
        throw new TypeError("Age is Invalid");
    }
} catch (error) {
    console.log(error.name);
    console.log(error.message);
}