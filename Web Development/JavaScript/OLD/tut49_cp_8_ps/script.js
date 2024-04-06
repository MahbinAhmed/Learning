// Question-1
// let btn1 = document.getElementsByTagName("button")[0];
// let btn2 = document.getElementsByTagName("button")[1];
// let btn3 = document.getElementsByTagName("button")[2];

// const func1 = () =>{
//     alert("Alert 1");
// }

// const func2 = () =>{
//     alert("Alert 2");
// }

// const func3 = () =>{
//     alert("Alert 3");
// }

// btn1.addEventListener("click", func1);
// btn1.addEventListener("click", function(){console.log("Btn1 is clicked")});
// btn2.addEventListener("click", func2);
// btn1.addEventListener("click", function(){console.log("Btn2 is clicked")});
// btn3.addEventListener("click", func3);
// btn1.addEventListener("click", function(){console.log("Btn3 is clicked")});

// Question-2
// DONE IN THE HTML FILE.

// Question-3
// let btn1 = document.getElementsByTagName("button")[0];
// let btn2 = document.getElementsByTagName("button")[1];
// let btn3 = document.getElementsByTagName("button")[2];
// let btn4 = document.getElementsByTagName("button")[3];

// btn1.addEventListener("click", function(){window.location = "https://google.com"})
// btn2.addEventListener("click", function(){window.location = "https://youtube.com"})
// btn3.addEventListener("click", function(){window.location = "https://facebook.com"})
// btn4.addEventListener("click", function(){window.location = "https://messenger.com"})

// Question-4
// WASN'T INCLUDED IN LESSON
// const fetchContent = async (url)=>{
//     con = await fetch(url);
//     let a = await con.json();
//     return a;
// }

// setInterval(async function(){
//     let url = "https://jsonplaceholder.typicode.com/todos/1";
//     console.log(await fetchContent(url));
// }, 5000);

// Question-5
// // let bulb = document.getElementById("bulb");
// let bulb = document.getElementsByClassName("glow")[0];
// setInterval(function(){bulb.classList.toggle("glow")}, 1000);