let a = prompt("Enter a number:- ","50");
// a = Number.parseInt(a);
let confirmation = confirm("Are you sure to confirm?");
if(confirmation){
    document.write(a);
}
else{
    document.write("Permission denied by the user.");
}