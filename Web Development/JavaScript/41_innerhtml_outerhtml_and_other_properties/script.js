let x = document.getElementsByTagName("div")[0];
console.log(x);
console.dir(x);
console.log(document.body.firstChild.nodeName);
console.log(document.body.firstElementChild.nodeName);

let id1 = document.getElementById("id1");
console.log(id1.innerHTML);
// id1.innerHTML = "<b>Hello Bangladesh</b>"
console.log(id1.outerHTML);
// id1.outerHTML = "<div><b>Hello BD</b></div>";
console.log(id1.innerText)
id1.innerText = "<b>Hello Duniya</b>"