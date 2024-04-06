// Arrays
let arr = [1,3,null, "Hello"];
console.log(arr);
console.log(arr.length);
console.log(arr[3]);
arr[6] = "World";
arr[1] = 34;
console.log(arr);
console.log(typeof arr);

for(let i=0;i<arr.length;i++){
    console.log(arr[i]);
}