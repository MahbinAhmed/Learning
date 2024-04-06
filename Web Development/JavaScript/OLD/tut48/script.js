let text = document.getElementsByTagName("h2")[0];
const greet = () =>{
    console.log("Hey there!");
}

const random = (e) =>{
    console.log(e.target);
    console.log(e.clientX, e.clientY);
    console.log("Let's learn JavaScript.");
}
text.addEventListener("click", greet);
text.addEventListener("click", random);

let validator = confirm("Do you want second Event Listener to execute?");
if(validator==false){
    text.removeEventListener("click", random);
}