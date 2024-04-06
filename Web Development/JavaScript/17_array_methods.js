let arr = [2,4,7,3,8,5];

let s = arr.toString();
console.log(s, typeof s);

let t = arr.join(" - ");
console.log(t, typeof t);

let a = arr.pop(); //Removes the last element of an array and returns it
console.log(arr);
console.log(a);

let b = arr.push(1); //Adds an element at the end of an array and returns the new array length
console.log(arr);
console.log(b);

let c = arr.shift(); //Removes the first element of an array and returns it
console.log(arr);
console.log(c);

let d = arr.unshift(6) //Adds an element at the beginning of an array and returns the new array length
console.log(arr);
console.log(d);