let a = document.getElementsByTagName("div")[0];

const x = (e) =>{
    console.log("Function 1");
}

const y = (e) =>{
    console.log("Function 2");
    console.log(e.type);
    console.log(e.currentTarget);
    console.log(e.clientX, e.clientY);
}

a.addEventListener('click', x);
a.addEventListener('click', y);

a.removeEventListener('click', x);