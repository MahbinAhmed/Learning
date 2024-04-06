let element = document.getElementsByTagName("h2")[0];
element.className = "yellow";
element.classList.add("color_cyan");
element.classList.toggle("red");
console.log(element.classList.contains("yellow"));
console.log(element.classList);