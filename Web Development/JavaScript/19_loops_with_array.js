let arr = [2,34,32,3,345,43];

// for(let i=0; i<arr.length; i++){
//     console.log(arr[i]);
// }

// arr.forEach((a)=>{
//     console.log(a*2);
// })

let str = "Hello";
let arr2 = Array.from(str); //Mainly used to covert HTML collection into array
// console.log(arr2);

// for(let i of arr){
//     console.log(i);
// }

for(let i in arr){
    console.log(i);
}