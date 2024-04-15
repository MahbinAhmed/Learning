// Quesiton-1
let btn_1 = document.getElementsByTagName("div")[0];
let btn_2 = document.getElementsByTagName("div")[1];
let btn_3 = document.getElementsByTagName("div")[2];

btn_1.onclick = function(){
    alert("Button 1 has been clicked!");
}

btn_2.onclick = function(){
    alert("Button 2 has been clicked!");
}

btn_3.onclick = function(){
    alert("Button 3 has been clicked!");
}

// Quesiton-2
// DONE IN HTML FILE

// Quesiton-3
let b1 = document.getElementsByTagName("button")[0];
let b2 = document.getElementsByTagName("button")[1];
let b3 = document.getElementsByTagName("button")[2];

b1.addEventListener('click', function(){
    window.location.href = "https://google.com";
})

b2.addEventListener('click', function(){
    window.location.href = "https://youtube.com";
})
b3.addEventListener('click', function(){
    window.location.href = "https://github.com";
})

// Quesiton-4
const fetchContent = async(url) =>{
    let con = await fetch(url);
    let a = await con.json();
    return a;
}
// setInterval(async function(){
//     let api = "https://jsonplaceholder.typicode.com/todos/1"
//     console.log(await fetchContent(api));
// }, 5000);

// Quesiton-5
let bulb = document.getElementsByClassName("bulb")[0];

setInterval(() => {
    bulb.classList.toggle("glow");
}, 500);