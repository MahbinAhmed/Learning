let text = document.getElementsByTagName("h2")[0];
text.onmouseenter = () =>{
    console.log("Mouse is hovered on h2 tag.");
}

text.onclick = () =>{
    text.innerHTML = "You've clicked the text!"
}