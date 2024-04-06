//Conditional Expressions
let x = prompt("Enter your age:- ");
x = Number.parseInt(x);

if(x<0){
  alert("This is an invalid age.");
}

else if(x<18){
  alert("You're not adult! You can't drive.");
}

else{
  alert("You're eligible for driving.")
}

//Ternary Operator
let y = 50;
console.log("You can", y<18? "not drive" : "drive");