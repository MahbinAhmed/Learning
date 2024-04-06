//Primitive Data Types in JavaScript
//Mnemonic of Premitive data types in JavaScript - NN BB SS U

let a = null;
let b = 34;
let c = true;
let d = BigInt("5453") + BigInt("343");
let e = "Hello";
let f = Symbol("Hey there!");
let g = undefined; //Only declaration is enough

console.log(a, b, c, d, e, f, g);
console.log(typeof d);

//Non-Prmitive Data Types in JavaScript
const item = {
    "Alex":50,
    "John":53,
    "Rohan":34,
    "Harry":68
};
console.log(item["Rohan"]);