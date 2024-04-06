alert("Welcome to our website");
let a = prompt("Enter a value:- ", 34);
a = Number.parseInt(a);
let confirmation = confirm("Do you want the value to be written on the page?");
if(confirmation){
    document.write(a);
}
else{
    console.log("Writing operation stopped by the user");
}