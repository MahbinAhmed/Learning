let titles = document.getElementsByClassName("card");
titles[0].children[1].firstElementChild.style.color = "cyan";

let second_head = document.getElementsByTagName("h5")[1];
second_head.style.color = "red";

let third_head = document.getElementById("third_head");
third_head.children[1].firstElementChild.style.color = "blue";

let first_text = document.querySelector(".card-text");
first_text.style.fontWeight = "bold";

let second_text = document.querySelectorAll(".card-text")[1];
second_text.style.fontStyle = "italic";

let third_text = document.getElementsByName("third_text")[0];
third_text.style.textDecoration = "underline";