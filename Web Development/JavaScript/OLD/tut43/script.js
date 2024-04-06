let text = document.createElement("div");
text.innerHTML = "<h2>Let's learn JS!</h2>"

let container = document.getElementsByClassName("container")[0];
container.appendChild(text);

let text2 = document.createElement("span");
text2.innerHTML = "This line is inside span tag.";
// container.append(text2);
container.prepend(text2);
container.before(text2);
container.after(text2);
container.getElementsByTagName("div")[0].replaceWith(text2);