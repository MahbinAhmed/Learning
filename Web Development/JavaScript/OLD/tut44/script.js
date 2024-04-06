let container = document.getElementsByClassName("container")[0];
container.insertAdjacentHTML("beforebegin", "<h1>Hey there guys!</h1>");
// container.insertAdjacentHTML("afterbegin", "<h1>Hey there guys!</h1>");
// container.insertAdjacentHTML("beforeend", "<p>How are you guys?</p>");
container.insertAdjacentHTML("afterend", "<p>How are you guys?</p>");
container.remove();