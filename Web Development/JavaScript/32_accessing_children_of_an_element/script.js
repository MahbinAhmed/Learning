// console.log(document.body.firstChild);
// console.log(typeof document.body.firstChild);
// console.log(document.body.lastChild);
// console.log(typeof document.body.lastChild);
console.log(document.body.childNodes);
console.log(typeof document.body.childNodes);
// let string = document.body.childNodes.join("-");
// console.log(string); //Throws an error as .join doesn't work with childNodes
let arr = Array.from(document.body.childNodes);
console.log(arr);
let str = arr.join(",");
console.log(str);
console.log(typeof arr);