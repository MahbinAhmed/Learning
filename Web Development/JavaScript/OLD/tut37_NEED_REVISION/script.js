let cards = document.querySelectorAll(".card");
cards[1].style.margin = "20px";
// console.log(cards);

let firstCard = document.querySelector(".card");
console.log(firstCard)
firstCard.style.borderColor = "red";

let firstCardId = document.getElementById("firstCard");
let h1FirstCard = firstCardId.getElementsByTagName("h1")[0];
// console.log(firstCardId)
console.log(h1FirstCard);
h1FirstCard.style.color = "green";

let thirdCard = document.getElementsByClassName("card")[2];
thirdCard.style.borderColor = "blue";