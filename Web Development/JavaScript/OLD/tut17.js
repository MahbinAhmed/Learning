let num = [1,354,45];
let b = num.toString();
// console.log(b);
// console.log(typeof b);

let c = num.join("-");
// console.log(c);

num.pop();
let d = num.pop();
// console.log(num,d);

let e = num.push(893);
// console.log(num, e);

let f = num.shift();
// console.log(num, f);

let g = num.unshift(5);
console.log(num, g);