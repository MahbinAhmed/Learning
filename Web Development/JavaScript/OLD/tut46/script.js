const greet=(a,b)=>{
    alert(`Hello User! ${a}+${b}=${a+b}`);
}

let element = document.getElementsByTagName("h2")[0];
element.classList.add("yellow");

let timer = setTimeout(greet, 3000, 4,5);
let confirmation = confirm("Do you want to be greeted?");
if(confirmation==false){
    clearTimeout(timer);
}

const color_change=()=>{
    let element = document.getElementsByTagName("h2")[0];
    element.classList.toggle("red");
}

let animation = setInterval(color_change, 5000);