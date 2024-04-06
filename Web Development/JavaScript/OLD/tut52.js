// Syncronous programming
// let a = prompt("Enter value of a:- ");
// let b = prompt("Enter value of b:- ");
// let c = prompt("Enter value of c:- ");
// console.log(a,b,c);

// Asyncronous programming
// console.log("Start");
// setTimeout(function(){console.log("Text from Time Out")}, 3000);
// console.log("End!");

function calculator(arg1, arg2, func1){
    let result = arg1 + arg2;
    if(func1){
        func1(result);
    }
    else{
        return result;
    }
}

const display=(value)=>{
    console.log("The result is " + value);
}

console.log(calculator(5,34));
calculator(54,3, display);