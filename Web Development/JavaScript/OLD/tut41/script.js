console.log(document.body.getElementsByTagName("span")[0]);
console.dir(document.body.getElementsByTagName("span")[0]);

console.log(document.body.firstChild.nodeName);
console.log(document.body.firstElementChild.nodeName);

console.log(document.getElementById("first").innerHTML);
console.log(document.getElementById("first").outerHTML);
document.getElementById("first").outerHTML = "<div>This line is edited by script.js file.</div>";
console.log(document.getElementsByTagName("div")[0].outerHTML);

console.log(document.body.firstChild.data);
console.log(document.body.firstChild.textContent);
console.log(document.body.textContent);

document.getElementById("second").hidden = false;