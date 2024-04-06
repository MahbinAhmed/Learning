let text = document.getElementById("text");
text.className = "dark_text yellow";
console.log(text.classList);
text.classList.add("red");
text.classList.remove("yellow");
text.classList.toggle("red");
console.log(text.classList.contains("dark_text"));