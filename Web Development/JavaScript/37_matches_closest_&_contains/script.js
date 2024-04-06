let id1 = document.getElementById("id1");
let sp1 = document.getElementById("sp1");
let a = document.getElementsByClassName("span_text")[0];
console.log(id1.matches(".text"))
console.log(id1.matches("#id1"))
console.log(sp1.closest(".body_class"));
console.log(id1.contains(a));
console.log(id1.contains(sp1));
console.log(sp1.contains(a));
console.log(sp1.contains(id1));
console.log(a.contains(id1));