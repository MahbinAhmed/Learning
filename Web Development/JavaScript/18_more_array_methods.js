let arr = [1,34,22,4,56,43];
// delete arr[0]; //Operator
console.log(arr);

let arr2 = [12,15,81,45,21,96];
let new_arr = arr.concat(arr2);
// console.log(new_arr);

const compare = (a,b) =>{
    return a-b;
}

// arr.sort();
arr.sort(compare);
// console.log(arr);

let arr3 = arr.splice(1, 2, 5, 3);
console.log(arr);
console.log(arr3);

let arr4 = arr2.slice(2,5);
// console.log(arr4);

console.log(arr2.reverse());