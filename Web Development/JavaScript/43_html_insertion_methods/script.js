let body = document.getElementsByTagName("body")[0];
let div = document.createElement("div");
let section = document.getElementsByTagName("section")[0];
div.innerHTML = "<h1>Hello World</h1>";
section.innerHTML = section.innerHTML + div.innerHTML;
// body.appendChild(div);
// section.append(div); //Before the end of the section
// section.prepend(div); //After the start of the section
// section.before(div); //Before the start of the section
// section.after(div) //After the end of the section
// section.replaceWith(div) //Replaces the section with div