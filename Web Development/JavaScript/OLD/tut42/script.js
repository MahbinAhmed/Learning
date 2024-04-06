let first = document.getElementById("first");
console.log(first.hasAttribute("class"));
console.log(first.setAttribute("class", "text"));
console.log(first.getAttribute("class"));
console.log(document.getElementById("second").removeAttribute("hidden"));

// Custom Attributes
console.log(document.getElementById("second").dataset);
console.log(document.getElementById("second").dataset.course);
console.log(document.getElementById("second").dataset.tutor);
console.log(document.getElementById("second").hasAttribute("data-course"));