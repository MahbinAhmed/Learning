// Map
let arr = [34,234,45,23];
let arr2 = arr.map((value, index, array)=>{
    console.log(value, index);
    return value+index;
})

// console.log(arr2);

// Filter
let arr3 = arr.filter((value,index)=>{
    // return value<40;
    return index>1;
})

// console.log(arr3);

// Reduce
let sum = arr.reduce((a,b)=>{
    return a+b;
})

console.log(sum);
console.log(typeof sum);