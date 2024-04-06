// For loop
let arr = [2,34,2,4,3,5];
// for(let i=0;i<arr.length;i++){
//     console.log(arr[i]);
// }

// arr.forEach((element)=>{
//     console.log(element*element);
// })

// Array.from
let text = "Hello";
let arr2 = Array.from(text);
// arr2.forEach((a)=>{
//     console.log(a);
// })

// For of
for(let i of arr){
    console.log(i);
}

// For in
for(let i in arr){
    console.log(i);
}