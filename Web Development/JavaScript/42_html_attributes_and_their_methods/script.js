let id1 = document.getElementById("id1");
let sp1 = document.getElementById("sp1");
console.log(id1.hasAttribute("class"));
console.log(id1.getAttribute("class"));
id1.setAttribute("class", "text red");
id1.removeAttribute("class");
console.log(id1.attributes);
console.log(sp1.dataset);
console.log(sp1.dataset.custom);