let num = [1,3,4,2,9,4,5,32,5,3434,3,34,8];
delete num[1];
// console.log(num);

let num2 = [44,69,420,171];
let num3 = [56,96,90];

// let concat_array = num.concat(num2, num3);
// console.log(concat_array);
// console.log(num, num2);

// num.sort();
// console.log(num);

let compare = (a,b)=>{
    return a-b;
}

num.sort(compare);
// console.log(num);

num.reverse();
// console.log(num);

let arr = [5,6,34,3];
// arr.splice(2,0, 44, 69);
// console.log(arr);

let new_arr = arr.slice(1,3);
console.log(new_arr);