// Question-1
// let age = prompt("Enter your age:- ", -50);
// age = Number.parseInt(age);
// let drive = false;

// if (age <= 0 || age > 120) {
//     alert("Invalid age!");
// }
// else if (age < 10) {
//     alert("Don't even think of driving!");
// }
// else if (age < 18) {
//     alert("You can drive after being 18.");
// }
// else {
//     alert("You are eligible for driving.");
//     drive = true;
// }

// Question-2
// let confirmation = confirm("Do you want to see the prompt again?");
// if (confirmation) {
//     age = prompt("Enter your age:- ");
//     age = Number.parseInt(age);
//     let drive = false;

//     if (age <= 0 || age > 120) {
//         alert("Invalid age!");
//     }
//     else if (age < 10) {
//         alert("Don't even think of driving!");
//     }
//     else if (age < 18) {
//         alert("You can drive after being 18.");
//     }
//     else {
//         alert("You are eligible for driving.");
//         drive = true;
//     }
// }

// Question-3
// let confirmation = confirm("Do you want to see the prompt again?");
// if (confirmation) {
//     age = prompt("Enter your age:- ");
//     age = Number.parseInt(age);
//     let drive = false;

//     if (age > 120) {
//         alert("Invalid age!");
//     }
//     else if(age<=0){
//         console.error("Negative value of age!");
//     }
//     else if (age < 10) {
//         alert("Don't even think of driving!");
//     }
//     else if (age < 18) {
//         alert("You can drive after being 18.");
//     }
//     else {
//         alert("You are eligible for driving.");
//         drive = true;
//     }
// }

// Question-4
// let user_inp = prompt("Enter a value:- ");
// if(user_inp>4){
//     location.href = "https://google.com";
// }

// Question-5
let user_inp = prompt("Enter a color name:- ");
document.body.style.background = user_inp;