// Question-1
let navFirstElement = document.getElementById("navHome");
navFirstElement.style.color = "red";

// Question-2
// SOLVED INSIDE HTML FILE

// Question-3
let cards = document.getElementsByClassName("container")[0];
let firstChild = cards.firstElementChild;
firstChild.style.color = "green";
let lastChild = cards.lastElementChild;
lastChild.style.color = "green";

// Question-4
let li = document.getElementsByTagName("li");
for(let i=0;i<3;i++){
    li[i].style.backgroundColor = "cyan";
}

// Question-5
// NEED REVISION